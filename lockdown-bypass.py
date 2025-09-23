from Cocoa import *
import objc
import time
import psutil
import os

# ----------------- Settings ------------------
waitTime = 15  # seconds to wait for user to click LockDown URL
appName = "He3"  # actual Helium app is "He3" in process list
# ---------------------------------------------

def get_helium_pids():
    pids = []
    for proc in psutil.process_iter():
        try:
            if appName.lower() in proc.name().lower():
                pids.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pids

def bring_to_front(pids):
    for pid in pids:
        print(f"Attempting to bring PID {pid} to front...")
        x = NSRunningApplication.runningApplicationWithProcessIdentifier_(pid)
        if x is not None:
            try:
                x.hide()
                time.sleep(1)
                x.unhide()
                print(f"✅ PID {pid} was brought to front.")
            except Exception as e:
                print(f"⚠️ Failed to bring to front: {e}")
        else:
            print(f"⚠️ PID {pid} not found as running application (x is None).")

def launch_helium(instances=1):
    print(f"🔁 Launching {instances} instance(s) of {appName}...")
    for _ in range(instances):
        os.system(f"open -n -a {appName}.app")
    time.sleep(1)

# Step 1: Ensure Helium is running
helium_pids = get_helium_pids()
if not helium_pids:
    print(f"⚠️ {appName} not running. Launching now...")
    launch_helium(instances=1)
    helium_pids = get_helium_pids()
    if not helium_pids:
        print("❌ Failed to launch Helium.")
        exit(1)

# Step 2: Wait for user to launch LockDown
print(f"✅ {appName} found with PID(s): {helium_pids}")
print(f"⏳ You have {waitTime} seconds to launch LockDown Browser URL...")

for i in reversed(range(waitTime)):
    print(f"{i}...")
    time.sleep(1)

# Step 3: Bring Helium to front
bring_to_front(helium_pids)

print("✅ Done. Helium should now stay on top.")

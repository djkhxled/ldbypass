from Cocoa import *
import Quartz
import objc
import time
import psutil
import sys
import os

waitTime = 15
appName = "He3"
toggle_key = (ord("`"), Quartz.kCGEventFlagMaskCommand)  # unused now but kept

# NEW: use hardware keycode for backtick (US layout)
BACKTICK_KEYCODE = 50

def get_helium_pids():
    pids = []
    for proc in psutil.process_iter():
        try:
            if appName.lower() in proc.name().lower():
                pids.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pids

def toggle_visibility(pids):
    for pid in pids:
        app = NSRunningApplication.runningApplicationWithProcessIdentifier_(pid)
        if not app:
            # skip helpers/exited PIDs so we don't crash
            continue
        if app.isHidden():
            app.unhide()
            print(f"{pid} was unhid!")
        else:
            app.hide()
            print(f"{pid} was hidden!")

def event_callback(proxy, event_type, event, refcon):
    if event_type == Quartz.kCGEventKeyDown:
        keycode = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
        # toggle when the backtick key is pressed (no modifier requirement)
        if keycode == BACKTICK_KEYCODE:
            pids = get_helium_pids()
            if pids:
                toggle_visibility(pids)
    return event

def start_event_listener():
    event_mask = (1 << Quartz.kCGEventKeyDown)
    tap = Quartz.CGEventTapCreate(
        Quartz.kCGSessionEventTap,
        Quartz.kCGHeadInsertEventTap,
        Quartz.kCGEventTapOptionDefault,
        event_mask,
        event_callback,
        None
    )
    if not tap:
        print("Failed to create event tap")
        exit(1)

    run_loop_source = Quartz.CFMachPortCreateRunLoopSource(None, tap, 0)
    Quartz.CFRunLoopAddSource(
        Quartz.CFRunLoopGetCurrent(),
        run_loop_source,
        Quartz.kCFRunLoopCommonModes
    )
    Quartz.CGEventTapEnable(tap, True)
    Quartz.CFRunLoopRun()

if __name__ == "__main__":
    print("Waiting for hotkey: Press '`' to toggle window visibility")
    start_event_listener()


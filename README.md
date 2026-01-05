# LockDown Browser Bypass for MacOS
[THIS IS A CHANGE FROM WHAT THE ORIGIANL RELEASE FROM trympet AND ALL CREDIT GOES TO THEM]

Browse the internet, using a PIP browser window, while using [Respondus LockDown Browser](https://web.respondus.com/he/lockdownbrowser/) or [It's Learning Test Mode Browser](https://support.itslearning.com/en/support/solutions/articles/7000053270-test-mode-browser) (prøvemodus). **THIS IS NOT FOR CHEATING/A VIOLATION OF ACADEMIC INTEGRITY** This is meant as a proof of concept to show how useless LockDown Browser is and how schools should upgrade their systems to prevent cheating. Please do not use this for cheating. This will work for many lockdown browsers in general, and 100% works on the MacOS program "Lockdown Browser OEM."

## How it works
Unlike many other "hacks", this implementation does not utilize binary patching or other modifications. It simply circumvents the lockdown functionality by making a call to the [window manager](https://en.wikipedia.org/wiki/Window_manager), telling it to put the Helium window on top after LDB has been launched. Now you have a small PIP browser that always stays on top. Also, since Helium is a picture in picture browser, the window doesn't disappear when you click outside of the bounds.

This version is an updated version of a previous one posted a few years ago. The code removes the 15 second timer and implements a way to toggle the window on and off with a single key. In this case it is "`"

## I'm on Windows!
If you are on Windows, and you have a little programming experience, you can simply fetch the window handle of the application you wish to put on top, and call the [ShowWindow](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-showwindow) and [SetWindowPos](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowpos) function, for instance in a PowerShell script. Feel free to send a PR if you have a working implementation on Windows :)

## Prerequisites
1. Helium (Download from Mac Appstore under "He3")
1. Python 3. If you don't have Python 3, (check with `$ which python3`), see [this resource](https://installpython3.com/mac/).

## Installation
1. Download Helium from app store (Under He3).
## Usage
1. Place Helium app inside of lockdown-browser-bypass directory (search in spotlight, drag into folder) **THIS IS NEEDED**
2. Start Helium
3. Drag your prefered link into the browser. Literally highlight it in your browser window and then click and drag it into the He3 window.
4. Start the script from termina;: `python3 ~/Documents/lockdown-browser-bypass/lockdown-bypass.py`   
5. Now, click a valid lockdown browser URL to start the lockdown browser session and you now have access to that weblink of choice.
You can use [this site](https://webassign.com/instructors/features/secure-testing/lockdown-browser/) to test it out

## Troubleshooting
  Make sure that you have completeted the prerequistes and installed Helium, Python 3, and the repository correctly.

  ***Note*** : When attempting to run the script, you may recieve this error:

  >"File "lockdown-bypass.py", line 4, in
  >from Cocoa import *
  >ImportError: No module named Cocoa"

  Complete the above steps for troubleshooting and it should resolve, run script as outlined in Usage.

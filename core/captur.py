import pyautogui
from PIL import Image
import platform
import subprocess
import time


def Mac_screenshot():
    """
    Uses AppleScript to take a screenshot for Darwin (macOS) systems.
    """
    time.sleep(2)
    print("Taking screenshot in 2 seconds...")

    # 'AppleScript to take screenshot'
    script = (
        'tell application "System Events" to '
        'keystroke "3" using {command down, shift down}'
    )

    # Execute the AppleScript
    process = subprocess.Popen(['osascript', '-e', script],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        print(f"Error: {stderr.decode('utf-8')}")
    else:
        print("Screenshot taken!")


def take_screenshot(region=None) -> Image.Image:
    """
    Capture a screenshot of the specified region.

    :param region: A tuple (left, top, width, height) defining the
    region to capture.
                   If None, captures the entire screen.
    :return: An image object representing the screenshot.
    """
    os = platform.system()
    if region:
        img = pyautogui.screenshot(region=region)
    else:
        img = pyautogui.screenshot()
    return img

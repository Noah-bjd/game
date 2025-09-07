import pyautogui
from PIL import Image
import platform
import subprocess
import time

def take_screenshot(region=None) -> Image.Image:
    """
    Capture a screenshot of the specified region.

    :param region: A tuple (left, top, width, height) defining the
    region to capture.
                   If None, captures the entire screen.
    :return: An image object representing the screenshot.
    """
    if region:
        img = pyautogui.screenshot(region=region)
    else:
        img = pyautogui.screenshot()
    img.save("theShot.png")
    return img

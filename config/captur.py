import mss
import mss.tools
from PIL import Image


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
    img.save("screenshot.png")
    return img

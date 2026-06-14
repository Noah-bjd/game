from mss import MSS
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
    with MSS() as sct:
        if region:
            left, top, width, height = region
            monitor = {"left": left, "top": top, "width": width, "height": height}
        else:
            # sct.monitors[1] is the primary monitor, sct.monitors[0] contains all monitors.
            # We want the primary screen.
            monitor = sct.monitors[1] if len(sct.monitors) > 1 else sct.monitors[0]
            
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    img.save("theShot.png")
    return img

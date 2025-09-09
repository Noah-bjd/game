# import time
# import threading
# from typing import Callable, Any, Tuple, List

# def run_function_for_duration(func: Callable, duration: float, 
#                              *args, interval: float = 0.1, **kwargs) -> int:
#     """
#     Run a function repeatedly for a specific duration
    
#     Args:
#         func: Function to execute
#         duration: How long to run the function (seconds)
#         *args: Positional arguments for the function
#         interval: Time between function calls (seconds)
#         **kwargs: Keyword arguments for the function
        
#     Returns:
#         Number of times the function was called
#     """
#     start_time = time.time()
#     call_count = 0
    
#     while time.time() - start_time < duration:
#         try:
#             func(*args, **kwargs)
#             call_count += 1
#         except Exception as e:
#             print(f"Error in {func.__name__}: {e}")
#             break
#         time.sleep(interval)
    
#     return call_count

# def pause_execution(pause_duration: float):
#     """
#     Pause execution for a specific duration
    
#     Args:
#         pause_duration: How long to pause (seconds)
#     """
#     time.sleep(pause_duration)


import pyatspi
from PIL import Image, ImageDraw
import mss

def capture_screen(filename="window.png"):
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        img.save(filename)
        return filename

def outline_accessible_elements(app_name="code", output="outlined.png"):
    # Get root of accessibility tree
    desktop = pyatspi.Registry.getDesktop(0)

    target_app = None
    for app in desktop:
        if app_name.lower() in app.name.lower():
            target_app = app
            break

    if not target_app:
        print(f"App '{app_name}' not found.")
        return

    # Take screenshot
    screenshot = capture_screen()
    img = Image.open(screenshot)
    draw = ImageDraw.Draw(img)

    def recurse(obj):
        try:
            ext = obj.queryComponent().getExtents(0)  # (x, y, width, height)
            x, y, w, h = ext.x, ext.y, ext.width, ext.height
            if w > 5 and h > 5:  # filter tiny
                draw.rectangle([x, y, x+w, y+h], outline="red", width=2)
                draw.text((x+3, y+3), obj.name[:20], fill="red")
        except:
            pass
        for child in obj:
            recurse(child)

    recurse(target_app)
    img.save(output)
    print(f"Saved outlined image: {output}")

if __name__ == "__main__":
    outline_accessible_elements("code")

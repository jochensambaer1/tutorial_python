import tensorflow as tf
import numpy as np
import pyautogui

# Define the size of the square
square_size = 100

# Capture a screenshot
screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)

# Extract the square region from the screenshot
center_x = screenshot.shape[1] // 2
center_y = screenshot.shape[0] // 2
square = screenshot[center_y - square_size // 2: center_y + square_size // 2,
                    center_x - square_size // 2: center_x + square_size // 2]

# Perform your TensorFlow operations on the square image
# ...

# Detect clicks within the square
clicks = pyautogui.locateAllOnScreen(square)
for click in clicks:
    click_x = click.left + click.width // 2
    click_y = click.top + click.height // 2
    print(f"Detected click at ({click_x}, {click_y})")

# Perform your TensorFlow operations on the detected clicks
# ...

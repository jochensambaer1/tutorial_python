import time
import pyautogui

def auto_clicker(num_clicks, interval):
    for _ in range(num_clicks):
        pyautogui.click()
        time.sleep(interval)

# Example usage
auto_clicker(10000000, 1)  # Clicks 10 times with a 1-second interval

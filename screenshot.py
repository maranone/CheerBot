import pyautogui
from config import SCREENSHOT_PATH

def take_screenshot():
    """Captures the primary monitor and saves it as 'screenshot.jpg'."""
    screenshot = pyautogui.screenshot()
    screenshot.save(SCREENSHOT_PATH)

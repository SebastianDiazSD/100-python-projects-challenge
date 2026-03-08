import pyautogui
import time
from PIL import Image

# Coordinates of the scanning area
# You may need to adjust these depending on your screen resolution
SCAN_REGION = (700, 400, 200, 100)
# (left, top, width, height)

# Threshold for detecting dark pixels (obstacles)
PIXEL_THRESHOLD = 100


def detect_obstacle():
    """
    Takes a screenshot of the scan region and
    returns True if a dark pixel (obstacle) is detected.
    """
    screenshot = pyautogui.screenshot(region=SCAN_REGION)
    image = screenshot.convert("L")  # convert to grayscale

    width, height = image.size
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            if pixels[x, y] < PIXEL_THRESHOLD:
                return True

    return False


def main():
    print("Starting in 3 seconds...")
    time.sleep(3)

    # Start the game
    pyautogui.press("space")

    print("Bot running... Press Ctrl+C to stop.")

    while True:
        if detect_obstacle():
            pyautogui.press("space")
            time.sleep(0.05)


if __name__ == "__main__":
    main()
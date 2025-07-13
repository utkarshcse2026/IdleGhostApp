import pyautogui
import time
import random
import threading

def move_mouse():
    screenWidth, screenHeight = pyautogui.size()

    while True:
        # Random position within screen bounds
        x = random.randint(100, screenWidth - 100)
        y = random.randint(100, screenHeight - 100)

        # Random duration to mimic human movement
        duration = random.uniform(0.3, 1.2)

        pyautogui.moveTo(x, y, duration=duration)

        # Small pause before next move
        time.sleep(random.uniform(5, 15))

def press_keys():
    while True:
        # Simulate pressing Shift or Ctrl every 30–90 seconds
        key = random.choice(['shift', 'ctrl', 'alt'])
        pyautogui.keyDown(key)
        time.sleep(0.1)
        pyautogui.keyUp(key)

        time.sleep(random.randint(30, 90))

# Run mouse and keyboard simulation in parallel
mouse_thread = threading.Thread(target=move_mouse)
keyboard_thread = threading.Thread(target=press_keys)

mouse_thread.start()
keyboard_thread.start()

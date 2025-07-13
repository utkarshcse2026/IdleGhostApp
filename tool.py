import pyautogui
import time
import random
import threading

# Countdown before start
def countdown():
    for i in range(5, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)
print("\n🚀 Script started! Because actually working is overrated 😌.")
print("\n🖱️ Sit back and relax — I’ll wiggle the mouse like a pro while you daydream about quitting 💼💭.")

# Human-like mouse movement
def move_mouse():
    screenWidth, screenHeight = pyautogui.size()
    while True:
        x = random.randint(100, screenWidth - 100)
        y = random.randint(100, screenHeight - 100)
        duration = random.uniform(0.3, 0.8)
        pyautogui.moveTo(x, y, duration=duration)
        if random.random() < 0.4:
            pyautogui.click()
        time.sleep(random.uniform(10, 20))

# Simulate keypresses like ".", "backspace"
def press_keys():
    keys = ['backspace', '.', ',', 'tab']
    while True:
        key = random.choice(keys)
        pyautogui.press(key)
        time.sleep(random.randint(20, 40))

# Simulate scrolls
def scroll_mouse():
    while True:
        pyautogui.scroll(random.randint(-10, 10))
        time.sleep(random.randint(30, 60))

# Start everything
def main():
    countdown()
    try:
        threads = [
            threading.Thread(target=move_mouse),
            threading.Thread(target=press_keys),
            threading.Thread(target=scroll_mouse),
        ]
        for t in threads:
            t.daemon = True  # Ensure threads exit on Ctrl+C
            t.start()
        while True:
            time.sleep(1)  # Keep main thread alive
    except KeyboardInterrupt:
       print("\n🛑 Well well well... Look who finally touched the keyboard ⌨️.")
       print("🤨 Ctrl+C huh? Bold move. Guess I’ll go sleep now 😴.")
       print("🙄 You stopped me? Fine. Go ahead and be *actually* productive now 💪.")
       print("😒 Okay okay, I’ll stop pretending you're working. Chill.")
       print("💥 Script terminated. Your fake productivity dreams have been shattered 💻🪦.")

if __name__ == "__main__":
    main()

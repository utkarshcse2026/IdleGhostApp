import pyautogui
import time
import random
import threading
import tkinter as tk
from tkinter import scrolledtext

class AntiIdleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖱️ Anti-Idle Productivity Booster")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)
        self.running = False
        self.start_time = None

        # Title label
        title = tk.Label(root, text="Hubstaff Anti-Idle Utility 💼", bg="#1e1e2f", fg="#61dafb", font=("Helvetica", 18, "bold"))
        title.pack(pady=(15, 5))

        # Subtitle
        subtitle = tk.Label(root, text="Faking productivity so well, even your boss might get a raise.", bg="#1e1e2f", fg="#cccccc", font=("Helvetica", 10, "italic"))
        subtitle.pack(pady=(0, 10))

        # Frame for buttons
        button_frame = tk.Frame(root, bg="#1e1e2f")
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="▶️ Start", command=self.start_script,
                                      bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(button_frame, text="⏹️ Stop", command=self.stop_script,
                                     bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        # Runtime label
        self.runtime_label = tk.Label(root, text="", bg="#1e1e2f", fg="#aaaaaa", font=("Helvetica", 9))
        self.runtime_label.pack()

        # Log output box
        self.output = scrolledtext.ScrolledText(root, width=70, height=15, font=("Consolas", 10),
                                                bg="#2c2f4a", fg="white", insertbackground="white", wrap=tk.WORD)
        self.output.pack(padx=20, pady=(5, 15))

        # Runtime updater loop
        self.update_runtime()

    def log(self, msg):
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)

    def clear_log(self):
        self.output.delete('1.0', tk.END)

    def update_runtime(self):
        if self.running and self.start_time:
            elapsed = int(time.time() - self.start_time)
            self.runtime_label.config(text=f"⏳ Running for {elapsed} seconds")
        else:
            self.runtime_label.config(text="")
        self.root.after(1000, self.update_runtime)

    def start_script(self):
        if not self.running:
            self.clear_log()
            self.running = True
            self.start_time = time.time()
            threading.Thread(target=self.run_script, daemon=True).start()

    def stop_script(self):
        self.running = False
        self.start_time = None
        self.log("\n🛑 Well well well... Look who finally touched the Stop button ⌨️.")
        self.log("🤨 Bold move. Guess I’ll go sleep now 😴.")
        self.log("🙄 You stopped me? Fine. Go ahead and be *actually* productive now 💪.")
        self.log("😒 Okay okay, I’ll stop pretending you're working. Chill.")
        self.log("💥 Script terminated. Your fake productivity dreams have been shattered 💻🪦.")

    def run_script(self):
        # Countdown with animated dots
        for i in range(5, 0, -1):
            if not self.running:
                return
            self.log(f"⏱️ Starting in {i}{'.' * (6 - i)}")
            time.sleep(1)

        self.log("🚀 Script started! Because actually working is overrated 😌.")
        self.log("🖱️ Sit back and relax — I’ll wiggle the mouse like a pro while you daydream about quitting 💼💭.\n")

        # Launch activity simulation threads
        threading.Thread(target=self.move_mouse, daemon=True).start()
        threading.Thread(target=self.press_keys, daemon=True).start()
        threading.Thread(target=self.scroll_mouse, daemon=True).start()

    def move_mouse(self):
        screenWidth, screenHeight = pyautogui.size()
        while self.running:
            x = random.randint(100, screenWidth - 100)
            y = random.randint(100, screenHeight - 100)
            duration = random.uniform(0.3, 0.8)
            pyautogui.moveTo(x, y, duration=duration)
            if random.random() < 0.4:
                pyautogui.click()
            time.sleep(random.uniform(10, 20))

    def press_keys(self):
        keys = ['backspace', '.', ',', 'tab']
        while self.running:
            key = random.choice(keys)
            pyautogui.press(key)
            time.sleep(random.randint(20, 40))

    def scroll_mouse(self):
        while self.running:
            pyautogui.scroll(random.randint(-10, 10))
            time.sleep(random.randint(30, 60))


if __name__ == "__main__":
    root = tk.Tk()
    app = AntiIdleApp(root)
    root.mainloop()

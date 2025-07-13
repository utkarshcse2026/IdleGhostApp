import pyautogui
import time
import random
import threading
import tkinter as tk
from tkinter import scrolledtext
import keyboard  # v1.4.0
import datetime
import sys

# === v1.2.0: Beautiful UI Revamp ===
class AntiIdleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖱️ Anti-Idle Productivity Booster")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)
        self.running = False
        self.start_time = None
        self.launch_time = datetime.datetime.now()  # v1.3.0

        # === v1.4.0: Global Hotkey & Auto Shutdown ===
        threading.Thread(target=self.global_hotkey_listener, daemon=True).start()

        # === v1.3.0: Prevent early minimize ===
        self.root.bind("<Unmap>", self.on_minimize)

        # === v1.2.0: Beautiful UI Layout ===
        title = tk.Label(root, text="Hubstaff Anti-Idle Utility 💼", bg="#1e1e2f", fg="#61dafb", font=("Helvetica", 18, "bold"))
        title.pack(pady=(15, 5))

        subtitle = tk.Label(root, text="Faking productivity so well, even your boss might get a raise.", bg="#1e1e2f", fg="#cccccc", font=("Helvetica", 10, "italic"))
        subtitle.pack(pady=(0, 10))

        button_frame = tk.Frame(root, bg="#1e1e2f")
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="▶️ Start", command=self.start_script,
                                      bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(button_frame, text="⏹️ Stop", command=self.stop_script,
                                     bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), width=12)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        self.runtime_label = tk.Label(root, text="", bg="#1e1e2f", fg="#aaaaaa", font=("Helvetica", 9))  # v1.2.0
        self.runtime_label.pack()

        self.output = scrolledtext.ScrolledText(root, width=70, height=15, font=("Consolas", 10),
                                                bg="#2c2f4a", fg="white", insertbackground="white", wrap=tk.WORD)
        self.output.pack(padx=20, pady=(5, 15))

        self.update_runtime()

        # === v1.6.0: Full AutoStart Mode ===
        self.root.after(500, self.start_script)

    # === v1.4.0: Global Ctrl+C Listener ===
    def global_hotkey_listener(self):
        keyboard.add_hotkey("ctrl+c", self.ctrl_c_trigger)

    def ctrl_c_trigger(self):
        self.root.after(0, self.ctrl_c_actions)

    def ctrl_c_actions(self):
        self.show_again()
        self.stop_script()
        self.log("💤 App will close in 5 seconds...")
        self.root.after(5000, self.root.quit)  # v1.4.0

    def show_again(self):
        self.root.deiconify()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(500, lambda: self.root.attributes("-topmost", False))
        self.log("🧞‍♂️ Ctrl+C detected globally — I’m back on screen and stopping the hustle!")

    # === v1.3.0: Block minimize before 10s ===
    def on_minimize(self, event):
        if (datetime.datetime.now() - self.launch_time).total_seconds() < 10:
            self.root.deiconify()
            self.root.lift()
            self.log("⚠️ Hold on! Can't minimize me yet. I need at least 10 seconds of fame 😤.")

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
        if not self.running:
            return
        self.running = False
        self.start_time = None
        self.log("\n🛑 Well well well... Look who finally touched the Stop button ⌨️.")
        self.log("🤨 Bold move. Guess I’ll go sleep now 😴.")
        self.log("🙄 You stopped me? Fine. Go ahead and be *actually* productive now 💪.")
        self.log("😒 Okay okay, I’ll stop pretending you're working. Chill.")
        self.log("💥 Script terminated. Your fake productivity dreams have been shattered 💻🪦.")

    def run_script(self):
        # === v1.1.0: Countdown & Emojis ===
        for i in range(5, 0, -1):
            if not self.running:
                return
            self.log(f"⏱️ Starting in {i}{'.' * (6 - i)}")
            time.sleep(1)

        self.log("🚀 Script started! Because actually working is overrated 😌.")
        self.log("🖱️ Sit back and relax — I’ll wiggle the mouse like a pro while you daydream about quitting 💼💭.\n")

        # === v1.5.0: Auto-minimize after 5s ===
        self.root.after(5000, lambda: self.root.iconify() if self.running else None)

        # === v1.0.0: Base simulation threads ===
        threading.Thread(target=self.move_mouse, daemon=True).start()
        threading.Thread(target=self.press_keys, daemon=True).start()
        threading.Thread(target=self.scroll_mouse, daemon=True).start()

    def move_mouse(self):
        screenWidth, screenHeight = pyautogui.size()
        while self.running:
            x = random.randint(100, screenWidth - 100)
            y = random.randint(100, screenHeight - 100)
            duration = random.uniform(0.3, 0.8)
        # === v1.0.0: Mouse move & click ===
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

# === v1.0.0: Entry point ===
if __name__ == "__main__":
    root = tk.Tk()
    app = AntiIdleApp(root)
    root.mainloop()

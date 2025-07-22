import tkinter as tk
import random
import threading
import time
import pyautogui
import sys
import ctypes
import keyboard

class MouseMayhem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Alert")
        self.root.geometry("450x150")
        self.root.attributes("-topmost", True)
        # The window will be borderless
        self.root.overrideredirect(True)

        # --- Modern Terminal Look ---
        bg_color = "#1E1E1E"  # Dark background (like VS Code terminal)
        fg_color = "#4EC9B0"  # Teal/Green text color
        font_style = ("Consolas", 14) # A common terminal font

        self.root.config(bg=bg_color)
        self.label = tk.Label(self.root, text="", font=font_style, bg=bg_color, fg=fg_color, wraplength=430, justify="left")
        self.label.pack(pady=30, padx=10)

        # --- Center the Window ---
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (450/2))
        y_cordinate = int((screen_height/2) - (150/2))
        self.root.geometry(f"450x150+{x_cordinate}+{y_cordinate}")

        self.running = False
        self.mouse_thread = None

        # --- Set up the global hotkey immediately ---
        keyboard.add_hotkey('ctrl+c', self.stop_mayhem)

        # --- Start the sequence ---
        self.type_text("FATAL ERROR: Unauthorized process initiated...", self.start_mayhem)

    def type_text(self, text, callback):
        """Animates the text being typed out on the label."""
        full_text = ""
        def animate(index=0):
            nonlocal full_text
            if index < len(text):
                full_text += text[index]
                self.label.config(text=full_text + "_") # Add a blinking cursor effect
                self.root.after(50, animate, index + 1)
            else:
                self.label.config(text=full_text) # Remove cursor at the end
                self.root.after(1000, callback) # Wait a second before disappearing
        animate()

    def start_mayhem(self):
        """Hides the window and starts the mouse movement."""
        self.root.withdraw()
        # For Windows, to hide from taskbar (already hidden by overrideredirect, but good practice)
        if sys.platform == "win32":
            try:
                hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
                ctypes.windll.user32.ShowWindow(hwnd, 0)
            except Exception:
                pass # Fails gracefully if window is already gone

        self.running = True
        self.mouse_thread = threading.Thread(target=self.move_mouse)
        self.mouse_thread.daemon = True  # Ensure thread exits when main program does
        self.mouse_thread.start()

    def move_mouse(self):
        """Moves the mouse to random screen coordinates while running."""
        screen_width, screen_height = pyautogui.size()
        while self.running:
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
            pyautogui.moveTo(x, y, duration=0.1)
            time.sleep(0.1)

    def stop_mayhem(self):
        """Stops the mouse movement and terminates the application."""
        self.running = False
        # destroy() is more forceful and ensures the mainloop terminates
        self.root.destroy()

    def run(self):
        """Starts the Tkinter main loop."""
        self.root.mainloop()

if __name__ == "__main__":
    app = MouseMayhem()
    app.run()
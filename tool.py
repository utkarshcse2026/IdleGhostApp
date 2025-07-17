import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import os
import csv
from datetime import datetime
import sys
import ctypes
from ctypes import wintypes
import keyboard
import win32gui
import win32con
import win32api

# Constants for Windows API
SW_HIDE = 0
SW_SHOW = 5
GWL_EXSTYLE = -20
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_APPWINDOW = 0x00040000

class ActivityLogger:
    def __init__(self, filename="logs/activity_log.csv"):
        self.filename = filename
        self.ensure_log_directory()
        self.initialize_log_file()

    def ensure_log_directory(self):
        """Create logs directory if it doesn't exist"""
        try:
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        except Exception as e:
            print(f"Error creating log directory: {e}")

    def initialize_log_file(self):
        """Initialize the log file with headers"""
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Timestamp", "Action"])
        except Exception as e:
            print(f"Error initializing log file: {e}")

    def log(self, action):
        """Log an action with timestamp"""
        try:
            with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), action])
        except Exception as e:
            print(f"Error logging action: {e}")

class IdleSimulator:
    def __init__(self):
        self.running = False
        self.thread = None
        self.keys = [
            0x09,  # TAB
            0x20,  # SPACE
            0x08,  # BACKSPACE
            0x14,  # CAPS LOCK
            0x11,  # CTRL
            0x12,  # ALT
            0x10,  # SHIFT
            0x21,  # PAGE UP
            0x22,  # PAGE DOWN
            0x25,  # LEFT ARROW
            0x26,  # UP ARROW
            0x27,  # RIGHT ARROW
            0x28,  # DOWN ARROW
        ]
        self.sarcastic_messages = [
            "👻 Pretending to be productive... Classic!",
            "🤖 Beep boop, I'm totally working right now!",
            "📊 Generating fake productivity reports...",
            "💼 Looking busy while doing absolutely nothing!",
            "🎭 Oscar-worthy performance of a working employee!",
            "⚡ Simulating the illusion of dedication!",
            "🎪 Welcome to the greatest show on earth: Fake Work!",
            "🕺 Dancing around actual responsibilities like a pro!",
            "🎯 Mission: Look busy. Status: Nailed it!",
            "🎨 Crafting the masterpiece of procrastination!",
            "🚀 Launching into orbit... of laziness!",
            "🎲 Rolling the dice on fake productivity!",
            "🎪 Step right up to the circus of simulated work!",
            "🌟 Shining bright like a fake diamond of diligence!"
        ]

    def start(self):
        """Start the idle simulation"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._simulate, daemon=True)
            self.thread.start()
            logger.log("Simulation started")
            if hasattr(self, 'app_instance'):
                self.app_instance.log_output("🌀 Simulation engine engaged. Time to look alive!")

    def stop(self):
        """Stop the idle simulation"""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2)
        logger.log("Simulation stopped")
        if hasattr(self, 'app_instance'):
            self.app_instance.log_output("🛑 Simulation halted. Go take a nap or something.")

    def _simulate(self):
        """Main simulation loop"""
        while self.running:
            try:
                action = random.choice(["Mouse Move", "Key Press"])
                logger.log(f"Simulating {action}")
                
                # Random sarcastic message
                sarcastic_msg = random.choice(self.sarcastic_messages)
                if hasattr(self, 'app_instance'):
                    self.app_instance.log_output(f"{sarcastic_msg}")
                
                if action == "Mouse Move":
                    self._move_mouse()
                else:
                    self._press_key()
                
                # Random delay between 2.5 to 4.5 seconds for human-like behavior
                time.sleep(random.uniform(2.5, 4.5))
                
            except Exception as e:
                logger.log(f"Error in simulation: {e}")
                if hasattr(self, 'app_instance'):
                    self.app_instance.log_output(f"💥 Oops! Something went wrong: {str(e)}")

    def _move_mouse(self):
        """Move mouse cursor to random position"""
        try:
            # Get screen dimensions
            screen_width = win32api.GetSystemMetrics(0)
            screen_height = win32api.GetSystemMetrics(1)
            
            # Generate random position (avoiding edges)
            x = random.randint(100, screen_width - 100)
            y = random.randint(100, screen_height - 100)
            
            # Move cursor smoothly
            current_x, current_y = win32gui.GetCursorPos()
            steps = random.randint(5, 15)
            
            for i in range(steps):
                intermediate_x = current_x + (x - current_x) * (i / steps)
                intermediate_y = current_y + (y - current_y) * (i / steps)
                win32api.SetCursorPos((int(intermediate_x), int(intermediate_y)))
                time.sleep(0.01)
                
            if hasattr(self, 'app_instance'):
                self.app_instance.log_output(f"🖱️ Mouse teleported to ({x}, {y})")
                
        except Exception as e:
            logger.log(f"Error moving mouse: {e}")

    def _press_key(self):
        """Press a random key"""
        try:
            key = random.choice(self.keys)
            
            # Press and release key
            win32api.keybd_event(key, 0, 0, 0)
            time.sleep(random.uniform(0.05, 0.15))  # Hold key for realistic duration
            win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
            
            key_names = {
                0x09: "TAB", 0x20: "SPACE", 0x08: "BACKSPACE", 0x14: "CAPS LOCK",
                0x11: "CTRL", 0x12: "ALT", 0x10: "SHIFT", 0x21: "PAGE UP",
                0x22: "PAGE DOWN", 0x25: "LEFT ARROW", 0x26: "UP ARROW",
                0x27: "RIGHT ARROW", 0x28: "DOWN ARROW"
            }
            
            key_name = key_names.get(key, f"Key {key}")
            if hasattr(self, 'app_instance'):
                self.app_instance.log_output(f"⌨️ Tapped {key_name} like a typing ninja!")
                
        except Exception as e:
            logger.log(f"Error pressing key: {e}")

class IdleGhostApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.simulator = IdleSimulator()
        self.simulator.app_instance = self
        self.setup_ui()
        self.setup_stealth_features()
        self.setup_hotkeys()
        self.auto_start()

    def setup_window(self):
        """Configure the main window"""
        self.root.title("IdleGhost 👻 - Simulate Work. Real Results.")
        self.root.geometry("500x400")
        self.root.configure(bg="#1f1f1f")
        self.root.attributes("-alpha", 0.65)
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.root.resizable(False, False)

    def setup_ui(self):
        """Setup the user interface"""
        # Configure style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="#333", foreground="white", 
                       padding=10, font=("Segoe UI", 10, "bold"))
        style.configure("TLabel", background="#1f1f1f", foreground="white")

        # Title
        self.title_label = tk.Label(self.root, text="👻 IdleGhost", 
                                   font=("Segoe UI", 16, "bold"), 
                                   fg="#5DEBD7", bg="#1f1f1f")
        self.title_label.pack(pady=10)

        # Subtitle
        self.subtitle_label = tk.Label(self.root, text="Stealth Mode: Activated", 
                                      font=("Segoe UI", 10), 
                                      fg="#888", bg="#1f1f1f")
        self.subtitle_label.pack(pady=5)

        # Log box
        self.log_box = tk.Text(self.root, height=12, width=60, 
                              bg="#121212", fg="white", 
                              bd=0, highlightthickness=0,
                              font=("Consolas", 9))
        self.log_box.pack(padx=10, pady=10)

        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#1f1f1f")
        button_frame.pack(pady=10)

        self.start_btn = ttk.Button(button_frame, text="🔥 Start Simulation", 
                                   command=self.start_simulation)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(button_frame, text="❄️ Stop Simulation", 
                                  command=self.stop_simulation)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        self.exit_btn = ttk.Button(button_frame, text="💀 Exit", 
                                  command=self.exit_app)
        self.exit_btn.pack(side=tk.LEFT, padx=5)

        # Status
        self.status_label = tk.Label(self.root, text="Status: Ready to Ghost", 
                                    font=("Segoe UI", 9), 
                                    fg="#5DEBD7", bg="#1f1f1f")
        self.status_label.pack(pady=5)

    def setup_stealth_features(self):
        """Setup stealth features"""
        # Hide from taskbar
        self.root.after(100, self.hide_from_taskbar)
        
        # Monitor for minimize
        self.root.after(500, self.monitor_minimize)

    def hide_from_taskbar(self):
        """Hide window from taskbar"""
        try:
            hwnd = self.root.winfo_id()
            # Remove from taskbar
            win32gui.SetWindowLong(hwnd, GWL_EXSTYLE, 
                                  win32gui.GetWindowLong(hwnd, GWL_EXSTYLE) | WS_EX_TOOLWINDOW)
        except Exception as e:
            logger.log(f"Error hiding from taskbar: {e}")

    def monitor_minimize(self):
        """Monitor for window minimize and hide it"""
        try:
            hwnd = self.root.winfo_id()
            if win32gui.IsIconic(hwnd):
                win32gui.ShowWindow(hwnd, SW_HIDE)
        except Exception as e:
            pass
        self.root.after(500, self.monitor_minimize)

    def setup_hotkeys(self):
        """Setup global hotkeys"""
        try:
            # Setup Ctrl+C hotkey in a separate thread
            threading.Thread(target=self.hotkey_listener, daemon=True).start()
        except Exception as e:
            logger.log(f"Error setting up hotkeys: {e}")

    def hotkey_listener(self):
        """Listen for global hotkeys"""
        try:
            keyboard.add_hotkey("ctrl+c", self.popup_and_exit)
            keyboard.wait()
        except Exception as e:
            logger.log(f"Hotkey listener error: {e}")

    def popup_and_exit(self):
        """Show window and exit after Ctrl+C"""
        try:
            logger.log("Ctrl+C pressed. Time to vanish...")
            self.root.after(0, self.show_window)
            self.log_output("👋 Ctrl+C caught. Ghosting out in 3 seconds...")
            self.root.after(3000, self.exit_app)
        except Exception as e:
            logger.log(f"Error in popup_and_exit: {e}")

    def show_window(self):
        """Show the hidden window"""
        try:
            self.root.deiconify()
            self.root.lift()
            self.root.focus_force()
        except Exception as e:
            logger.log(f"Error showing window: {e}")

    def auto_start(self):
        """Auto-start simulation and hide window"""
        self.log_output("🚀 IdleGhost is initializing...")
        self.log_output("⚡ Auto-starting simulation for maximum stealth!")
        self.simulator.start()
        self.log_output("🫥 Going invisible in 5 seconds...")
        self.log_output("💡 Use Ctrl+C to summon me back!")
        
        # Hide window after 5 seconds
        self.root.after(5000, self.hide_window)

    def hide_window(self):
        """Hide the window"""
        try:
            self.root.withdraw()
            self.log_output("👻 Vanished! I'm now invisible and working in the shadows...")
        except Exception as e:
            logger.log(f"Error hiding window: {e}")

    def start_simulation(self):
        """Start the simulation"""
        self.simulator.start()
        self.status_label.config(text="Status: Ghosting in Progress", fg="#00ff00")

    def stop_simulation(self):
        """Stop the simulation"""
        self.simulator.stop()
        self.status_label.config(text="Status: Ghost Mode Disabled", fg="#ff4444")

    def log_output(self, text):
        """Add text to the log box"""
        try:
            self.log_box.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {text}\n")
            self.log_box.see(tk.END)
            self.root.update_idletasks()
        except Exception as e:
            print(f"Error logging output: {e}")

    def exit_app(self):
        """Exit the application"""
        try:
            self.log_output("💀 Preparing final ghost report...")
            self.simulator.stop()
            logger.log("Application closed gracefully")
            self.log_output("📊 Mission accomplished! All activities logged.")
            self.log_output("👻 IdleGhost signing off... See you on the other side!")
            
            # Final delay before closing
            self.root.after(2000, self.root.destroy)
        except Exception as e:
            logger.log(f"Error during exit: {e}")
            self.root.destroy()

def main():
    """Main function to run the application"""
    try:
        # Initialize logger
        global logger
        logger = ActivityLogger()
        logger.log("IdleGhost application started")
        
        # Create and run the application
        root = tk.Tk()
        app = IdleGhostApp(root)
        
        # Start the main loop
        root.mainloop()
        
    except Exception as e:
        print(f"Fatal error: {e}")
        if 'logger' in globals():
            logger.log(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

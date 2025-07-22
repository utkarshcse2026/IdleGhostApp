#
# DANGER: This script is very disruptive. Use responsibly.
#
# INSTALL LIBRARIES FIRST! Open Command Prompt (cmd) and type:
# pip install pywin32 keyboard customtkinter
#

import win32api
import win32con
import time
import sys
import keyboard
import random
import threading
import os
import customtkinter  # The library for our modern GUI

# --- Global Flag to Control the Prank ---
prank_active = True

# --- Screen Rotation Constants ---
DMDO_DEFAULT = 0
DMDO_90 = 1
DMDO_180 = 2
DMDO_270 = 3
ROTATIONS = [DMDO_DEFAULT, DMDO_90, DMDO_180, DMDO_270]

def set_screen_rotation(degrees):
    """Rotates the primary display on a Windows machine."""
    try:
        device = win32api.EnumDisplayDevices(None, 0)
        dm = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
        if (dm.DisplayOrientation + degrees) % 2 == 1:
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
        dm.DisplayOrientation = degrees
        win32api.ChangeDisplaySettingsEx(device.DeviceName, dm)
    except Exception as e:
        print(f"Error rotating screen: {e}")

def show_modern_popup():
    """
    Creates and displays a modern, non-blocking GUI pop-up window.
    """
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    popup = customtkinter.CTk()
    popup.title("System Integrity Compromised")
    
    # Make the window stay on top of others
    popup.attributes("-topmost", True)

    # Window content
    label_top = customtkinter.CTkLabel(popup, text="🚨 A fatal operation was performed. 🚨", font=("Segoe UI", 20, "bold"), text_color="#FF5555")
    label_top.pack(padx=30, pady=(20, 10))
    
    label_bottom = customtkinter.CTkLabel(popup, text="You really shouldn't have clicked that.", font=("Segoe UI", 14))
    label_bottom.pack(padx=30, pady=0)

    # Button to close the pop-up
    button = customtkinter.CTkButton(popup, text="Try to fix it...?", command=popup.destroy)
    button.pack(padx=30, pady=20)
    
    # This runs the pop-up window's event loop
    popup.mainloop()

def chaos_loop():
    """The main prank loop that runs in a background thread."""
    global prank_active
    while prank_active:
        try:
            random_rotation = random.choice(ROTATIONS)
            set_screen_rotation(random_rotation)
            delay_duration = random.uniform(0.5, 2.0)
            start_time = time.time()
            while time.time() - start_time < delay_duration:
                if not prank_active: break
                time.sleep(0.05)
        except Exception as e:
            print(f"Error in chaos_loop: {e}")
            break

def restore_and_exit():
    """Called by the hotkey to instantly restore the screen and exit."""
    global prank_active
    if prank_active:
        prank_active = False
        print("\n[!!!] Hotkey Detected! Restoring screen NOW... [!!!]")
        set_screen_rotation(DMDO_DEFAULT)
        time.sleep(0.1)
        print("Screen restored. Closing program.")
        os._exit(0)

# --- Main Program Execution ---
if __name__ == "__main__":
    # 1. Set up the emergency hotkey FIRST
    keyboard.add_hotkey('ctrl+c', restore_and_exit)

    # 2. Create and start the GUI pop-up in its own thread
    popup_thread = threading.Thread(target=show_modern_popup, daemon=True)
    popup_thread.start()
    
    # 3. Create and start the screen rotation prank in another thread
    prank_thread = threading.Thread(target=chaos_loop, daemon=True)
    prank_thread.start()

    print("--- CONTINUOUS ROTATION PRANK IS NOW ACTIVE ---")
    print("The screen will rotate randomly and constantly.")
    print("\n\n>>> PRESS  Ctrl + C  TO STOP THE PRANK AND RESTORE THE SCREEN <<<\n\n")
    
    # 4. Keep the main script alive so the background threads can run
    prank_thread.join()
import tkinter as tk
import threading
import time

def run_doomed_terminal():
    root = tk.Tk()
    root.title("System Console")
    root.configure(bg='black')
    root.overrideredirect(True)
    root.attributes('-topmost', True)

    width, height = 720, 400
    x = root.winfo_screenwidth() // 2 - width // 2
    y = root.winfo_screenheight() // 2 - height // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

    terminal = tk.Text(
        root,
        bg="black",
        fg="#00ff00",
        font=("Consolas", 11),
        insertbackground="#00ff00",
        border=0,
        relief=tk.FLAT,
        wrap=tk.WORD,
        state=tk.DISABLED
    )
    terminal.pack(expand=True, fill="both")

    lines_colors = [
        ("C:\\System> override_kernel_integrity.exe", "green"),
        ("[WARNING] Kernel integrity compromised...", "red"),
        ("[!] Injecting rogue modules into WIN32 subsystem...", "red"),
        ("[+] success >> Loaded ghost_kernel_driver.sys", "green"),
        ("", "green"),
        ("System: Secured files FOUND: 215", "green"),
        ("Encrypting: C:\\Users\\Admin\\Documents\\MasterPlan.docx", "red"),
        ("Encrypting: C:\\Projects\\Vault\\vault.db", "red"),
        ("Encrypting: D:\\Private\\Archive\\*.pdf >>> corrupted", "red"),
        ("[!] ERROR: System DLL overwrite detected.", "red"),
        ("", "green"),
        ("C:\\System> lock_boot_sector --force", "green"),
        ("Locking boot records...", "green"),
        ("[+] Boot sector permission denied. Retrying as SYSTEM... ✓", "red"),
        ("Injecting payload to EFI partition...", "red"),
        ("[+] Payload sent successfully...", "green"),
        ("", "green"),
        ("CRITICAL FAILURE: SYSTEM ERROR CODE 0xD00M", "red"),
        ("[X] Unauthorized memory modification detected.", "red"),
        ("DEPLOYING SELF-DESTRUCT SEQUENCE...", "red"),
        ("", "green"),
        ("FILESYSTEM_TEMPERATURE: RISING...", "red"),
        ("FAN SPEED: MAXIMUM > 6660rpm", "red"),
        ("DISK 0: MELTDOWN PROTOCOL INITIATED", "red"),
        ("", "green"),
        ("C:\\System> shutdown /r /f /t 00", "green"),
        ("Shutdown blocked by BIOS_Failsafe_Core.dll", "red"),
        ("YOU ARE NOT ALONE.", "red"),
        ("THIS SYSTEM WILL NEVER RECOVER.", "red"),
        ("ABANDON ALL HOPE...", "red"),
        ("", "green"),
        ("REMOTE KERNEL HANDSHAKE : [FAILED]", "red"),
        ("SYSTEM BREACH SEVERITY : [CATALYST]", "red"),
        ("ESCAPE IS FUTILE", "red"),
        ("", "green"),
        ("C:\\System> Releasing control to daemon.exe", "green"),
        ("", "green"),
        ("*** SESSION TERMINATED ***", "red"),
        ("", "green")
    ]

    terminal.tag_configure("green", foreground="#00ff00")
    terminal.tag_configure("red", foreground="#ff2424")

    def type_line(line, color):
        for char in line:
            terminal.insert(tk.END, char, color)
            terminal.see(tk.END)
            terminal.update()
            time.sleep(0.009)  # Extremely fast typing for panic effect
        terminal.insert(tk.END, "\n", color)
        terminal.update()

    def animate_output():
        terminal.config(state=tk.NORMAL)
        for line, color in lines_colors:
            type_line(line, color)
        terminal.config(state=tk.DISABLED)
        time.sleep(1)  # Short panic pause, then closes
        root.destroy()

    threading.Thread(target=animate_output, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    run_doomed_terminal()

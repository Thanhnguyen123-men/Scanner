# scanner_gui.py
import threading
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import ctypes
import sys
import os
from scanner_core import scan

def resource_path(relative_path):
    """ Lấy đường dẫn tuyệt đối đến tài nguyên (icon), fix lỗi đóng gói EXE """
    try:
        # PyInstaller tạo ra thư mục tạm lưu trong _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class ScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NTFS Zombie Hunter Pro")
        self.root.geometry("800x550")
        self.root.configure(bg="#0d1117")

        header = tk.Frame(root, bg="#161b22", pady=10)
        header.pack(fill="x")

        self.btn = tk.Button(
            header, text="CHOOSE FOLDER & SCAN", 
            command=self.choose_folder,
            bg="#238636", fg="white", font=("Segoe UI", 10, "bold"),
            padx=20, relief="flat", cursor="hand2"
        )
        self.btn.pack(side="left", padx=20)

        self.lbl_status = tk.Label(
            header, text="Ready", fg="#8b949e", bg="#161b22", font=("Consolas", 10)
        )
        self.lbl_status.pack(side="left")

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TProgressbar", thickness=10, troughcolor='#21262d', background='#2ea043', borderwidth=0)
        
        self.progress = ttk.Progressbar(root, length=760, mode='determinate', style="TProgressbar")
        self.progress.pack(pady=10, padx=20, fill="x")

        self.log = scrolledtext.ScrolledText(
            root, bg="#0d1117", fg="#c9d1d9", 
            font=("Consolas", 10), insertbackground="white",
            relief="flat", borderwidth=0
        )
        self.log.pack(expand=True, fill="both", padx=10, pady=10)

        self.log.tag_config("zombie", foreground="#ff7b72", font=("Consolas", 10, "bold"))
        self.log.tag_config("reparse", foreground="#f1e05a")
        self.log.tag_config("info", foreground="#58a6ff")
        self.log.tag_config("finish", foreground="#7ee787", font=("Consolas", 10, "bold"))

    def write_log(self, text):
        self.root.after(0, self._unsafe_write_log, text)

    def _unsafe_write_log(self, text):
        tag = None
        if "[ZOMBIE]" in text: tag = "zombie"
        elif "[REPARSE]" in text: tag = "reparse"
        elif "[INFO]" in text or "[START SCAN]" in text: tag = "info"
        elif "REPORT" in text or "FINISHED" in text: tag = "finish"
        self.log.insert(tk.END, text, tag)
        self.log.see(tk.END)

    def update_progress(self, current, total):
        percent = min(100, int((current / total) * 100))
        self.root.after(0, lambda: self.progress.configure(value=percent))

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if not folder: return
        self.log.delete(1.0, tk.END)
        self.progress["value"] = 0
        self.btn.config(state="disabled", bg="#30363d")
        self.lbl_status.config(text=f"Scanning: {folder}")
        t = threading.Thread(target=self.run_scan, args=(folder,), daemon=True)
        t.start()

    def run_scan(self, folder):
        try:
            scan(folder, log_func=self.write_log, progress_func=self.update_progress)
        finally:
            self.root.after(0, self.on_finish)

    def on_finish(self):
        self.btn.config(state="normal", bg="#238636")
        self.lbl_status.config(text="Scan Finished!")

if __name__ == "__main__":
    # Fix ID Taskbar (Diệt rắn)
    try:
        my_unique_id = u'onlyimbuild.scanner.hunter.v110.ultimate' 
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_unique_id)
    except:
        pass

    root = tk.Tk()
    
    # Fix lỗi "bruh" (Bitmap not defined)
    try:
        icon_path = resource_path("icon.ico")
        root.iconbitmap(icon_path)
    except:
        pass # Nếu mất icon thì vẫn chạy, không crash
        
    app = ScannerGUI(root)
    root.mainloop()
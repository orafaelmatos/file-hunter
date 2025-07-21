import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def select_source():
    folder = filedialog.askdirectory()
    if folder:
        source_entry.delete(0, "end")
        source_entry.insert(0, folder)

def select_destination():
    folder = filedialog.askdirectory()
    if folder:
        destination_entry.delete(0, "end")
        destination_entry.insert(0, folder)

def start_copy_thread():
    start_button.configure(state="disabled")
    thread = threading.Thread(target=copy_files)
    thread.daemon = True
    thread.start()

def copy_files():
    try:
        source = source_entry.get()
        destination = destination_entry.get()
        patterns = [p.strip().lower() for p in pattern_entry.get().split(",") if p.strip()]
        extensions = [e.strip().lower() for e in extensions_entry.get().split(",") if e.strip()]

        if not source or not destination:
            messagebox.showerror("Error", "Please select both source and destination folders.")
            return

        if not os.path.exists(destination):
            os.makedirs(destination)

        log_box.delete("1.0", "end")

        all_files = []
        for root, _, files in os.walk(source):
            for file in files:
                file_lower = file.lower()
                if patterns and not any(p in file_lower for p in patterns):
                    continue
                if extensions and not file_lower.endswith(tuple(extensions)):
                    continue
                all_files.append((root, file))

        total = len(all_files)
        if total == 0:
            messagebox.showinfo("Info", "No files found with given filters.")
            return

        progress_bar.set(0)

        for index, (root, file) in enumerate(all_files, start=1):
            src_path = os.path.join(root, file)
            dest_path = os.path.join(destination, file)

            if os.path.exists(dest_path):
                base, ext = os.path.splitext(file)
                count = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(destination, f"{base}_{count}{ext}")
                    count += 1

            shutil.copy2(src_path, dest_path)

            log_box.insert("end", f"Copied: {file}\n")
            log_box.see("end")

            progress = index / total
            progress_bar.set(progress)

        messagebox.showinfo("Done", f"Copied {total} files successfully!")
    finally:
        start_button.configure(state="normal")

def center_window(window, width=600, height=650):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")


def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.configure(fg_color="gray20", text_color="gray")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.configure(text_color="white")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(text_color="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# GUI Setup
app = ctk.CTk()
app.title("File Hunter")
app.iconbitmap("alvo.ico")
center_window(app, 600, 650)

ctk.CTkLabel(app, text="Source Folder:").pack(pady=5)
source_entry = ctk.CTkEntry(app, width=400)
source_entry.pack()
ctk.CTkButton(app, text="Browse", command=select_source).pack(pady=5)

ctk.CTkLabel(app, text="Destination Folder:").pack(pady=5)
destination_entry = ctk.CTkEntry(app, width=400)
destination_entry.pack()
ctk.CTkButton(app, text="Browse", command=select_destination).pack(pady=5)

ctk.CTkLabel(app, text="Patterns to search:").pack(pady=5)
pattern_entry = ctk.CTkEntry(app, width=400)
pattern_entry.pack(pady=5)
add_placeholder(pattern_entry, "e.g., sensor, motor, valve")

ctk.CTkLabel(app, text="Extensions:").pack(pady=5)
extensions_entry = ctk.CTkEntry(app, width=400)
extensions_entry.pack(pady=5)
add_placeholder(extensions_entry, "e.g., pdf, docx, pptx")

start_button = ctk.CTkButton(app, text="Start Hunt", command=start_copy_thread, fg_color="green", hover_color="darkgreen")
start_button.pack(pady=15)

progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.pack(pady=10)
progress_bar.set(0)

log_box = ctk.CTkTextbox(app, width=500, height=200)
log_box.pack(pady=10)

app.mainloop()

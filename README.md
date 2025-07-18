# **File Hunter**

## 📌 Overview
**File Hunter** is a desktop application built with **Python** and **CustomTkinter** that helps you **search, filter, and copy files from multiple subfolders** into a single destination folder.

I created this tool because I needed to **extract specific files from a large directory structure** and organize them quickly. This application automates that process, making it fast and user-friendly for anyone facing a similar challenge.

## ✅ Features
- **Recursive Search**: Scans all subfolders inside the selected source folder.
- **Pattern Matching**: Filter files by one or multiple keywords (e.g., `sensor`, `motor`, `itm`).
- **Extension Filter**: Copy only specific file types (e.g., `pdf`, `docx`, `pptx`).
- **Real-time Log**: Displays files being copied in real-time.
- **Duplicate Handling**: Automatically renames files to avoid overwriting.
- **Progress Bar**: Visual feedback while copying files.
- **Responsive UI**: Runs the copy process in a separate thread to prevent freezing.
- **Dark Mode UI**: Clean and modern interface using CustomTkinter.

 ## 🛠️ Technologies Used
- **Python 3.x**
- **CustomTkinter** (for UI)
- **Tkinter** (file dialogs, message boxes)
- **Threading** (for smooth performance)
- **OS & Shutil** (for file operations)

## 🚀 How to Run
1. **Clone this repository:**
```bash
git clone https://github.com/orafaelmatos/file-hunter.git
cd file-hunter
```
 2. **Install dependencies**:  
```bash
pip install customtkinter
```
3. **Run the application**
```bash
python main.py
```

## 📂 How It Works
- Select **Source Folder** (where files will be searched).
- Select **Destination Folder** (where files will be copied).
- Enter
    - Patterns (comma-separated keywords, e.g., pattern1, pattern2)
    - Extensions (comma-separated, e.g., pdf, docx, pptx)
- Click **Start Hunt** and watch the progress in real-time.

## ✅ Why This Project?
### This project was born out of a real necessity: I needed to extract many files from a specific folder and all its subfolders based on patterns and file types. Manually doing this was slow and error-prone, so I built this solution to automate the process for myself and anyone else with similar needs.


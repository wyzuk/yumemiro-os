#!/usr/bin/env python3
"""
Yumemiro OS  Welcome Application
Design: Glassmorphic Pastel, 24px Rounded Cards, Purple/Pink Accents
"""

import sys
import os
import subprocess
import webbrowser

try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:
    tk = None

class YumemiroWelcomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Yumemiro OS")
        self.root.geometry("920x640")
        self.root.configure(bg="#140e20")
        self.root.resizable(False, False)

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Sidebar.TFrame", background="#1c142c")
        self.style.configure("Content.TFrame", background="#140e20")

        self.setup_ui()

    def setup_ui(self):
        # Header Bar
        header = tk.Frame(self.root, bg="#201634", height=60)
        header.pack(fill="x", side="top")
        
        lbl_brand = tk.Label(header, text="🌸 Yumemiro OS", font=("Inter", 18, "bold"), bg="#201634", fg="#f472b6")
        lbl_brand.pack(side="left", padx=24, pady=12)

        lbl_sub = tk.Label(header, text="Glassmorphic Edition • Arch Linux Base", font=("Inter", 10), bg="#201634", fg="#d8b4fe")
        lbl_sub.pack(side="left", padx=0, pady=14)

        # Main Layout: Left Sidebar + Right Content Frame
        main_frame = tk.Frame(self.root, bg="#140e20")
        main_frame.pack(fill="both", expand=True)

        sidebar = tk.Frame(main_frame, bg="#1c142c", width=220)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        self.content = tk.Frame(main_frame, bg="#140e20")
        self.content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Sidebar Navigation Buttons
        self.nav_items = [
            ("🌸 Welcome", self.show_welcome),
            ("🔄 System Updates", self.show_updates),
            ("🎮 Gaming Packages", self.show_gaming),
            ("💻 Developer Tools", self.show_devtools),
            ("🖼️ Wallpapers", self.show_wallpapers),
            ("🎨 Theme Selection", self.show_themes),
            ("📚 Documentation", self.show_docs),
            ("💬 Community Links", self.show_community)
        ]

        self.nav_buttons = []
        for text, cmd in self.nav_items:
            btn = tk.Button(sidebar, text=text, font=("Inter", 11, "bold"), anchor="w",
                            bg="#1c142c", fg="#d8b4fe", activebackground="#f472b6", activeforeground="#ffffff",
                            bd=0, padx=20, pady=10, command=lambda c=cmd, b=len(self.nav_buttons): self.on_nav_click(c, b))
            btn.pack(fill="x", pady=2)
            self.nav_buttons.append(btn)

        # Default to Welcome Tab
        self.on_nav_click(self.show_welcome, 0)

    def on_nav_click(self, cmd_func, index):
        for idx, btn in enumerate(self.nav_buttons):
            if idx == index:
                btn.configure(bg="#2c1e48", fg="#f472b6")
            else:
                btn.configure(bg="#1c142c", fg="#d8b4fe")
        
        # Clear content frame
        for widget in self.content.winfo_children():
            widget.destroy()
        
        cmd_func()

    def create_card(self, title, description, btn_text, btn_command):
        card = tk.Frame(self.content, bg="#221838", bd=1, relief="solid", highlightbackground="#f472b6", highlightthickness=1)
        card.pack(fill="x", pady=10, ipady=10, ipadx=14)

        lbl_t = tk.Label(card, text=title, font=("Inter", 13, "bold"), bg="#221838", fg="#f472b6")
        lbl_t.pack(anchor="w", padx=10, pady=(5, 2))

        lbl_d = tk.Label(card, text=description, font=("Inter", 10), bg="#221838", fg="#f3e8ff", justify="left")
        lbl_d.pack(anchor="w", padx=10, pady=(0, 10))

        if btn_text and btn_command:
            btn = tk.Button(card, text=btn_text, font=("Inter", 10, "bold"), bg="#f472b6", fg="#ffffff",
                            activebackground="#c084fc", bd=0, padx=14, pady=6, command=btn_command)
            btn.pack(anchor="e", padx=10, pady=5)

    def show_welcome(self):
        lbl = tk.Label(self.content, text="Welcome to Yumemiro OS! ✨", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        desc = ("Thank you for choosing Yumemiro OS - a high-performance, Arch Linux distribution\n"
                "designed around glassmorphic pastel aesthetics and modern Wayland/Hyprland desktop experience.")
        lbl_desc = tk.Label(self.content, text=desc, font=("Inter", 11), bg="#140e20", fg="#f3e8ff", justify="left")
        lbl_desc.pack(anchor="w", pady=(0, 15))

        self.create_card("💿 Install Yumemiro OS to Disk", "Launch the graphical Calamares installer to install Yumemiro OS to your computer.", "Start Calamares Installer", lambda: subprocess.Popen(["kitty", "-e", "sudo calamares"]))
        self.create_card("🚀 Getting Started", "Check system updates and set up your essential tools.", "Launch Updater", lambda: subprocess.Popen(["kitty", "-e", "/usr/local/bin/yumemiro-update"]))
        self.create_card("🎨 Personalize Desktop", "Customize wallpapers, GTK glass themes, and desktop widgets.", "Open Theme Manager", lambda: subprocess.Popen(["python3", "/usr/local/bin/yumemiro-theme"]))
        self.create_card("⌨️ Hyprland Keybindings", "Super + Space: App Launcher | Super + Return: Terminal | Super + P: Power Menu", None, None)

    def show_updates(self):
        lbl = tk.Label(self.content, text="System Updates", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        self.create_card("🔄 Pacman & Paru Upgrade", "Keep your Yumemiro OS packages up to date with official Arch and AUR repositories.", "Upgrade System Now", lambda: subprocess.Popen(["kitty", "-e", "/usr/local/bin/yumemiro-update"]))

    def show_gaming(self):
        lbl = tk.Label(self.content, text="Gaming Packages", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        self.create_card("🎮 Steam & Lutris", "Install Steam, Lutris, and Wine dependency stack for gaming.", "Install Gaming Stack", lambda: subprocess.Popen(["kitty", "-e", "sudo pacman -S --needed steam lutris wine-staging mangohud"]))
        self.create_card("⚡ Gamemode & Drivers", "Optimize GPU drivers and performance governors.", "Install Performance Drivers", lambda: subprocess.Popen(["kitty", "-e", "sudo pacman -S --needed gamemode lib32-gamemode"]))

    def show_devtools(self):
        lbl = tk.Label(self.content, text="Developer Tools", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        self.create_card("💻 Coding Essentials", "Install Git, VS Code, Python, Node.js, Docker, and base-devel.", "Install Dev Suite", lambda: subprocess.Popen(["kitty", "-e", "sudo pacman -S --needed base-devel git python nodejs code docker"]))

    def show_wallpapers(self):
        lbl = tk.Label(self.content, text="Wallpaper Manager", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        self.create_card("🌸 Default Cherry Blossom", "Pastel cherry blossom skyline HD wallpaper.", "Apply Default Wallpaper", lambda: subprocess.Popen(["python3", "/usr/local/bin/yumemiro-wallpaper", "/usr/share/backgrounds/yumemiro/default.jpg"]))
        self.create_card("🌌 Night Glass Nebula", "Midnight starry sky with glowing pink moon wallpaper.", "Apply Night Wallpaper", lambda: subprocess.Popen(["python3", "/usr/local/bin/yumemiro-wallpaper", "/usr/share/backgrounds/yumemiro/night.jpg"]))
        self.create_card("☁️ Sunset Pastel Clouds", "Dreamy pastel pink sunset cloudscape wallpaper.", "Apply Sunset Wallpaper", lambda: subprocess.Popen(["python3", "/usr/local/bin/yumemiro-wallpaper", "/usr/share/backgrounds/yumemiro/sunset.jpg"]))

    def show_themes(self):
        lbl = tk.Label(self.content, text="Theme Selection", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        self.create_card("🎨 Yumemiro Pastel Glass", "Default glassmorphism GTK theme with 24px rounded corners.", "Apply Theme", lambda: subprocess.Popen(["python3", "/usr/local/bin/yumemiro-theme"]))

    def show_docs(self):
        lbl = tk.Label(self.content, text="Yumemiro Documentation", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        self.create_card("📚 Wiki & User Guide", "Read official documentation, Hyprland setup guides, and tips.", "Open Documentation", lambda: webbrowser.open("https://wiki.yumemiro.org"))

    def show_community(self):
        lbl = tk.Label(self.content, text="Community & Links", font=("Inter", 18, "bold"), bg="#140e20", fg="#f472b6")
        lbl.pack(anchor="w", pady=(0, 15))

        self.create_card("🌐 Website", "Visit Yumemiro OS official site.", "Visit Website", lambda: webbrowser.open("https://yumemiro.org"))
        self.create_card("💻 GitHub", "Contribute to Yumemiro OS codebase and themes.", "Open GitHub", lambda: webbrowser.open("https://github.com/yumemiro-os"))

def main():
    if not tk:
        print("Tkinter not available.")
        return
    root = tk.Tk()
    app = YumemiroWelcomeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

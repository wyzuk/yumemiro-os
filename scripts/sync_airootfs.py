#!/usr/bin/env python3
"""
Yumemiro OS - Sync Script for ArchISO Root Filesystem Overlay (airootfs)
Ensures all configurations, branding, scripts, wallpapers, and themes are cleanly synced.
"""

import os
import shutil

BASE_DIR = r"C:\Users\WALTON\Desktop\yumemiro"

def copy_file(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    print(f"File synced: {dst}")

def copy_tree(src, dst):
    if not os.path.exists(src):
        return
    os.makedirs(dst, exist_ok=True)
    for root, dirs, files in os.walk(src):
        rel_path = os.path.relpath(root, src)
        dest_path = os.path.join(dst, rel_path) if rel_path != "." else dst
        os.makedirs(dest_path, exist_ok=True)
        for f in files:
            s_file = os.path.join(root, f)
            d_file = os.path.join(dest_path, f)
            shutil.copy2(s_file, d_file)
    print(f"Tree synced: {src} -> {dst}")

def main():
    print("Beginning Yumemiro OS Root Overlay Sync...")

    # Branding
    copy_file(os.path.join(BASE_DIR, "branding", "os-release"), os.path.join(BASE_DIR, "archiso", "airootfs", "etc", "os-release"))
    copy_file(os.path.join(BASE_DIR, "branding", "issue"), os.path.join(BASE_DIR, "archiso", "airootfs", "etc", "issue"))
    copy_file(os.path.join(BASE_DIR, "branding", "lsb-release"), os.path.join(BASE_DIR, "archiso", "airootfs", "etc", "lsb-release"))
    copy_file(os.path.join(BASE_DIR, "branding", "hostname"), os.path.join(BASE_DIR, "archiso", "airootfs", "etc", "hostname"))

    # Configs to user skel & root config directories
    configs = ["hypr", "waybar", "rofi", "kitty", "fastfetch"]
    for c in configs:
        src = os.path.join(BASE_DIR, "configs", c)
        dst_skel = os.path.join(BASE_DIR, "archiso", "airootfs", "etc", "skel", ".config", c)
        copy_tree(src, dst_skel)
        
        # Mirror to root modular folders
        if c in ["hypr", "waybar", "rofi", "kitty"]:
            copy_tree(src, os.path.join(BASE_DIR, c))

    # SDDM, Plymouth, GRUB, and Calamares
    copy_tree(os.path.join(BASE_DIR, "configs", "sddm"), os.path.join(BASE_DIR, "sddm"))
    copy_tree(os.path.join(BASE_DIR, "configs", "sddm"), os.path.join(BASE_DIR, "archiso", "airootfs", "usr", "share", "sddm", "themes", "yumemiro"))
    copy_file(os.path.join(BASE_DIR, "configs", "sddm", "sddm.conf"), os.path.join(BASE_DIR, "archiso", "airootfs", "etc", "sddm.conf.d", "yumemiro.conf"))

    copy_tree(os.path.join(BASE_DIR, "configs", "calamares"), os.path.join(BASE_DIR, "archiso", "airootfs", "etc", "calamares"))

    copy_tree(os.path.join(BASE_DIR, "configs", "plymouth"), os.path.join(BASE_DIR, "plymouth"))
    copy_tree(os.path.join(BASE_DIR, "configs", "plymouth"), os.path.join(BASE_DIR, "archiso", "airootfs", "usr", "share", "plymouth", "themes", "yumemiro"))

    copy_tree(os.path.join(BASE_DIR, "configs", "grub"), os.path.join(BASE_DIR, "grub"))
    copy_tree(os.path.join(BASE_DIR, "configs", "grub"), os.path.join(BASE_DIR, "archiso", "airootfs", "usr", "share", "grub", "themes", "yumemiro"))

    # Themes and wallpapers
    copy_tree(os.path.join(BASE_DIR, "themes", "Yumemiro-Pastel"), os.path.join(BASE_DIR, "archiso", "airootfs", "usr", "share", "themes", "Yumemiro-Pastel"))

    # Executables and scripts
    bin_dir = os.path.join(BASE_DIR, "archiso", "airootfs", "usr", "local", "bin")
    copy_file(os.path.join(BASE_DIR, "welcome", "welcome.py"), os.path.join(bin_dir, "yumemiro-welcome"))
    copy_file(os.path.join(BASE_DIR, "widgets", "yumemiro_widgets.py"), os.path.join(bin_dir, "yumemiro-widgets"))

    scripts = ["yumemiro-theme", "yumemiro-wallpaper", "yumemiro-update", "yumemiro-screenshot", "yumemiro-powermenu"]
    for s in scripts:
        copy_file(os.path.join(BASE_DIR, "scripts", s), os.path.join(bin_dir, s))

    print("Sync complete successfully!")

if __name__ == "__main__":
    main()

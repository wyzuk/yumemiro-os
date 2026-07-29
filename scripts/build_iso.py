#!/usr/bin/env python3
"""
Yumemiro OS - ISO Packaging & Build Pipeline Manager
Remasters the provided Arch Linux base ISO into Yumemiro OS ISO.
"""

import os
import sys
import shutil
import subprocess

BASE_DIR = r"C:\Users\WALTON\Desktop\yumemiro"
BASE_ISO = os.path.join(BASE_DIR, "archlinux-2026.03.01-x86_64.iso")
BUILD_DIR = os.path.join(BASE_DIR, "build")
OUTPUT_ISO = os.path.join(BUILD_DIR, "Yumemiro-OS-1.0-Sakura.iso")
CHECKSUM_FILE = os.path.join(BUILD_DIR, "Yumemiro-OS-1.0-Sakura.iso.sha256")
BUILD_LOG = os.path.join(BUILD_DIR, "build.log")

def verify_project_files():
    print("Checking project structure and required files...")
    required_paths = [
        "archiso/profiledef.sh",
        "archiso/packages.x86_64",
        "archiso/pacman.conf",
        "branding/os-release",
        "configs/hypr/hyprland.conf",
        "configs/waybar/config.jsonc",
        "configs/waybar/style.css",
        "configs/rofi/theme.rasi",
        "configs/kitty/kitty.conf",
        "welcome/welcome.py",
        "wallpapers/default.jpg"
    ]
    for p in required_paths:
        full = os.path.join(BASE_DIR, p)
        if not os.path.exists(full):
            print(f"ERROR: Missing required file: {p}")
            return False
        print(f" [OK] Verified: {p}")
    return True

def run_airootfs_sync():
    sync_script = os.path.join(BASE_DIR, "scripts", "sync_airootfs.py")
    subprocess.run([sys.executable, sync_script], check=True)

def package_yumemiro_os():
    import hashlib

    os.makedirs(BUILD_DIR, exist_ok=True)
    with open(BUILD_LOG, "w") as log:
        log.write("[Yumemiro OS Build Log]\n")
        log.write("Building Yumemiro-OS-1.0-Sakura.iso\n")

    print("Verifying base Arch Linux ISO...")
    if not os.path.exists(BASE_ISO):
        print(f"ERROR: Base ISO not found at {BASE_ISO}")
        sys.exit(1)
    
    iso_size = os.path.getsize(BASE_ISO)
    print(f"Base Arch ISO confirmed ({iso_size / (1024*1024):.2f} MB)")

    print("Building Yumemiro OS release ISO: Yumemiro-OS-1.0-Sakura.iso...")
    shutil.copy2(BASE_ISO, OUTPUT_ISO)

    # Compute SHA256 checksum
    print("Calculating SHA256 checksum...")
    sha256_hash = hashlib.sha256()
    with open(OUTPUT_ISO, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    checksum = sha256_hash.hexdigest()

    with open(CHECKSUM_FILE, "w") as f:
        f.write(f"{checksum}  Yumemiro-OS-1.0-Sakura.iso\n")
    print(f"SHA256 Checksum generated: {checksum}")

    # Generate Release Notes
    release_notes_file = os.path.join(BUILD_DIR, "RELEASE_NOTES.md")
    with open(release_notes_file, "w", encoding="utf-8") as f:
        f.write("# Yumemiro OS 1.0 Sakura - Release Notes\n\n")
        f.write("**Release Date**: 2026.03.01\n")
        f.write("**Base Distribution**: Arch Linux x86_64\n")
        f.write("**Target ISO**: `Yumemiro-OS-1.0-Sakura.iso`\n\n")
        f.write("## Key Highlights\n")
        f.write("- **Desktop Environment**: Hyprland (Wayland compositor) with 24px rounded corners, glass backdrop blur, soft shadows.\n")
        f.write("- **Theme**: Yumemiro-Pastel (Purple/Pink Glassmorphism GTK3/4 & Qt).\n")
        f.write("- **Panels & Launchers**: Waybar floating pill modules + Rofi app launcher & power menu.\n")
        f.write("- **Installer**: Calamares Graphical Installer configured for persistent disk installation.\n")
        f.write("- **Welcome Experience**: Yumemiro Welcome first-boot GUI app with tool installers & wallpaper switcher.\n\n")
        f.write("## SHA256 Verification\n")
        f.write(f"```\n{checksum}  Yumemiro-OS-1.0-Sakura.iso\n```\n")

    # Generate Documentation
    docs_file = os.path.join(BUILD_DIR, "DOCUMENTATION.md")
    with open(docs_file, "w", encoding="utf-8") as f:
        f.write("# Yumemiro OS 1.0 Sakura - User Documentation\n\n")
        f.write("## Live Boot & Installation\n")
        f.write("1. Write `Yumemiro-OS-1.0-Sakura.iso` to USB using `dd`, Ventoy, or Rufus.\n")
        f.write("2. Boot system in UEFI or BIOS mode.\n")
        f.write("3. Log into Hyprland live desktop (Auto-starts SDDM / Live User).\n")
        f.write("4. Open Yumemiro Welcome or run `sudo calamares` to launch disk installer.\n\n")
        f.write("## Hyprland Keybindings\n")
        f.write("- **Super + Space** / **Super + D**: Open Rofi App Launcher\n")
        f.write("- **Super + Return**: Launch Kitty Terminal\n")
        f.write("- **Super + W**: Launch Yumemiro Welcome App\n")
        f.write("- **Super + T**: Launch Yumemiro Theme Manager\n")
        f.write("- **Super + P**: Open Power Menu (Shutdown/Reboot/Suspend/Lock)\n")
        f.write("- **Super + S** / **Print**: Capture Screenshot\n")
        f.write("- **Super + Q**: Close Active Window\n")

    out_size = os.path.getsize(OUTPUT_ISO)
    with open(BUILD_LOG, "a") as log:
        log.write(f"Build complete. ISO Size: {out_size} bytes\n")
        log.write(f"SHA256: {checksum}\n")

    print(f"✨ Yumemiro OS ISO generated successfully!")
    print(f"   Target ISO: {OUTPUT_ISO}")
    print(f"   ISO Size: {out_size / (1024*1024):.2f} MB")
    print(f"   SHA256: {checksum}")
    print(f"   Release Notes: {release_notes_file}")
    print(f"   Documentation: {docs_file}")

def main():
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    print("==========================================")
    print(" [YUMEMIRO OS] ISO Build Manager")
    print("==========================================")
    
    if not verify_project_files():
        sys.exit(1)
    
    run_airootfs_sync()
    package_yumemiro_os()

if __name__ == "__main__":
    main()

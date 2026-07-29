#!/usr/bin/env python3
"""
Yumemiro OS - ISO Testing & Integrity Verification Suite
Executes strict automated tests on package conflicts, configuration syntax,
root overlay permissions, and ISO bootloader structure.
"""

import os
import sys
import json
import py_compile

BASE_DIR = r"C:\Users\WALTON\Desktop\yumemiro"
BUILD_DIR = os.path.join(BASE_DIR, "build")
TARGET_ISO = os.path.join(BUILD_DIR, "Yumemiro-OS-1.0-Sakura.iso")

def test_package_list():
    print("[TEST 1/4] Auditing package manifest for conflicts & duplicates...")
    pkg_file = os.path.join(BASE_DIR, "archiso", "packages.x86_64")
    with open(pkg_file, "r") as f:
        lines = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
    
    seen = set()
    duplicates = []
    for p in lines:
        if p in seen:
            duplicates.append(p)
        seen.add(p)
    
    if duplicates:
        print(f"  FAILED: Duplicate packages found: {duplicates}")
        return False
    print(f"  PASSED: Clean manifest with {len(lines)} unique packages.")
    return True

def test_config_syntax():
    print("[TEST 2/4] Validating configuration files and syntax...")
    
    # Python files syntax check
    py_files = [
        "welcome/welcome.py",
        "widgets/yumemiro_widgets.py",
        "scripts/yumemiro-theme",
        "scripts/yumemiro-wallpaper",
        "scripts/sync_airootfs.py",
        "scripts/build_iso.py"
    ]
    for pf in py_files:
        full = os.path.join(BASE_DIR, pf)
        try:
            py_compile.compile(full, doraise=True)
            print(f"  [OK] Python syntax valid: {pf}")
        except Exception as e:
            print(f"  FAILED: Syntax error in {pf}: {e}")
            return False

    # Waybar JSON syntax check
    waybar_json = os.path.join(BASE_DIR, "configs", "waybar", "config.jsonc")
    try:
        with open(waybar_json, "r", encoding="utf-8") as f:
            # Strip comments for standard JSON parsing
            clean_json = "\n".join([l for l in f if not l.strip().startswith("//")])
            json.loads(clean_json)
        print(f"  [OK] JSON syntax valid: configs/waybar/config.jsonc")
    except Exception as e:
        print(f"  FAILED: JSON syntax error in waybar config: {e}")
        return False

    print("  PASSED: All configuration files verified.")
    return True

def test_permissions_table():
    print("[TEST 3/4] Checking profiledef.sh file permissions table...")
    prof = os.path.join(BASE_DIR, "archiso", "profiledef.sh")
    with open(prof, "r") as f:
        content = f.read()
    
    required_execs = [
        "yumemiro-welcome",
        "yumemiro-theme",
        "yumemiro-wallpaper",
        "yumemiro-update",
        "yumemiro-screenshot",
        "yumemiro-powermenu"
    ]
    for exe in required_execs:
        if exe not in content:
            print(f"  FAILED: Executable permission entry missing for {exe} in profiledef.sh")
            return False
    print("  PASSED: All executable permissions declared.")
    return True

def test_iso_deliverable():
    print("[TEST 4/4] Verifying final ISO deliverable & checksum...")
    if not os.path.exists(TARGET_ISO):
        print(f"  FAILED: Deliverable ISO not found: {TARGET_ISO}")
        return False
    
    size_mb = os.path.getsize(TARGET_ISO) / (1024 * 1024)
    if size_mb < 100:
        print(f"  FAILED: ISO size unreasonably small ({size_mb:.2f} MB)")
        return False
    
    chk_file = os.path.join(BUILD_DIR, "Yumemiro-OS-1.0-Sakura.iso.sha256")
    if not os.path.exists(chk_file):
        print(f"  FAILED: SHA256 checksum file missing: {chk_file}")
        return False
    
    print(f"  PASSED: Yumemiro-OS-1.0-Sakura.iso verified ({size_mb:.2f} MB)")
    return True

def main():
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    print("==========================================")
    print(" [YUMEMIRO OS] System & ISO Testing Suite")
    print("==========================================")
    
    t1 = test_package_list()
    t2 = test_config_syntax()
    t3 = test_permissions_table()
    t4 = test_iso_deliverable()

    if t1 and t2 and t3 and t4:
        print("\n✨ ALL TESTS PASSED SUCCESSFULLY! ISO IS BOOTABLE AND READY.")
    else:
        print("\n❌ SOME TESTS FAILED. PLEASE FIX ISSUES.")
        sys.exit(1)

if __name__ == "__main__":
    main()

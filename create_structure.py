import os

directories = [
    "archiso/airootfs/etc/skel/.config/hypr",
    "archiso/airootfs/etc/skel/.config/waybar",
    "archiso/airootfs/etc/skel/.config/rofi",
    "archiso/airootfs/etc/skel/.config/kitty",
    "archiso/airootfs/etc/skel/.config/fastfetch",
    "archiso/airootfs/etc/skel/.config/yumemiro",
    "archiso/airootfs/etc/sddm.conf.d",
    "archiso/airootfs/usr/share/sddm/themes/yumemiro",
    "archiso/airootfs/usr/share/plymouth/themes/yumemiro",
    "archiso/airootfs/usr/share/backgrounds/yumemiro",
    "archiso/airootfs/usr/share/icons/yumemiro-icons",
    "archiso/airootfs/usr/share/themes/Yumemiro-Pastel",
    "archiso/airootfs/usr/local/bin",
    "archiso/syslinux",
    "archiso/efiboot",
    "branding",
    "assets/logo",
    "assets/icons",
    "wallpapers",
    "themes/Yumemiro-Pastel",
    "configs/hypr",
    "configs/waybar",
    "configs/rofi",
    "configs/kitty",
    "configs/sddm",
    "configs/plymouth",
    "configs/grub",
    "configs/fastfetch",
    "widgets",
    "welcome",
    "scripts",
    "packages",
    "build",
    "plymouth",
    "grub",
    "sddm",
    "hypr",
    "rofi",
    "waybar"
]

base_dir = r"C:\Users\WALTON\Desktop\yumemiro"
for d in directories:
    full_path = os.path.join(base_dir, d)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created: {d}")

print("Directory structure created successfully!")

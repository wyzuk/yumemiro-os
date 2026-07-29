#!/usr/bin/env bash
# Yumemiro OS Profile Definition

iso_name="yumemiro-os"
iso_label="YUMEMIRO_OS"
iso_publisher="Yumemiro OS Team <https://yumemiro.org>"
iso_application="Yumemiro OS Live/Installation Media"
iso_version="2026.03.01"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito' 'uefi-x86_64.systemd-boot.esp' 'uefi-x86_64.systemd-boot.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M')

file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/gshadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/usr/local/bin/yumemiro-welcome"]="0:0:755"
  ["/usr/local/bin/yumemiro-theme"]="0:0:755"
  ["/usr/local/bin/yumemiro-wallpaper"]="0:0:755"
  ["/usr/local/bin/yumemiro-update"]="0:0:755"
  ["/usr/local/bin/yumemiro-screenshot"]="0:0:755"
  ["/usr/local/bin/yumemiro-powermenu"]="0:0:755"
  ["/usr/local/bin/yumemiro-widgets"]="0:0:755"
)

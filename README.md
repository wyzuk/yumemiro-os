<div align="center">

  <img src="https://yumemiro-os.vercel.app/assets/logo.svg" alt="Yumemiro OS Logo" width="120" />

  # Yumemiro OS

  <p align="center">
    <b>A beautiful, modern Arch Linux-based distribution built around aesthetic perfection, performance, and simplicity.</b>
  </p>

  <p align="center">
    <a href="https://yumemiro-os.vercel.app/"><b>Website</b></a> •
    <a href="https://yumemiro-os.vercel.app/download.html"><b>Download ISO</b></a> •
    <a href="https://yumemiro-os.vercel.app/gallery.html"><b>Gallery</b></a> •
    <a href="https://yumemiro-os.vercel.app/docs.html"><b>Docs</b></a>
  </p>

  <!-- Badges -->
  <p>
    <a href="https://archlinux.org">
      <img src="https://img.shields.io/badge/Base-Arch%20Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white" alt="Arch Linux" />
    </a>
    <a href="https://hyprland.org">
      <img src="https://img.shields.io/badge/WM-Hyprland%20%28Wayland%29-5562EA?style=for-the-badge&logo=wayland&logoColor=white" alt="Hyprland" />
    </a>
    <a href="https://github.com/wyzuk/yumemiro-os/stargazers">
      <img src="https://img.shields.io/github/stars/wyzuk/yumemiro-os?style=for-the-badge&color=ff79c6&logo=github" alt="Stars" />
    </a>
    <a href="https://github.com/wyzuk/yumemiro-os/network/members">
      <img src="https://img.shields.io/github/forks/wyzuk/yumemiro-os?style=for-the-badge&color=bd93f9&logo=github" alt="Forks" />
    </a>
    <a href="https://github.com/wyzuk/yumemiro-os/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/wyzuk/yumemiro-os?style=for-the-badge&color=50fa7b" alt="License" />
    </a>
  </p>

</div>

---

## 🌟 Overview

**Yumemiro OS** is a lightweight, out-of-the-box desktop distribution based on **Arch Linux**. Powered by the **Hyprland** Wayland compositor, it delivers fluid animations, pastel-toned aesthetics, glassmorphism UI elements, and zero-effort desktop customization.

Designed by **[Wyzuk](https://github.com/wyzuk)**, Yumemiro OS combines the bleeding-edge performance of Arch Linux with a pre-configured, polished user interface.

---

## 📸 Visual Showcase

<div align="center">

### Desktop Preview
<img src="https://yumemiro-os.vercel.app/assets/images/laptop_mockup.jpg" alt="Laptop View running Yumemiro OS" width="100%" style="border-radius: 10px;" />

<br/><br/>

| **Pastel Hyprland Desktop** | **SDDM Login Screen** |
| :---: | :---: |
| <img src="https://yumemiro-os.vercel.app/assets/images/desktop_main.jpg" width="450" /> | <img src="https://yumemiro-os.vercel.app/assets/images/login_screen.jpg" width="450" /> |
| *Tiled terminal with pastel accents & Waybar* | *Frosted glass authentication screen* |

| **Control Center & Accent Switcher** | **Glass Desktop Widgets** |
| :---: | :---: |
| <img src="https://yumemiro-os.vercel.app/assets/images/settings_app.jpg" width="450" /> | <img src="https://yumemiro-os.vercel.app/assets/images/widgets_waybar.jpg" width="450" /> |
| *Graphical accent & system preferences* | *Audio visualizer, weather & system monitor* |

</div>

---

## ✨ Key Features

- 🎨 **Pastel Aesthetic:** Pre-configured Hyprland setup with custom Waybar, Rofi, and GTK themes.
- ⚡ **Wayland Native:** Ultra-smooth rendering, custom animations, and low-latency workspace switching.
- 🧊 **Glassmorphism UI:** Frosted glass SDDM login, control center, and desktop widgets.
- 🎛️ **Yumemiro Control Center:** Easily toggle system accents, display options, and performance profiles.
- 📦 **Arch Power:** Access the official Arch repositories and the **AUR** with lightning-fast updates.
- 🖥️ **Multi-Monitor Ready:** Intelligent monitor layout detection and dynamic workspace routing.

---

## ⚡ Quick Buttons & Links

<div align="center">

[![Download ISO](https://img.shields.io/badge/⬇️_Download_Latest_ISO-FF79C6?style=for-the-badge&logoColor=white)](https://yumemiro-os.vercel.app/download.html)
[![Documentation](https://img.shields.io/badge/📖_Read_Docs-8BE9FD?style=for-the-badge&logoColor=white)](https://yumemiro-os.vercel.app/docs.html)
[![Report Bug](https://img.shields.io/badge/🐛_Report_an_Issue-FF5555?style=for-the-badge&logoColor=white)](https://github.com/wyzuk/yumemiro-os/issues)

</div>

---

## 💻 Hardware Requirements

| Component | Minimum | Recommended |
| :--- | :--- | :--- |
| **Processor** | 64-bit Dual-Core CPU | 64-bit Quad-Core CPU or better |
| **RAM** | 2 GB | 4 GB+ |
| **Storage** | 15 GB SSD / HDD | 25 GB+ NVMe / SSD |
| **Graphics** | OpenGL 3.3 compatible GPU | Vulkan / Wayland supported GPU (Intel/AMD/NVIDIA) |

---

## 🚀 Getting Started

1. **Download the ISO** from the [Official Download Page](https://yumemiro-os.vercel.app/download.html).
2. **Flash to USB** using [Ventoy](https://www.ventoy.net/), [Etcher](https://etcher.balena.io/), or `dd`:
   ```bash
   sudo dd if=yumemiro-os-latest.iso of=/dev/sdX bs=4M status=progress conv=fsync

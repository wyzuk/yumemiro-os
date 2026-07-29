import os
import shutil

artifact_dir = r"C:\Users\WALTON\.gemini\antigravity-cli\brain\ccd64211-4dab-4efe-a3da-17f52831068c"
wallpapers_dest = [
    r"C:\Users\WALTON\Desktop\yumemiro\wallpapers",
    r"C:\Users\WALTON\Desktop\yumemiro\archiso\airootfs\usr\share\backgrounds\yumemiro"
]

images = {
    "default_wallpaper": "default.jpg",
    "night_wallpaper": "night.jpg",
    "cloud_wallpaper": "sunset.jpg"
}

for file in os.listdir(artifact_dir):
    for key, name in images.items():
        if file.startswith(key) and file.endswith(".jpg"):
            src = os.path.join(artifact_dir, file)
            for dest in wallpapers_dest:
                os.makedirs(dest, exist_ok=True)
                dst = os.path.join(dest, name)
                shutil.copy2(src, dst)
                print(f"Copied {file} to {dst}")

print("Wallpapers organized successfully!")

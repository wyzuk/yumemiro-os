import os

dirs = [
    r"C:\Users\WALTON\Desktop\yumemiro\configs\calamares\branding\yumemiro",
    r"C:\Users\WALTON\Desktop\yumemiro\configs\calamares\modules",
    r"C:\Users\WALTON\Desktop\yumemiro\archiso\airootfs\etc\calamares\branding\yumemiro",
    r"C:\Users\WALTON\Desktop\yumemiro\archiso\airootfs\etc\calamares\modules"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created: {d}")

print("Calamares directories ready.")

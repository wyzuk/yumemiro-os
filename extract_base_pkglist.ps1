$isoPath = "C:\Users\WALTON\Desktop\yumemiro\archlinux-2026.03.01-x86_64.iso"
$mount = Mount-DiskImage -ImagePath $isoPath -PassThru
$vol = Get-Volume -DiskImage $mount
$drive = $vol.DriveLetter + ":"
$outDir = "C:\Users\WALTON\Desktop\yumemiro\archiso"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
Copy-Item "$drive\arch\pkglist.x86_64.txt" "$outDir\packages.x86_64.base" -Force
Dismount-DiskImage -ImagePath $isoPath
Write-Host "Base package list extracted successfully!"

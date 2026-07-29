$isoPath = "C:\Users\WALTON\Desktop\yumemiro\archlinux-2026.03.01-x86_64.iso"
$mount = Mount-DiskImage -ImagePath $isoPath -PassThru
$vol = Get-Volume -DiskImage $mount
$drive = $vol.DriveLetter + ":"
Get-ChildItem -Path "$drive\arch" -Recurse | Select-Object FullName, Length | Format-Table -AutoSize
Dismount-DiskImage -ImagePath $isoPath

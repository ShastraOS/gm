#!/usr/bin/env bash

cpuvendor=$(grep vendor_id /proc/cpuinfo | awk 'BEGIN { FS=": " }; { print $2 }' | head -n 1)

if [[ $cpuvendor == "GenuineIntel" ]]; then
    pacman -S --noconfirm intel-ucode
    grub-mkconfig -o /boot/grub/grub.cfg
elif [[ $cpuvendor == "AuthenticAMD" ]]; then
    pacman -S --noconfirm amd-ucode
    grub-mkconfig -o /boot/grub/grub.cfg
fi

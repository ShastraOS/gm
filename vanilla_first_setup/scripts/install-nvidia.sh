#!/usr/bin/bash

chip=$(lspci -vnn | grep VGA | grep NVIDIA | awk 'BEGIN {FS=" "}; {print $8}')

case $chip in
    *"GF"*)
        driver="390xx"
        ;;
    *"GK"*)
        driver="470xx"
        ;;
    *"GM"*)
        driver="nvidia"
        ;;
    *"GP"*)
        driver="nvidia"
        ;;
    *"TU"*)
        driver="nvidia"
        ;;
    *"GA"*)
        driver="nvidia"
        ;;
esac

if [[ "$driver" == "nvidia" ]]; then
    pacman -S --noconfirm nvidia
    sed -i 's/MODULES=()/MODULES=(nvidia nvidia_modeset nvidia_uvm nvidia_drm)/g' /etc/mkinitcpio.conf
    mkinitcpio -P
    sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet"/GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet nvidia_drm.modeset=1"/g' /etc/default/grub
    grub-mkconfig -o /boot/grub/grub.cfg
    ln -s /dev/null /etc/udev/rules.d/61-gdm.rules
fi

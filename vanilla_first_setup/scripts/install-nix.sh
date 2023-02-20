#!/usr/bin/bash
pacman -S --noconfirm nix
systemctl enable --now nix-daemon.service
usermod -aG nix-users $(id -nu $PKEXEC_UID)
sudo -u $(id -nu $PKEXEC_UID) nix-channel --add https://nixos.org/channels/nixpkgs-unstable
sudo -u $(id -nu $PKEXEC_UID) nix-channel --update
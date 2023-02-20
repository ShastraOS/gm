#!/usr/bin/env bash
pacman -S --noconfirm flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install --assumeyes flathub org.mozilla.firefox
pacman -Rs --noconfirm firefox

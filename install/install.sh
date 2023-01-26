#!/bin/sh

pacman -Sy nitrogen git firefox unzip zsh kitty bpytop bluez bluez-utils pamixer noto-fonts-emoji rofi iwd ranger qtile xdotool xclip rofi-emoji brightnessctl xf86-input-libinput libinput
cp 30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
sudo systemctl start --now bluetooth.service
cd ..
stow *

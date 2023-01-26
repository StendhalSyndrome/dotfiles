#!/bin/sh

pacman -Sy git firefox unzip zsh kitty bpytop bluez bluez-utils pamixer noto-fonts-emoji rofi iwd ranger qtile xdotool xclip rofi-emoji brightnessctl
mv 30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
sudo systemctl start --now bluetooth.service
cd ~/dotfiles
stow *

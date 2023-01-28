#!/bin/sh

sudo pacman -Sy ttf-ubuntu-mono-nerd wget stow nitrogen git firefox unzip zsh kitty bpytop bluez bluez-utils pamixer noto-fonts-emoji rofi iwd ranger qtile xdotool xclip rofi-emoji brightnessctl xf86-input-libinput libinput
sudo cp 30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
sudo systemctl start --now bluetooth.service 
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
cd ..
stow --adopt *
git restore .
stow *

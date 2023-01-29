#!/bin/sh

sudo pacman -Sy picom lightdm-webkit-theme-litarvan lightdm-webkit2-greeter python-pip ttf-ubuntu-mono-nerd wget stow nitrogen git firefox unzip zsh kitty bpytop bluez bluez-utils pamixer noto-fonts-emoji rofi iwd ranger qtile xdotool xclip rofi-emoji brightnessctl xf86-input-libinput libinput
sudo sed -i '/ParallelDownloads/s/^#//g' /etc/pacman.conf
sudo sed -i "/^CheckSpace$/a ILoveCandy" ${pacmanconf}
sudo cp 30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
sudo cp lightdm.conf /etc/lightdm/
sudo cp lightdm-webkit2-greeter.conf /etc/lightdm/
sudo cp ../../wallpapers/wallpapers/wallpaper.png /usr/share/backgrounds
sudo systemctl start --now bluetooth.service 
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
pip install iwlib
cd ../..
stow --adopt *
git restore .
stow *
cd install/install
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

#!/bin/sh

installdir=echo pwd

welcomemsg() {
    echo "Welcome to Omega Installation script. This script is intended to run on a archinstall-ed machine with qtile, pipewire, NetworkManager and Xorg already setup."
}

getuser() {
	# Asks on which user he wants to install the config 
    echo -n "Please enter the user you want to install Omega for: "
    read name
        # Checks username validity
	while ! echo "$name" | grep -q "^[a-z_][a-z0-9_-]*$"; do
		echo "Username not valid."
        getuserandpass
	done
        # Checks if the user exists
    while ! id -u "$name" >/dev/null 2>&1 ; do
        echo "This user does not exist."
        getuserandpass
    done
}

getdotfilesdir() {
    dotfilesdir="/home/$name/dotfiles"
}

pacmanconf() {
    sudo sed -i '/ParallelDownloads/s/^#//g' /etc/pacman.conf
    sudo sed -i "/^CheckSpace$/a ILoveCandy" /etc/pacman.conf 
}

laptopconf() {
    sudo cp 30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
}

lightdmconf() {
    sudo cp lightdm.conf /etc/lightdm/
    sudo cp lightdm-webkit2-greeter.conf /etc/lightdm/
    sudo cp ../../wallpapers/wallpapers/wallpaper.png /usr/share/backgrounds
}

ohmyzshinstaller() {
    sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
}

dotfilesinstaller() {
    cd $dotfilesdir
    stow --adopt *
    git restore .
    stow *
    cd $installdir 
} 

paruinstaller() {
    git clone https://aur.archlinux.org/paru.git
    cd paru
    makepkg -si 
    cd $installdir
}

rangerplug() {
    git clone https://github.com/alexanderjeurissen/ranger_devicons /home/$name/.config/ranger/plugins/ranger_devicons
}

servicestarter() {
    sudo systemctl enable --now bluetooth.service 
}

fonts=(ttf-firacode-nerd noto-fonts-emoji)
apps=(firefox audacity gimp ranger nvim)
tools=(unzip)
omega_dep=(git picom nitrogen wget stow rofi rofi-emoji pamixer bpytop zsh kitty bluez bluez-utils iwd xdotool xclip brightnessctl xf86-input-libinput libinput npm lightdm-webkit2-greeter lightdm-webkit-theme-litarvan python-pip)
pipinstall=(iwlib)
aurinstall=(fastfetch)

welcomemsg
getuser
getdotfilesdir
pacmanconf
laptopconf
lightdmconf
ohmyzshinstaller
paruinstaller
rangerplug
paru -Sy $fonts $app $tools $omega_dep $aurinstall
pip install $pipinstall
dotfilesinstaller

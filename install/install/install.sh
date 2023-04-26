#!/bin/sh


welcomemsg() {
    echo "Welcome to Omega Installation script. This script is intended to run on a archinstall-ed machine with qtile, pipewire, NetworkManager and Xorg already setup."
}

endmsg() {
    echo "Omega was successfuly installed !"
}

getuser() {
	# Asks on which user he wants to install the config 
    echo -n "Please enter the user you want to install Omega for: "
    read name
        # Checks username validity
	while ! echo "$name" | grep -q "^[a-z_][a-z0-9_-]*$"; do
		echo "Username not valid."
        getuser
	done
        # Checks if the user exists
    while ! id -u "$name" >/dev/null 2>&1 ; do
        echo "This user does not exist."
        getuser
    done
}

pacmanconf() {
    # Enables parallel downloads and pacman animation in the loading bar
    echo "Configuring pacman..."
    sudo sed -i '/ParallelDownloads/s/^#//g' /etc/pacman.conf
    sudo sed -i "/^CheckSpace$/a ILoveCandy" /etc/pacman.conf 
    echo "Done."
}

laptopconf() {
    # Configure the touchpad so double click and other functionalities work
    sudo cp 30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
}

lightdmconf() {
    # Sets lightdm theme
    echo "Configuring lightdm..."
    cd $installdir
    sudo cp $dotfilesdir/install/install/lightdm.conf /etc/lightdm/
    sudo cp $dotfilesdir/install/install/lightdm-webkit2-greeter.conf /etc/lightdm/
    mkdir /usr/share/backgrounds
    sudo cp $dotfilesdir/wallpapers/wallpapers/wallpaper.png /usr/share/backgrounds
    echo "Done."
}

ohmyzshinstaller() {
    echo "Installing Oh-My-Zsh..."
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended > /dev/null
    chsh -s $(which zsh)
    echo "Done."
}

dotfilesinstaller() {
    echo "Setting up dotfiles..."
    cd $dotfilesdir
    stow --adopt *
    git restore .
    stow *
    cd $installdir 
    echo "Done."
} 

paruinstaller() {
    echo "Installing paru..."
    git clone https://aur.archlinux.org/paru.git > /dev/null
    cd paru
    makepkg -si > /dev/null
    cd $installdir
    echo "Done."
}

lockscreenconf() {
    betterlockscreen -u "/home/syndrome/wallpapers/wallpaper.png"
}

vimpluginstaller() {
    echo "Installing vim plugins..."
    sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
    nvim -c PlugInstall -c qa!
    echo "Done."
}

rangerplug() {
    git clone https://github.com/alexanderjeurissen/ranger_devicons /home/$name/.config/ranger/plugins/ranger_devicons > /dev/null
}

servicestarter() {
    echo "Starting services..."
    sudo systemctl enable --now bluetooth.service 
    echo "Done."
}

welcomemsg
getuser

# Packages to install
fonts="ttf-firacode-nerd noto-fonts-emoji wqy-zenhei"
apps="firefox audacity gimp ranger neovim vlc"
tools="unzip reflector udisks2"
omega_dep="dunst git picom nitrogen wget stow rofi rofi-emoji pamixer bpytop zsh kitty bluez bluez-utils iwd xdotool xclip brightnessctl xf86-input-libinput libinput npm lightdm-webkit2-greeter lightdm-webkit-theme-litarvan python-pip"
pipinstall="iwlib python-xlib"
aurinstall="fastfetch tomatoshell betterlockscreen"

# Directories
installdir=echo pwd
dotfilesdir="/home/$name/dotfiles"


pacmanconf
laptopconf
paruinstaller
rangerplug
rm -rf /usr/share/backgrounds
echo "Installing packages:"
paru -Sy $fonts $apps $tools $omega_dep
paru -Sy $aurinstall
pip install $pipinstall
echo "Done."
vimpluginstaller
ohmyzshinstaller
dotfilesinstaller
lockscreenconf
servicestarter
lightdmconf

endmsg

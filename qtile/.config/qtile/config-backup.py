# _______________________________________________________________
#|                                                               |
#|    _____                 _                                    | 
#|  / ____|               | |                           _        |
#| | (___  _   _ _ __   __| |_ __ ___  _ __ ___   ___  ( ) ___   |
#|  \___ \| | | | '_ \ / _` | '__/ _ \| '_ ` _ \ / _ \ |/ / __|  | 
#|  ____) | |_| | | | | (_| | | | (_) | | | | | |  __/    \__ \  |
#| |_____/ \__, |_| |_|\__,_|_|  \___/|_| |_| |_|\___|    |___/  |
#|          __/ |                                                |
#|         |___/   QTILE CONFIG FILE                             |
#|                                                               |
#|  <stendhalxsyndrome@protonmail.com>                           |
#|_______________________________________________________________|
#


##### IMPORTS #####

from libqtile import bar, widget
from libqtile.command import lazy
from libqtile.lazy import lazy
from libqtile.config import Group, Key, Screen
import os, socket


##### CONSTANTS #####

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "xfce4-terminal"  # My terminal of choice
myConfig = "~/.config/qtile/config.py"  # The Qtile config file location
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())




#### COLORSCHEME ####

colors = {
        "black": "#1F2430", #Black Bacground,
        "white": "#CBCCC6", #White Foreground
        "pink": "#F28779", #Pink
        "green": "#A6CC70", #Green
        "yellow": "#FFCC66", #Yellow
        "cyan": "#5CCFE6", #Cyan
        "orange": "#F29E74", #Orange
        "blue": "#77A8D9", #Blue
        "grey": "#5C6773", #Grey
}


#### KEYBINDS ####

keys = [
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc="Restart Qtile"
    ),
    Key([mod], "v",
        lazy.spawn(myTerm + " -e code"),
        desc="Launch Visual Studio Code"
    ),
    Key([mod], "f",
        lazy.spawn("firefox"),
        desc="Launch Firefox"
    ),
    Key([mod], "k",
    lazy.window.kill(),
    desc="Kill active window")
]


#### GROUPS ####

groups = [
        Group("WWW"),
        Group("DEV"),
        Group("TERM"),
        Group("MUS"),
        Group("CHAT"),
        Group("GFX"),
        Group("RAND"),
        ]


#### TOP BAR ####
top_bar=bar.Bar([
    widget.Sep(
        linewidth = 0,
        padding = 6,
        foreground = colors[1],
        background = colors[0]
        ),
    widget.GroupBox(
        font = "Ubuntu Bold",
        fontsize = 9,
        margin_y = 3,
        margin_x = 5,
        padding_y = 5,
        padding_x = 5,
        borderwidth = 3,
        active = colors[1],
        inactive = colors[1],
        rounded = False,
        highlight_color = colors[0],
        highlight_method = "line",
        this_current_screen_border = colors[6],
        his_screen_border = colors [4],
        other_current_screen_border = colors[0],
        other_screen_border = colors[0],
        foreground = colors[1],
        background = colors[0]
        ),
    widget.Prompt(
        prompt = prompt,
        font = "Ubuntu Mono",
        padding = 10,
        foreground = colors[3],
        background = colors[1]
        ),],
        opacity=1.0, 
        size=20),




#### SCREENS ####

screens = [
    Screen(top=top_bar)
]
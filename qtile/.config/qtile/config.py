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

from libqtile import bar, widget, layout, qtile
from libqtile.command import lazy
from libqtile.lazy import lazy
from libqtile.config import Group, Key, Screen
import os, socket


##### CONSTANTS #####

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
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
        "red": "#b30000", #Orange
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
    Key([mod], "t",
        lazy.spawn("kitty"),
        desc="Launch a Terminal"
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

layout_theme = {"border_width": 2,
                "margin": 15,
                "border_focus": colors["red"],
                "border_normal": colors["black"]
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

top_bar=bar.Bar([
    widget.Sep(
        linewidth = 0,
        padding = 6,
        foreground = colors["white"],
        background = colors["black"]
        ),
    widget.GroupBox(
        font = "Ubuntu Bold",
        fontsize = 11,
        margin_y = 3,
        margin_x = 5,
        padding_y = 5,
        padding_x = 5,
        borderwidth = 3,
        active = colors["white"],
        inactive = colors["white"],
        rounded = False,
        highlight_color = colors["black"],
        highlight_method = "line",
        this_current_screen_border = colors["red"],
        his_screen_border = colors ["red"],
        other_current_screen_border = colors["black"],
        other_screen_border = colors["black"],
        foreground = colors["white"],
        background = colors["black"]
        ),
    widget.Prompt(
        prompt = prompt,
        font = "Ubuntu Mono",
        padding = 10,
        foreground = colors["green"],
        background = colors["white"]
        ),
    widget.Sep(
        linewidth = 0,
        padding = 25,
        foreground = colors["white"],
        background = colors["black"]
        ),
    widget.WindowName(
        foreground = colors["white"],
        background = colors["black"],
        padding = 0,
        fontsize = 14,
        max_chars = 100
        ),
    widget.TextBox(
            text = '',
            background = colors["black"],
            foreground = colors["red"],
            padding = 0,
            margin = 0,
            fontsize = 35,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.TextBox(
            text = "💾",
            padding = 2,
            foreground = colors["white"],
            background = colors["red"],
            fontsize = 14,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.Memory(
            foreground = colors["white"],
            background = colors["red"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bpytop')},
            padding = 5
        ),
    widget.TextBox(
            text = '',
            background = colors["red"],
            foreground = colors["black"],
            padding = 0,
            margin = 0,
            fontsize = 35,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.TextBox(
            text = "🌡️",
            padding = 2,
            foreground = colors["white"],
            background = colors["black"],
            fontsize = 14,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.OpenWeather(
            foreground = colors["white"],
            background = colors["black"],
            threshold = 90,
            padding = 5,
            cityid = 6455396,
            language = "fr",
            format = "{main_temp}°{units_temperature}, {weather_details}"
        ),
    widget.TextBox(
            text = '',
            background = colors["black"],
            foreground = colors["red"],
            padding = 0,
            margin = 0,
            fontsize = 35,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.TextBox(
            text = "📥",
            padding = 2,
            foreground = colors["white"],
            background = colors["red"],
            fontsize = 14,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.Net(
            interface = "enp37s0",
            format = '{down} ↓↑ {up}',
            foreground = colors["white"],
            background = colors["red"],
            padding = 5
        ),
    widget.TextBox(
            text = '',
            background = colors["red"],
            foreground = colors["black"],
            padding = 0,
            margin = 0,
            fontsize = 35,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.TextBox(
            text = "🔊",
            padding = 2,
            foreground = colors["white"],
            background = colors["black"],
            fontsize = 14,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.Volume(
            foreground = colors["white"],
            background = colors["black"],
            padding = 5,
            mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn('pavucontrol')},
        ),
    widget.TextBox(
            text = '',
            background = colors["black"],
            foreground = colors["red"],
            padding = 0,
            margin = 0,
            fontsize = 35,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.TextBox(
            text = "🕐",
            padding = 2,
            foreground = colors["white"],
            background = colors["red"],
            fontsize = 14,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.Clock(
            foreground = colors["white"],
            background = colors["red"],
            format = " %A, %d %B - %H:%M "
        ),



        ],
        opacity=1.0, 
        size=30)
    




#### SCREENS ####

screens = [
    Screen(top=top_bar)
]
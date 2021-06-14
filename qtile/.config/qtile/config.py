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

from libqtile import bar, widget, layout, qtile, hook
from libqtile.command import lazy
from libqtile.lazy import lazy
from libqtile.config import Group, Key, Screen
import os, socket, subprocess


##### CONSTANTS #####

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
myConfig = "~/.config/qtile/config.py"  # The Qtile config file location
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


#### COLORSCHEME ####

colors = {
        "black": "#1F2430",
        "white": "#CBCCC6",
        "pink": "#F28779",
        "green": "#A6CC70",
        "yellow": "#FFCC66",
        "cyan": "#5CCFE6",
        "red": "#b30000",
        "blue": "#77A8D9",
        "grey": "#5C6773",
}


#### KEYBINDS ####

keys = [
    ### the essentials
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc="Restart Qtile"
    ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),
    Key([mod, "shift"], "s",
        lazy.spawn("shutdown now"),
        desc='Shutdown Qtile'
    ),
    Key([mod], "x",
        lazy.window.kill(),
        desc="Kill active window"
    ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),

    ### groups
    Key([mod], "F1",
        lazy.group["WWW"].toscreen(),
        desc='Toggle WWW'
    ),
    Key([mod], "F2",
        lazy.group["DEV"].toscreen(),
        desc='Toggle DEV'
    ),
    Key([mod], "F3",
        lazy.group["TERM"].toscreen(),
        desc='Toggle TERM'
    ),
    Key([mod], "F4",
        lazy.group["MUS"].toscreen(),
        desc='Toggle MUS'
    ),
    Key([mod], "F5",
        lazy.group["CHAT"].toscreen(),
        desc='Toggle CHAT'
    ),
    Key([mod], "F6",
        lazy.group["GFX"].toscreen(),
        desc='Toggle GFX'
    ),
    Key([mod], "F7",
        lazy.group["RAND"].toscreen(),
        desc='Toggle RAND'
    ),

    ### windows controls
    Key([mod], "j",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),
    Key([mod], "k",
        lazy.layout.down(),
        desc='Move focus up in current stack pane'
    ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
    ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
    ),
    Key([mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    Key([mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key([mod], "d",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
    ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
    ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),

    ### launch apps
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
    Key([mod], "r",
        lazy.spawn("rofi -show run"),
        desc="Launch Rofi in run mode"
    ),
    Key([mod, "shift"], "r",
        lazy.spawn("rofi -show window"),
        desc="Launch Rofi in run mode"
    ),
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


#### LAYOUTS ####

layout_theme = {"border_width": 2,
                "margin": 15,
                "border_focus": colors["red"],
                "border_normal": colors["black"]
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Columns(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
]


#### TOP BAR ####

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
    widget.CurrentLayout(
            background = colors["red"],
            foreground = colors["white"],
            padding = 0,
            margin = 0,
            fontsize = 13,
        ),
    widget.Sep(
        linewidth = 0,
        padding = 6,
        foreground = colors["white"],
        background = colors["red"]
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
            text = "🕐",
            padding = 2,
            foreground = colors["white"],
            background = colors["black"],
            fontsize = 14,
            font="Ubuntu Mono Nerd Font",
        ),
    widget.Clock(
            foreground = colors["white"],
            background = colors["black"],
            format = " %A, %d %B - %H:%M "
        ),



        ],
        opacity=1.0, 
        size=30)


#### SCREENS ####

screens = [
    Screen(top=top_bar)
]



@hook.subscribe.startup_once
def start_once():
    subprocess.call(['~/.config/qtile/autostart.sh'])

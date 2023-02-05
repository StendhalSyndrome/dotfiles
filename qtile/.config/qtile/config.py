# import libraries

from libqtile import bar, widget, layout, qtile, hook
from libqtile.command import lazy
from libqtile.lazy import lazy
from libqtile.config import Group, Key, Screen
import os, socket, subprocess


# constants

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
myConfig = "~/.config/qtile/config.py"  # The Qtile config file location
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
home = os.path.expanduser('~')

@hook.subscribe.startup_once
def autostart():
    subprocess.call([home + '/.config/qtile/autostart.sh'])

@lazy.function
def window_to_prev_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None and i != 0:
        qtile.current_window.togroup(qtile.groups[i - 1].name)
        qtile.current_screen.toggle_group(qtile.groups[i - 1])

@lazy.function
def window_to_next_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None and i != 6:
        qtile.current_window.togroup(qtile.groups[i + 1].name)
        qtile.current_screen.toggle_group(qtile.groups[i + 1])

# colorscheme

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


# keybinds

keys = [
    ### the essentials
    Key([mod, "shift"], "y",
        lazy.reload_config(),
        desc="Restart Qtile"
    ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
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

    ### sound
    Key([mod, "shift"], "F5",
        lazy.spawn("pamixer -d 5"),
        desc='Volume down',
    ),
    Key([mod, "shift"], "F6",
        lazy.spawn("pamixer -i 5"),
        desc='Volume up',
    ),

    ### brightness
    Key([mod, "shift"], "F3",
        lazy.spawn("brightnessctl s 10%-"),
        desc='Brightness down',
    ),
    Key([mod, "shift"], "F4",
        lazy.spawn("brightnessctl s +10%"),
        desc='Brightness uo',
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
        desc='Toggle fullscreen'
    ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='Toggle floating'
    ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),
    Key([mod, "shift"], "h",
        window_to_prev_group(),
        desc='Move window to previous group'
    ),
    Key([mod, "shift"], "l",
        window_to_next_group(),
        desc='Move window to next group'
    ),



    ### launch apps
    Key([mod], "v",
        lazy.spawn(myTerm + " -e nvim"),
        desc="Launch Neovim"
    ),
    Key([mod], "f",
        lazy.spawn("firefox"),
        desc="Launch Firefox"
    ),
    Key([mod], "t",
        lazy.spawn(myTerm),
        desc="Launch a Terminal"
    ),
     Key([mod], "e",
        lazy.spawn(myTerm + " -e ranger"),
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
    Key([mod, "shift"], "e",
        lazy.spawn("rofi -modi emoji -show emoji"),
        desc="Launch Rofi in emoji selection mode"
    ),
    Key([mod, "shift"], "w",
        lazy.spawn([home + "/.local/bin/rofi-wifi"]),
        desc="Launch Rofi in wifi mode"
    ),
    Key([mod, "shift"], "b",
        lazy.spawn([home + "/.local/bin/rofi-bluetooth"]),
        desc="Launch Rofi in bluetooth mode"
    ),
]


# groups

groups = [
        Group("WWW"),
        Group("DEV"),
        Group("TERM"),
        Group("MUS"),
        Group("CHAT"),
        Group("GFX"),
        Group("RAND"),
        ]


# layouts

layout_theme = {"border_width": 2,
                "margin": 14,
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


# top bar

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
        ),
    widget.TextBox(
            text = "💾",
            padding = 2,
            foreground = colors["white"],
            background = colors["red"],
            fontsize = 14,
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
        ),
    widget.TextBox(
            text = "🔋",
            padding = 2,
            foreground = colors["white"],
            background = colors["black"],
            fontsize = 14,
        ),
    widget.Battery(
            foreground = colors["white"],
            background = colors["black"],
            threshold = 90,
            padding = 5,
            discharge_char ="↘️",
            charge_char = "↗️",
            format = "{char} {percent: 2.0%} ",
        ),
    widget.TextBox(
            text = '',
            background = colors["black"],
            foreground = colors["red"],
            padding = 0,
            margin = 0,
            fontsize = 35,
        ),
    widget.TextBox(
            text = "📥",
            padding = 2,
            foreground = colors["white"],
            background = colors["red"],
            fontsize = 14,
        ),
    widget.Wlan(
            background = colors["red"],
            foreground = colors["white"],
            padding = 5,
            format = "{essid}",
        ),
    widget.TextBox(
            text = '/',
            background = colors["red"],
            foreground = colors["white"],
            padding = 2,
        ),
    widget.Net(
            interface = "wlan0",
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
        ),
    widget.TextBox(
            text = "🔊",
            padding = 2,
            foreground = colors["white"],
            background = colors["black"],
            fontsize = 14,
        ),
    widget.GenPollText(
            background = colors["black"],
            foreground = colors["white"],
            padding = 5,
            margin = 25,
            func = lambda: "\n" + subprocess.run(['pamixer', '--get-volume-human'], stdout=subprocess.PIPE).stdout.decode("utf-8"),
            update_interval = 2,
        ),
    widget.TextBox(
            text = '',
            background = colors["black"],
            foreground = colors["red"],
            padding = 0,
            margin = 0,
            fontsize = 35,
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
        ),
    widget.TextBox(
            text = "🕐",
            padding = 2,
            foreground = colors["white"],
            background = colors["black"],
            fontsize = 14,
        ),
    widget.Clock(
            foreground = colors["white"],
            background = colors["black"],
            format = " %A, %d %B - %H:%M "
        ),



        ],
        opacity=1.0, 
        size=30)


# screens

screens = [
    Screen(top=top_bar)
]


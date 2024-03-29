import os
from typing import List
from libqtile import bar, layout, widget
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
)
from libqtile.lazy import lazy
from libqtile import qtile

#  _   _       _   _                  
# | | | | ___ | |_| | _____ _   _ ___ 
# | |_| |/ _ \| __| |/ / _ \ | | / __|
# |  _  | (_) | |_|   <  __/ |_| \__ \
# |_| |_|\___/ \__|_|\_\___|\__, |___/
#                           |___/     

mod = "mod4"
terminal = "kitty"

keys = [
    
    # Layout hotkeys
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
 

    # Window hotkeys
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
 

    # Spec hotkeys
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # App hotkeys
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using Rofi"),
]

#   ____                           
#  / ___|_ __ ___  _   _ _ __  ___ 
# | |  _| '__/ _ \| | | | '_ \/ __|
# | |_| | | | (_) | |_| | |_) \__ \
#  \____|_|  \___/ \__,_| .__/|___/
#                       |_|        

# groups = [Group(i) for i in "123456789"]

groups = [
    Group(
        name="1",
        label="",
        matches=[
        ],
        layout="columns",
    ),
    Group(
        name="2",
        label="",
        matches=[
            Match(wm_class=["nvim"]),
            Match(wm_class=["jetbrains-pycharm"]),
            Match(wm_class=["jetbrains-clion"]),
        ],
        layout="columns",
    ),
    Group(
        name="3",
        label="",
        matches=[
            Match(wm_class=["discord"]),

        ],
        layout="columns",
    ),
    Group(
        name="4",
        label="",
        matches=[
            Match(wm_class=["spotify"]),
        ],
        layout="columns",
    ),
    Group(
        name="5",
        label="",
        matches=[
            Match(wm_class=["libreoffice"]),
            Match(wm_class=["Zathura"]),
        ],
        layout="columns",
    ),
    Group(
        name="6",
        label="漣",
        matches=[
            Match(wm_class=["lxappearance"]),
            Match(wm_class=["kvantummanager"]),
            Match(wm_class=["qt5ct"]),
            Match(wm_class=["nitrogen"]),
        ],
        layout="columns",
    ),
    Group(
        name="7",
        label="八",
        layout="columns",
    ),
    Group(
        name="8",
        label="九",
        layout="columns",
    ),
]


for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

#  _                            _          ___    __        ___     _            _       
# | |    __ _ _   _  ___  _   _| |_ ___   ( _ )   \ \      / (_) __| | __ _  ___| |_ ___ 
# | |   / _` | | | |/ _ \| | | | __/ __|  / _ \/\  \ \ /\ / /| |/ _` |/ _` |/ _ \ __/ __|
# | |__| (_| | |_| | (_) | |_| | |_\__ \ | (_>  <   \ V  V / | | (_| | (_| |  __/ |_\__ \
# |_____\__,_|\__, |\___/ \__,_|\__|___/  \___/\/    \_/\_/  |_|\__,_|\__, |\___|\__|___/
#             |___/                                                   |___/              


def init_layout_theme():
    return {
        "margin": 6,
        "border_width": 1,
        "border_focus": "#d79921",
        "border_normal": "#3c3836",
    }


layout_theme = init_layout_theme()

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font Bold",
    fontsize=12,
    padding=8,
)
extension_defaults = widget_defaults.copy()


def init_group_box_settings():
    return {
        "fontsize": 20,
        "borderwidth": 4,
        "active": "#ebdbb2",
        "inactive": "#928374",
        "this_current_screen_border": "#b8bb26",
        "highlight_method": "text",
        "disable_drag": True,
        "urgent_alert_method": "text",
        "urgent_border": "#cc241d",
        "urgent_text": "#cc241d",
        "visible_groups": ["1", "2", "3", "4", "5", "6"],
    }


group_box_settings = init_group_box_settings()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text=" ",
                    foreground="#ebdbb2",
                    fontsize=16,
                    padding=12,
                ),

                widget.GroupBox(
                    **group_box_settings,
                ),
                widget.Prompt(),
                widget.Spacer(),
                widget.WindowName(
                    foreground="#ebdbb2",
                    width=bar.CALCULATED,
                    empty_group_string="Desktop",
                    max_chars=130,
                ),
                widget.Spacer(),
                widget.Systray(),
                widget.Sep(
                    padding=15,
                    linewidth=0,
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background="#282828",
                    foreground="#cc241d",
                ),
                widget.CurrentLayoutIcon(
                    background="#cc241d",
                    foreground="#ebdbb2",
                    scale=.6,
                    padding=0,
                ),
                widget.CurrentLayout(
                    background="#cc241d",
                    foreground="#ebdbb2",
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background="#cc241d",
                    foreground="#98971A",
                ),
                widget.TextBox(
                    text=" ",
                    background="#98971A",
                    foreground="#ebdbb2",
                    fontsize=16,
                    padding=0,
                ),
                widget.Wlan(
                    interface="wlp7s0u1",
                    format="{essid}",
                    background="#98971A",
                    foreground="#ebdbb2",
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                        os.path.expanduser("~/.config/qtile/rofi-wifi-menu.sh")
                    )},
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background="#98971A",
                    foreground="#D79921",
                ),
                widget.TextBox(
                    text="墳 ",
                    background="#D79921",
                    foreground="#ebdbb2",
                    fontsize=16,
                    padding=0,
                ),
                widget.PulseVolume(
                    background="#D79921",
                    foreground="#ebdbb2",
                    limit_max_volume=True,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty pacmixer")},
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background="#D79921",
                    foreground="#458588",
                ),
                widget.TextBox(
                    text=" ",
                    background="#458588",
                    foreground="#ebdbb2",
                    fontsize=16,
                    padding=0,
                ),
                widget.Clock(
                    background="#458588",
                    foreground="#ebdbb2",
                    format="%a, %b %d",
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background="#458588",
                    foreground="#B16286",
                ),
                widget.TextBox(
                    text=" ",
                    background="#B16286",
                    foreground="#ebdbb2",
                    fontsize=16,
                    padding=0,
                ),
                widget.Clock(
                    background="#B16286",
                    foreground="#ebdbb2",
                    format="%I:%M %p",
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background="#B16286",
                    foreground="#689D6A",
                ),
                widget.TextBox(
                    text="",
                    background="#689D6A",
                    foreground="#ebdbb2",
                    fontsize=16,
                    padding=16,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                        os.path.expanduser("~/.config/qtile/rofi-power-menu.sh")
                    )},
                ),
            ],
            background="#282828",
            size=24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

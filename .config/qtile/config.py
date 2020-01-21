# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# pylint: disable=no-member

import os
import subprocess
from datetime import datetime
from pathlib import Path
from time import time
from typing import List  # noqa: F401

from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, Key

from assets import Commands, KeyboardLayout, colors
from screens import DualMonitors, SingleMonitor, num_screens


# Screenshots
def screenshot(save=True, copy=True):
    def f(qtile):
        path = Path.home() / 'Pictures'
        date_time = datetime.fromtimestamp(time())
        filename = date_time.strftime("%Y-%m-%d-%-I-%M-%p-%S")
        path /= f'screenshot_{filename}.png'
        shot = subprocess.run(['maim'], stdout=subprocess.PIPE)

        if save:
            with open(path, 'wb') as sc:
                sc.write(shot.stdout)

        if copy:
            subprocess.run(['xclip', '-selection', 'clipboard', '-t',
                            'image/png'], input=shot.stdout)
    return f


# Keyboard next layout
@lazy.function
def NextKeyboardLayout(qtile):
    KeyboardLayout.cmd_next_keyboard()


# Keys
mod = "mod4"
alt = "mod1"
control = "control"
shift = "shift"

# Program defines
terminal = "termite"
browser = "vivaldi-stable"
filemgr = "nemo"
editor_gui = "code"



keys = [
    # Grow windows
    Key([mod, shift], "w", lazy.layout.grow_up()),
    Key([mod, shift], "a", lazy.layout.grow_left()),
    Key([mod, shift], "s", lazy.layout.grow_down()),
    Key([mod, shift], "d", lazy.layout.grow_right()),

    # Switch between windows (focus)
    Key([mod], "j", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "i", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, shift], "j", lazy.layout.shuffle_left()),
    Key([mod, shift], "l", lazy.layout.shuffle_right()),
    Key([mod, shift], "k", lazy.layout.shuffle_down()),
    Key([mod, shift], "i", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([alt], "Tab", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, control], "Tab", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, shift], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),

    # Window
    Key([mod], "n", lazy.window.toggle_minimize()),
    Key([mod], "m", lazy.window.toggle_maximize()),

    # Language
    Key([mod], "space", NextKeyboardLayout),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),

    Key([mod, control], "r", lazy.restart()),
    Key([mod, control], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # Sys Programs
    Key([mod, shift], "f", lazy.spawn(Commands.rofi)),

    # Programs
    Key([mod], "w", lazy.spawn(browser)),
    Key([mod], "e", lazy.spawn(filemgr)),
    Key([alt, control], "c", lazy.spawn(editor_gui)),
    Key([mod], "t", lazy.spawn(terminal)),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn(Commands.brightness_up)),
    Key([], "XF86MonBrightnessDown", lazy.spawn(Commands.brightness_down)),

    # Media
    Key([], "XF86AudioRaiseVolume", lazy.spawn(Commands.volume_up)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(Commands.volume_down)),
    Key([], "XF86AudioMute", lazy.spawn(Commands.volume_toggle)),
    Key([], "XF86AudioMicMute", lazy.spawn(Commands.mic_toggle)),

    Key([], 'Print', lazy.function(screenshot())),
    Key(['control'], 'Print', lazy.spawn('xfce4-screenshooter'))

]

# groups = [Group(i) for i in "asdfuiop"]
groups = [Group(i) for i in ''.join(map(str, [*range(1, 10)]))]

for i in groups:
    if num_screens==1:
        switch = lazy.group[i.name].toscreen()
    else:
        switch = None
    
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group if monitors=1
        Key([mod, shift], i.name, lazy.window.togroup(
            i.name), switch),
    ])

layouts = [
    layout.Max(border_width=0, max_border_width=0, fullscreen_border_width=0),
    # layout.Stack(num_stacks=2),
    layout.Bsp(max_border_width=0, fullscreen_border_width=0),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

if num_screens == 2:
    screens = DualMonitors()
else:
    screens = SingleMonitor()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    max_border_width=0,
    fullscreen_border_width=0,
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},  # gitk
        {'wmclass': 'makebranch'},  # gitk
        {'wmclass': 'maketag'},  # gitk
        {'wname': 'branchdialog'},  # gitk
        {'wname': 'pinentry'},  # GPG key password entry
        {'wmclass': 'gcr-prompter'},
        {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ])
auto_fullscreen = True
focus_on_window_activation = "smart"


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

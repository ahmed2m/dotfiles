# pylint: disable=no-member
from libqtile import widget


# Widgets
KeyboardLayout = widget.KeyboardLayout(configured_keyboards=['us', 'ara'])

# Commands
class Commands:
    autorandr = ['autorandr', '-c']
    alsamixer = 'st -e alsamixer'
    update = "st -e yay -Syu"
    volume_up = 'amixer -q -c 0 sset Master 5dB+'
    volume_down = 'amixer -q -c 0 sset Master 5dB-'
    volume_toggle = 'amixer -q set Master toggle'
    mic_toggle = 'amixer set Capture toggle'
    brightness_up = 'xbacklight -inc 10'
    brightness_down = 'xbacklight -dec 10'
    rofi = "rofi -show run"

    # def reload_screen(self):
    #     call(self.autorandr)

# Colors
colors = {
    "black": "#000000",
    "white": "#ffffff",
    "grey": "#454545",
    "red": "#ff0000",
    "yellow": "#ffff00",
    "lightgrey": "#999999",
    "silver": "#C0C0C0",
    "navy": "#000080",
    "darkblue": "#2471A3",
    "darkred": "#C0392B",
    "teal": "#008080",
    "maroon": "#800000",
    "salmon": "#FA8072"
}
from Xlib import display
from libqtile.config import Screen

from bars import single_monitor_bottom_bar,dual_monitor_screen_1_bottom,dual_monitor_screen_2_bottom

# Get resources from the display
d = display.Display()
s = d.screen()
r = s.root
res = r.xrandr_get_screen_resources()._data


# Count the number of screens
num_screens = 0
for output in res['outputs']:
    mon = d.xrandr_get_output_info(output, res['config_timestamp'])._data
    if mon['num_preferred']:
        num_screens += 1


def SingleMonitor():
    return [
        Screen(
            bottom=single_monitor_bottom_bar,
        ),
    ]


def DualMonitors():
    return [
        Screen(bottom= dual_monitor_screen_1_bottom
        ),
        Screen(bottom= dual_monitor_screen_2_bottom
        ),
    ]
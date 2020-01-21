from libqtile import bar, widget
from mic import MicIndicator
from mybat import Battery
from assets import colors, Commands, KeyboardLayout
import os
# pylint: disable=no-member



inoffensive_green = '339966'

single_monitor_bottom_bar= bar.Bar(
                [
                    widget.Wallpaper(directory=os.path.expanduser("~/Pictures/wallpapers/"), label=""),
                    widget.GroupBox(disable_drag=True),
                    widget.Prompt(),
                    widget.TaskList(background='000000',
                                    highlight_method='block',
                                    max_title_width=300),

                    widget.Systray(),
                    # widget.Battery(
                    #     energy_now_file='charge_now',
                    #     energy_full_file='charge_full',
                    #     power_now_file='current_now',
                    #     discharge_char='↓',
                    #     charge_char='↑',
                    #     format='{char} {percent:2.0%}',
                    #     foreground=colors['yellow'],
                    #     low_foreground=colors['red']
                    # ),
                    widget.CurrentLayout(),
                    widget.Battery(
                        discharge_char='↓',
                        charge_char='↑',
                        format='{char} {percent:2.0%}',
                        # format = '{char} {hour:d}:{min:02d}   {percent:2.0%}',
                        foreground=colors['yellow'],
                        low_percentage=0.20,
                        low_foreground=colors['red'],
                    ),
                    widget.Net(interface='wlp3s0', update_interval=2),
                    MicIndicator(),
                    widget.Volume(volume_app=Commands.alsamixer),
                    KeyboardLayout,
                    widget.Clock(format='%Y-%m-%d %a %I:%M %p')
                ],
                24,
            )

dual_monitor_screen_1_bottom = single_monitor_bottom_bar

dual_monitor_screen_2_bottom = bar.Bar(
                [
                    widget.GroupBox(disable_drag=True,this_current_screen_border=inoffensive_green),
                    widget.TaskList(background='000000',
                                    highlight_method='block',
                                    max_title_width=300),
                    widget.CurrentLayout(),
                    MicIndicator(),
                    widget.Clock(format='%Y-%m-%d %a %I:%M %p')
                    ],
                24
            )
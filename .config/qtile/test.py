import traceback

try:
    with open("/sys/class/power_supply/BAT0/curent_now", 'tr') as check_file:  # try open file in text mode
        x = check_file.read()
        print(x)

except Exception as e:
    print(e.__class__.__name__)
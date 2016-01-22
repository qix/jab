from tooler import (
  Tooler,
  bash,
)

tooler = Tooler()

@tooler.command
def monitor():
  bash('''
xrandr --output DP-1 --auto
sleep 3
xrandr --output LVDS-1 --off
xrandr --output DP-1 --auto
''')

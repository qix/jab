import soco
from tooler import (
  Tooler,
  bash,
)

tooler = Tooler()

@tooler.command
def line_in():
  speakers = {
    s.player_name: s
    for s in soco.discover()
  }

  speakers['Josh'].unjoin()
  speakers['Josh'].switch_to_line_in()
  speakers['Josh'].play()
  speakers['Josh'].volume = 70


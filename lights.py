from tooler import (
  Tooler,
  bash,
)

tooler = Tooler()

# Discover: https://www.meethue.com/api/nupnp
IP="192.168.1.122"

# Register: huectl -u josh-dave-pc -r 192.168.1.122
USER="josh-dave-pc"

# Light config
CACTUS="2"
BLINDS="1"

def huectl(light, commands):
  bash('huectl -u %s %s %s %s' % (USER, IP, light, commands))


@tooler.command
def off():
  huectl(CACTUS, '--on false')
  huectl(BLINDS, '--on false')
  
@tooler.command
def warm():
  huectl(CACTUS, '--on true --hue 8043 --sat 202 --bri 252')
  huectl(BLINDS, '--on true --hue 61461 --sat 175 --bri 120')

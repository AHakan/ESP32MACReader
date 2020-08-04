# Easy way to read ESP32 MAC Address with python
# @github: AHakan
import os
import re

# Run esptool code
# You can change the port
stream = os.popen("esptool.py --port /dev/ttyUSB0 read_mac")

# Read console output
output = stream.read()

# Using output for
# Find 'MAC: '
x = output.find("MAC: ")

# Read MAC address
mac = output[x+5:x+22]

# Regex for mac address
p = re.compile(r'(?:[0-9a-fA-F]:?){12}')

# re.findall, find mac address
# and return upper case
return re.findall(p, mac)[0].upper()

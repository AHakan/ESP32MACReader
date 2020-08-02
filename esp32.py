# Easy way to read ESP32 MAC Address with python
# @github: AHakan
import os

# Run esptool code
# You can change the port
stream = os.popen("esptool.py --port /dev/ttyUSB0 read_mac")

# Read console output
output = stream.read()

# Using output for
# Find 'MAC: '
x = output.find("MAC: ")

# Read MAC address
# And write upper case
mac = output[x+5:x+22]
print(mac.upper())

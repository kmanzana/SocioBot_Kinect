# This file basically handles establishing and sending of bluetooth
# commands to the Arduino. The data to be sent is passed as a string to
# this file. Requires PyBluez
#call like: python sendBluetooth.py dataToSend
from bluetooth import *

#RFCOMM is essencially the equivelent of TCP for standard internet fare, 
#  but for Bluetooth
socket = BluetoothSocket(RFCOMM)

arduinoAddress = "00:06:66:08:61:A5"
bluetoothPort = 1

#Connect to device
socket.connect((arduinoAddress,bluetoothPort))

#Send the data
socket.send(sys.argv[1])

#Unfortunately, sending data via a seperate file doesn't really manage
#the Blueooth connection in a long lived manner
socket.close()

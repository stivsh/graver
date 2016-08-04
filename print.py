import serial
import time
# open serial port
ser = serial.Serial('/dev/ttyUSB0',9600)
time.sleep(4)
#read image
#convert to comand
#write command
ser.write("a\n")
time.sleep(10)
ser.flush()
ser.close()

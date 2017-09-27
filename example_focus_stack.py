import serial
port = "/dev/cu.usbmodem1421"

ser = serial.Serial(port, 9600, timeout=1)

for t in range(100):
    print t
    while ser.readline(): pass
    ser.write("t2000")
    time.sleep(1)
    ser.readline()
    time.sleep(.5)
    ser.write("b1")
    time.sleep(1)
    ser.readline()

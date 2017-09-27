import os
import serial

def get_connection(timeout=.2):
    ports = [
        "/dev/" + name
        for name in filter(
            lambda name: name.startswith("cu.usbmodem"),
            os.listdir("/dev/")
        )
    ]
    for port in ports:
        ser = None
        try:
            ser = serial.Serial(port, 9600, timeout=timeout)
            return ser
        except serial.SerialException:
            pass
        finally:
            if ser:
                ser.close()

if "__main__" == __name__:
    print get_connection()


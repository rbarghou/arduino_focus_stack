import serial
import time

from machine import Machine


if "__main__" == __name__:
    machine = Machine()
    for i in range(100):
        try:
            machine.move_slow_forward(3)
            time.sleep(.1)
            machine.trigger(1000)
            time.sleep(1)
        except serial.SerialException as e:
            print "Connection lost!  Reconnecting..."
            machine.reconnect()
            print "Connection reestablished."


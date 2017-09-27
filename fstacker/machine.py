from connection import get_connection
import time

FORWARD = "FORWARD"
BACKWARD = "BACKWARD"
FAST = "FAST"
SLOW = "SLOW" 


class Machine(object):

    def __init__(self):
        self.connection = get_connection()
        time.sleep(2)

    def open(self):
        self.connection.open()
        time.sleep(2)

    def close(self):
        self.connection.close()

    def run_command(self, command):
        self.connection.read_all()
        self.connection.write(command)
        msg = self.connection.readline()
        while not msg:
            msg = self.connection.readline()
        print msg

    def move(self, direction, speed, steps):
        if direction == FORWARD and speed == FAST:
            command_letter = "F" 
        elif direction == BACKWARD and speed == FAST:
            command_letter = "B" 
        elif direction == FORWARD and speed == SLOW:
            command_letter = "f"
        elif direction == BACKWARD and speed == SLOW:
            command_letter = "b" 
        command = command_letter + str(steps)
        self.run_command(command)

    def move_fast_forward(self, steps):
        self.move(FORWARD, FAST, steps)

    def move_fast_backward(self, steps):
        self.move(BACKWARD, FAST, steps)

    def move_slow_forward(self, steps):
        self.move(FORWARD, SLOW, steps)

    def move_slow_backward(self, steps):
        self.move(BACKWARD, SLOW, steps)

    def rotate_stage(self, position):
        command = "s" + str(position)
        self.run_command(command)

    def trigger(self, duration):
        command = "t" + str(duration)
        self.run_command(command)

if "__main__" == __name__:
    machine = Machine()
    machine.move_fast_forward(100)
    machine.move_fast_backward(100)
    machine.rotate_stage(0)
    machine.rotate_stage(10)
    machine.rotate_stage(60)
    machine.rotate_stage(150)
    machine.trigger(300)
    machine.trigger(1000)
    machine.trigger(10000)


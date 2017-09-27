from connection import get_connection
import time

if "__main__" == __name__:
    connection = get_connection()
    connection.read_all()
    time.sleep(2)
    connection.write("B100")
    msg = connection.readline()
    while not msg:
        msg = connection.readline()
    print msg


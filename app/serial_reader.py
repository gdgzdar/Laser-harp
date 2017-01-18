import serial


class Reader:
    def __init__(self, port):
        self.device = serial.Serial(port, 9600)

    def read_line(self):
        return self.device.readline()[:22]

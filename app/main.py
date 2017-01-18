from app.serial_reader import Reader
from app.audio import Player

if __name__ == '__main__':
    arduino = Reader("/dev/ttyACM0")
    for x in range(0, 50):
        print(arduino.read_line())

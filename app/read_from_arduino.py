import serial
import copy
from sound_player import *
from random import *
from time import *


class Harp:
    def __init__(self, musical_instrument, notes):
        #self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        self.musical_instrument = musical_instrument
        self.notes = notes
        self.actual_booleans = [False, False, False, False, False, False, False, False, False, False, False, False,
                                False, False, False, False, False, False, False, False, False, False]
        self.last_booleans = [False, False, False, False, False, False, False, False, False, False, False, False,
                              False, False, False, False, False, False, False, False, False, False]
        self.sounds = []
        #self.data = ''
        #for x in range(10):
        #    self.data = self.arduino.readline()
        #    print(self.data)

    def load_sounds(self):
        for y in range(len(self.notes)):
            self.sounds.append(Sound(os.path.join('../', 'sounds', self.musical_instrument, self.notes[y] + '.wav'), y))

    def parse_booleans(self):
        self.last_booleans = copy.copy(self.actual_booleans)
        for a in range(22):
            if self.data[a] == '0':
                self.actual_booleans[a] = False
            else:
                self.actual_booleans[a] = True

    def play_sound(self):
        for z in range(len(self.actual_booleans)):
            if self.actual_booleans[z] == True and not self.actual_booleans[z] == self.last_booleans[z]:
                self.sounds[z].play()
                print(z)

    def generate_random_sound(self):
        random_position = randint(0, 22)
        self.data = ''
        for x in range(0, 22):
            if x == random_position:
                self.data += '1'
            else:
                self.data += '0'

    def read_from_arduino(self):
        self.data = self.arduino.readline()

if __name__ == '__main__':
    notes = ['A', 'A1', 'A2', 'C', 'C1', 'C2', 'C3', 'D', 'D1', 'D2', 'E', 'E1', 'E2', 'F', 'F1', 'F2', 'G', 'G1',
             'G2', 'H', 'H1', 'H2']
    harp = Harp('Bass', notes)
    harp.load_sounds()
    while True:
        harp.generate_random_sound()
        harp.parse_booleans()
        harp.play_sound()
        sleep(0.1)




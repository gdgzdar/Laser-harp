import copy
import serial
from random import *

from sound_player import *


class Harp:
    def __init__(self, musical_instrument, notes):
        self.arduino = serial.Serial('/dev/ttyACM1', 9600)
        self.musical_instrument = musical_instrument
        self.NUMBER_OF_STRINGS = 22
        self.notes = notes
        self.actual_booleans = []
        self.last_booleans = []
        for x in range(0, self.NUMBER_OF_STRINGS):
            self.actual_booleans.append(False)
            self.last_booleans.append(False)
        self.sounds = []
        self.played_sounds = []
        self.x = 0
        self.data = ''
        for x in range(50):
            self.data = self.arduino.readline()
            print(self.data)

    def load_sounds(self):
        for y in range(len(self.notes)):
            self.sounds.append(Sound(os.path.join('../', 'sounds', self.musical_instrument, self.notes[y] + '.wav'), y))

    def parse_booleans(self):
        self.last_booleans = copy.copy(self.actual_booleans)
        for a in range(self.NUMBER_OF_STRINGS):
            if self.data[a] == '0':
                self.actual_booleans[a] = False
            else:
                self.actual_booleans[a] = True

    def play_sound(self):
        for z in range(len(self.actual_booleans)):
            if self.actual_booleans[z] == True and not self.actual_booleans[z] == self.last_booleans[z]:
                self.x += 1
                if self.x >= self.NUMBER_OF_STRINGS:
                    self.played_sounds[0].player.stop()
                    self.played_sounds[0].player.delete()
                    self.played_sounds[0].sound.delete()
                    self.played_sounds[0].listener.delete()
                    self.played_sounds.remove(self.played_sounds[0])
                    self.x -= 1
                self.played_sounds.append(self.sounds[z])
                self.sounds[z].play()
                print(self.x)

    def generate_random_sound(self):
        random_position = randint(0, self.NUMBER_OF_STRINGS)
        self.data = ''
        for x in range(0, self.NUMBER_OF_STRINGS):
            if x == random_position:
                self.data += '1'
            else:
                self.data += '0'

    def read_from_arduino(self):
        self.data = self.arduino.readline()

if __name__ == '__main__':
    notes = ["C","D","E","F","G","A","H","C1","D1","E1","F1","G1","A1","H1","C2","D2","E2","F2","G2","A2","H2","C3"]
    harp = Harp('Violin', notes)
    harp.load_sounds()
    while True:
        harp.read_from_arduino()
        harp.parse_booleans()
        harp.play_sound()


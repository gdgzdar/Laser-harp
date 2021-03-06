import pygame
import os
import serial
import sys
import glob


class Reader:
    def __init__(self, port):
        self.device = serial.Serial(port, 9600)

    @staticmethod
    def get_available_ports():
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
                ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        return ports

    def read_line(self):
        line = str(self.device.readline())
        line = line[1:24]
        return line


class Player:
    def __init__(self, instrument, port):
        self.actual_tones = "0000000000000000000000000000"
        self.last_tones = "000000000000000000000000000"
        self.mixer = None
        self.load_pygame()
        self.instrument = instrument
        self.sounds = {}
        self.load_sounds()
        self.arduino = Reader(port)
        self.indexes_to_notes = [
            "C", "D", "E", "F", "G", "A", "H", "C1", "D1", "E1", "F1", "G1", "A1", "H1", "C2", "D2", "E2", "F2", "G2",
            "A2", "H3", "C3", "C3", "C3", "C3"
        ]

    def load_pygame(self):
        pygame.init()
        self.mixer = pygame.mixer
        self.mixer.init(44100, -16, 2, 2048)
        self.mixer.set_num_channels(200)

    def load_sounds(self):
        self.sounds = {
            "C": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C.wav")),
            "D": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "D.wav")),
            "E": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "E.wav")),
            "F": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "F.wav")),
            "G": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "G.wav")),
            "A": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "A.wav")),
            "H": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "H.wav")),
            "C1": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C1.wav")),
            "D1": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "D1.wav")),
            "E1": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "E1.wav")),
            "F1": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "F1.wav")),
            "G1": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "G1.wav")),
            "A1": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "A1.wav")),
            "H1": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "H1.wav")),
            "C2": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C2.wav")),
            "D2": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "D2.wav")),
            "E2": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "E2.wav")),
            "F2": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "F2.wav")),
            "G2": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "G2.wav")),
            "A2": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "A2.wav")),
            "H3": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "H2.wav")),
            "C3": self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C3.wav"))
        }

    def play_sound(self, sound):
        channel = self.mixer.find_channel()
        channel.play(self.sounds.get(sound))

    def listen_arduino(self):
        for x in range(0, 20):
            self.arduino.read_line()
        while True:
            self.actual_tones = self.arduino.read_line()
            for x in range(0, len(self.actual_tones)):
                if self.actual_tones[x] != self.last_tones[x]:
                    self.play_sound(self.indexes_to_notes[x])
            self.last_tones = self.actual_tones

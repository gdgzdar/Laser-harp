import pygame
import os
import serial


class Reader:
    def __init__(self, port):
        self.device = serial.Serial(port, 9600)

    def read_line(self):
        line = str(self.device.readline())
        line = line[1:24]
        return line


class Player:
    def __init__(self, instrument, port):
        self.mixer = None
        self.load_pygame()
        self.instrument = instrument
        self.sounds = {}
        self.load_sounds()
        self.arduino = Reader(port)

    def load_pygame(self):
        pygame.init()
        self.mixer = pygame.mixer
        self.mixer.init(44100, -16, 2, 2048)
        self.mixer.set_num_channels(100)

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
        while True:
            print(self.arduino.read_line())

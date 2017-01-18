import pygame
import os


class Player:
    def __init__(self, instrument):
        self.mixer = None
        self.load_pygame()
        self.instrument = instrument
        self.sounds = {}
        self.load_sounds()

    def load_pygame(self):
        pygame.init()
        self.mixer = pygame.mixer
        self.mixer.init(44100, -16, 2, 2048)
        self.mixer.set_num_channels(100)

    def load_sounds(self):
        self.sounds = [
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "D.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "E.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "F.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "G.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "A.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "H.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C1.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "D1.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "E1.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "F1.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "G1.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "A1.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "H1.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C2.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "D2.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "E2.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "F2.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "G2.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "A2.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "H2.wav")),
            self.mixer.Sound(os.path.join("..", "sounds", self.instrument, "C3.wav"))
        ]

    def play(self, sound):
        channel = self.mixer.find_channel()
        channel.play(self.sounds.get(sound))

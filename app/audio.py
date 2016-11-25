import pygame


class Player:
    def __init__(self):
        self.mixer = None
        self.load_pygame()
        self.sounds = {}
        self.load_sounds()

    def load_pygame(self):
        pygame.init()
        self.mixer = pygame.mixer
        self.mixer.init(44100, -16, 2, 2048)
        self.mixer.set_num_channels(100)

    def load_sounds(self):
        self.sounds = {
            "a": self.mixer.Sound("All_Guns_Blazing.wav"),
            "b": self.mixer.Sound("sparta_zacatek.wav"),
            "c": self.mixer.Sound("Winged_Hussars_zacatek.wav")
        }

    def play(self, sound):
        channel = self.mixer.find_channel()
        channel.play(self.sounds.get(sound))

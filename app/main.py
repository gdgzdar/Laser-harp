import pygame
import pygame.constants
import os
import getch


def get_user_input(array, last_key):
    user_input = getch.Getch().__call__()
    return play_sound(array.get(user_input), user_input, last_key)


def play_sound(sound, user_input, last_key):
    if not pygame.mixer.get_busy() or not user_input == last_key:
        sound.play(loops=0, maxtime=0, fade_ms=0)
        last_key = user_input
        print("last key changed " + last_key)
    return last_key


def load_sounds(musical_instrument):
    array = {
        '1': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'A.wav')),
        '2': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'A1.wav')),
        '3': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'A2.wav')),
        '4': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'C.wav')),
        '5': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'C1.wav')),
        '6': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'C2.wav')),
        '7': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'C3.wav')),
        '8': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'D.wav')),
        '9': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'D1.wav')),
        '0': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'D2.wav')),
        'Q': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'E.wav')),
        'W': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'E1.wav')),
        'E': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'E2.wav')),
        'R': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'F.wav')),
        'T': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'F1.wav')),
        'Y': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'F2.wav')),
        'U': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'G.wav')),
        'I': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'G1.wav')),
        'O': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'G2.wav')),
        'P': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'H.wav')),
        'A': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'H1.wav')),
        'S': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'H2.wav'))
    }
    return array


def main():
    pygame.mixer.init()
    musical_instrument = raw_input("Choose musical instrument: ")
    array = load_sounds(musical_instrument)
    last_key = 'last_key'
    while True:
        last_key = get_user_input(array, last_key)


if __name__ == "__main__":
    main()

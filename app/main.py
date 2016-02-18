import pygame
import pygame.constants
import os
import getch
from tkinter import *
from tkFont import Font


class Harp:
    def __init__(self):
        pygame.mixer.init()
        self.last_key = 'last_key'
        self.array = self.load_sounds("Bass")
        self.main_window = Tk()
        self.menu = ["Menu", "Bass", "Church", "Glitch", "Glow", "Iron", "Techno", "Steal", "Violin"]

    def get_user_input(self, array, last_key):
        user_input = getch.Getch().__call__()
        return self.play_sound(array.get(user_input), user_input, last_key)

    def play_sound(self, sound, user_input, last_key):
        if not pygame.mixer.get_busy() or not user_input == last_key:
            sound.play(loops=0, maxtime=0, fade_ms=0)
            self.last_key = user_input
        return last_key

    @staticmethod
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

    def create_window(self):
        items_font = Font(family="Sans", size=-55)
        side_menu = Listbox(self.main_window, selectmode=EXTENDED, height=20, width=10, bg='#3f51b5', foreground="white",
                        font=items_font)

        for x in range(0, len(self.menu)):
            side_menu.insert(x, "  " + self.menu[x])

        side_menu.itemconfig(0, {'bg': 'green'})

        side_menu.grid(row=0, column=0)
        logo_image = PhotoImage(file=os.path.join("images", "GDG_logo.png"))
        logo_label = Label(self.main_window, image=logo_image)
        logo_label.grid(row=0, column=1, sticky=N)

        width = self.main_window.winfo_screenwidth()
        height = self.main_window.winfo_screenheight()
        self.main_window.geometry(str(width) + "x" + str(height))
        self.main_window.bind("<Key>", lambda event:
        self.play_sound(self.array.get(str(event.char)), str(event.char), self.last_key))
        self.main_window.mainloop()


if __name__ == "__main__":
    harp = Harp()
    harp.create_window()

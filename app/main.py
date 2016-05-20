import os
import pygame
from tkFont import Font
import pygame.constants
from tkinter import *


class Harp:
    def __init__(self):
        pygame.mixer.init()
        self.last_key = 'last_key'
        self.sounds = self.load_sounds("Bass")
        self.main_window = Tk()
        self.menu = ["Menu", "Bass", "Church", "Glitch", "Glow", "Iron", "Techno", "Steal", "Violin"]
        self.empty = PhotoImage(file="images/notes/empty.png")
        self.note_images = {
            "g": PhotoImage(file="images/notes/second-line.png"),
            "a": PhotoImage(file="images/notes/second-line.png")
        }
        self.notes = []
        self.labels = [
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0)
        ]

    def play_sound(self, sound, user_input):
        self.notes.append(user_input)
        self.rerender_notes()
        if not pygame.mixer.get_busy():
            sound.play(loops=0, maxtime=0, fade_ms=0)
            self.last_key = user_input

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
            'U': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'test.wav')),
            'I': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'G1.wav')),
            'O': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'G2.wav')),
            'P': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'H.wav')),
            'A': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'H1.wav')),
            'S': pygame.mixer.Sound(os.path.join('../', 'sounds', musical_instrument, 'H2.wav'))
        }
        return array

    def add_empty_stave(self):
        padding = 75
        for label in self.labels:
            label.grid(row=0, column=1, sticky=NW, padx=(padding, 0), pady=(650, 0))
            padding += 130

    def create_window(self):
        self.items_font = Font(family="Sans", size=-55)
        self.instruments_font = Font(family="Sans", size=-250)

        self.note_label = Label(self.main_window, text="a", font=self.instruments_font, foreground='#7d7d7d')
        self.note_label.grid(row=0, column=1, sticky=NW, padx=(50, 0), pady=(300, 0))

        self.instrument_label = Label(self.main_window, font=self.instruments_font, foreground='#7d7d7d', borderwidth=0,
                                      highlightthickness=0)
        self.instrument_label.grid(row=0, column=1, sticky=NW, padx=(660, 0), pady=(350, 0))
        self.side_menu = Listbox(self.main_window, selectmode=EXTENDED, height=20, width=10, bg='#3f51b5',
                                 foreground="white",
                                 font=self.items_font)

        for x in range(0, len(self.menu)):
            self.side_menu.insert(x, "  " + self.menu[x])

        self.side_menu.itemconfig(0, {'bg': 'green'})
        self.side_menu.bind("<<ListboxSelect>>", lambda event: self.instrument_label.config(text=event.widget.get(event.widget.curselection()[0]).strip()[:1]))
        self.side_menu.grid(row=0, column=0)

        self.add_empty_stave()

        logo_image = PhotoImage(file=os.path.join("images", "GDG_logo.png"))
        logo_label = Label(self.main_window, image=logo_image)
        logo_label.grid(row=0, column=1, sticky=N)

        width = self.main_window.winfo_screenwidth()
        height = self.main_window.winfo_screenheight()
        self.main_window.geometry(str(width) + "x" + str(height))
        self.main_window.bind("<Key>", lambda event: self.play_sound(self.sounds.get(str(event.char)), str(event.char)))
        self.main_window.mainloop()

    def rerender_notes(self):
        a = 0
        b = 0
        if len(self.notes) > len(self.labels):
            b = len(self.notes) - len(self.labels)
        while True:
            self.labels[a].configure(image=self.note_images.get(self.notes[b]))
            a += 1
            b += 1
            if b == len(self.notes):
                break
        padding = 75
        for label in self.labels:
            label.grid(row=0, column=1, sticky=NW, padx=(padding, 0), pady=(650, 0))
            padding += 130


if __name__ == "__main__":
    harp = Harp()
    harp.create_window()

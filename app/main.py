import os
import pygame
from tkFont import Font
from sound_player import *
from tkinter import *


class Harp:
    def __init__(self):
        self.last_key = 'last_key'
        self.musical_instrument = "Bass"
        self.main_window = Tk()
        self.menu = ["Menu", "Bass", "Church", "Glitch", "Glow", "Iron", "Techno", "Steal", "Violin"]
        self.empty = PhotoImage(file="images/notes/empty.png")
        self.note_images = {
            "1": PhotoImage(file="images/notes/second-space-bass.png"),
            "2": PhotoImage(file="images/notes/third-line-bass.png"),
            "3": PhotoImage(file="images/notes/third-space-bass.png"),
            "4": PhotoImage(file="images/notes/fourth-line-bass.png"),
            "5": PhotoImage(file="images/notes/fourth-space-bass.png"),
            "6": PhotoImage(file="images/notes/fifth-line-bass.png"),
            "7": PhotoImage(file="images/notes/first-overspace-bass.png"),
            "8": PhotoImage(file="images/notes/first-subline.png"),
            "9": PhotoImage(file="images/notes/first-subspace.png"),
            "0": PhotoImage(file="images/notes/first-line.png"),
            "Q": PhotoImage(file="images/notes/first-space.png"),
            "W": PhotoImage(file="images/notes/second-line.png"),
            "E": PhotoImage(file="images/notes/second-space.png"),
            "R": PhotoImage(file="images/notes/third-line.png"),
            "T": PhotoImage(file="images/notes/third-space.png"),
            "Y": PhotoImage(file="images/notes/fourth-line.png"),
            "U": PhotoImage(file="images/notes/fourth-space.png"),
            "I": PhotoImage(file="images/notes/fifth-line.png"),
            "O": PhotoImage(file="images/notes/first-overspace.png"),
            "P": PhotoImage(file="images/notes/first-overline.png"),
            "A": PhotoImage(file="images/notes/second-overspace.png"),
            "S": PhotoImage(file="images/notes/second-overline.png")
        }
        self.notes_keys = {
            "1": "C",
            "2": "D",
            "3": "E",
            "4": "F",
            "5": "G",
            "6": "A",
            "7": "H",
            "8": "C1",
            "9": "D1",
            "0": "E1",
            "Q": "F1",
            "W": "G1",
            "E": "A1",
            "R": "H1",
            "T": "C2",
            "Y": "D2",
            "U": "E2",
            "I": "F2",
            "O": "G2",
            "P": "A2",
            "A": "H2",
            "S": "C3"
        }
        self.keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
                     "A", "S"]
        self.notes = []
        self.notes_playing = 0
        self.played_sounds = []
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
        self.load_sounds()

    def load_sounds(self):
        self.sounds = {
            "1": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C.wav'), 0),
            "2": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'D.wav'), 1),
            "3": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'E.wav'), 2),
            "4": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'F.wav'), 3),
            "5": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'G.wav'), 4),
            "6": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'A.wav'), 5),
            "7": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'H.wav'), 6),
            "8": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C1.wav'), 7),
            "9": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'D1.wav'), 8),
            "0": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'E1.wav'), 9),
            "Q": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'F1.wav'), 10),
            "W": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'G1.wav'), 11),
            "E": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'A1.wav'), 12),
            "R": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'H1.wav'), 13),
            "T": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C2.wav'), 14),
            "Y": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'D2.wav'), 15),
            "U": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'E2.wav'), 16),
            "I": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'F2.wav'), 17),
            "O": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'G2.wav'), 18),
            "P": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'A2.wav'), 19),
            "A": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'H2.wav'), 20),
            "S": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C3.wav'), 21)
        }

    def play_sound(self, sound, user_input):
        if user_input in self.keys:
            self.notes.append(user_input)
            self.note_label.__setitem__("text", self.notes_keys.get(user_input))
            self.rerender_notes()
            self.notes_playing += 1
            if self.notes_playing >= 10:
                self.played_sounds[0].player.stop()
                self.played_sounds[0].player.delete()
                self.played_sounds[0].sound.delete()
                self.played_sounds[0].listener.delete()
                self.played_sounds.remove(self.played_sounds[0])
                self.notes_playing -= 1
            self.played_sounds.append(self.sounds.get(user_input))
            self.sounds.get(user_input).play()

    def add_empty_stave(self):
        padding = 75
        for label in self.labels:
            label.grid(row=0, column=1, sticky=NW, padx=(padding, 0), pady=(650, 0))
            padding += 130

    def create_window(self):
        self.items_font = Font(family="Sans", size=-55)
        self.instruments_font = Font(family="Sans", size=-250)

        self.note_label = Label(self.main_window, text="", font=self.instruments_font, foreground='#7d7d7d')
        self.note_label.grid(row=0, column=1, sticky=NW, padx=(50, 0), pady=(300, 0))

        self.instrument_label = Label(self.main_window, font=self.instruments_font, foreground='#7d7d7d', borderwidth=0,
                                      highlightthickness=0, text=self.musical_instrument[:1])
        self.instrument_label.grid(row=0, column=1, sticky=NW, padx=(660, 0), pady=(350, 0))
        self.side_menu = Listbox(self.main_window, selectmode=EXTENDED, height=20, width=10, bg='#3f51b5',
                                 foreground="white",
                                 font=self.items_font)

        for x in range(0, len(self.menu)):
            self.side_menu.insert(x, "  " + self.menu[x])

        self.side_menu.itemconfig(0, {'bg': '#4c5fea'})
        self.side_menu.bind("<<ListboxSelect>>", lambda event: self.instrument_changed(
            event.widget.get(event.widget.curselection()[0]).strip()))
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

    def instrument_changed(self, new_instrument):
        if not new_instrument == "Menu":
            self.musical_instrument = new_instrument
            self.instrument_label.config(text=new_instrument[:1])
            self.load_sounds()

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

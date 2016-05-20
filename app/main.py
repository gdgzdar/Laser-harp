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
        self.note_label.__setitem__("text", self.notes_keys.get(user_input))
        self.rerender_notes()

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

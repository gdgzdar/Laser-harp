from tkFont import Font
import alsaaudio
try:
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from sound_player import *


class Dialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.top.geometry("%dx%d%+d%+d" % (500, 100, 250, 125))

        variable = StringVar(top)
        variable.set("a")

        OptionMenu(top, variable, "a", "b").grid(row=0)

        self.e1 = Entry(top)

        self.e1.grid(row=0, column=1)
        b = Button(top, text="OK", command=self.ok)
        b.grid(row=2, columnspan=2)

    def ok(self):
        self.top.destroy()


class Harp:
    def __init__(self):
        self.last_key = 'last_key'
        self.musical_instrument = "Bass"
        self.main_window = Tk()
        self.menu = ["Menu", "Bass", "Church", "Glitch", "Glow", "Iron", "Techno", "Steal", "Violin"]
        self.empty = PhotoImage(file="images/notes/empty.png")
        self.note_images = {
            "Q": PhotoImage(file=os.path.join('images', 'notes', 'second-space-bass.png')),
            "W": PhotoImage(file=os.path.join('images', 'notes', 'third-line-bass.png')),
            "E": PhotoImage(file=os.path.join('images', 'notes', 'third-space-bass.png')),
            "R": PhotoImage(file=os.path.join('images', 'notes', 'fourth-line-bass.png')),
            "T": PhotoImage(file=os.path.join('images', 'notes', 'fourth-space-bass.png')),
            "Y": PhotoImage(file=os.path.join('images', 'notes', 'fifth-line-bass.png')),
            "U": PhotoImage(file=os.path.join('images', 'notes', 'first-overspace-bass.png')),
            "I": PhotoImage(file=os.path.join('images', 'notes', 'first-subline.png')),
            "O": PhotoImage(file=os.path.join('images', 'notes', 'first-subspace.png')),
            "P": PhotoImage(file=os.path.join('images', 'notes', 'first-line.png')),
            "[": PhotoImage(file=os.path.join('images', 'notes', 'first-space.png')),
            "A": PhotoImage(file=os.path.join('images', 'notes', 'second-line.png')),
            "S": PhotoImage(file=os.path.join('images', 'notes', 'second-space.png')),
            "D": PhotoImage(file=os.path.join('images', 'notes', 'third-line.png')),
            "F": PhotoImage(file=os.path.join('images', 'notes', 'third-space.png')),
            "G": PhotoImage(file=os.path.join('images', 'notes', 'fourth-line.png')),
            "H": PhotoImage(file=os.path.join('images', 'notes', 'fourth-space.png')),
            "J": PhotoImage(file=os.path.join('images', 'notes', 'fifth-line.png')),
            "K": PhotoImage(file=os.path.join('images', 'notes', 'first-overspace.png')),
            "L": PhotoImage(file=os.path.join('images', 'notes', 'first-overline.png')),
            ";": PhotoImage(file=os.path.join('images', 'notes', 'second-overspace.png')),
            "'": PhotoImage(file=os.path.join('images', 'notes', 'second-overline.png'))
        }
        self.notes_keys = {
            "Q": "C",
            "W": "D",
            "E": "E",
            "R": "F",
            "T": "G",
            "Y": "A",
            "U": "H",
            "I": "C1",
            "O": "D1",
            "P": "E1",
            "[": "F1",
            "A": "G1",
            "S": "A1",
            "D": "H1",
            "F": "C2",
            "G": "D2",
            "H": "E2",
            "J": "F2",
            "K": "G2",
            "L": "A2",
            ";": "H2",
            "'": "C3"
        }
        self.keys = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "A", "S", "D", "F", "G", "H", "J", "K", "L",
                     ";", "'"]
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
        self.instrument_images = {
            "Bass": PhotoImage(file=os.path.join('images', 'instruments', 'bass.png')),
            "Church": PhotoImage(file=os.path.join('images', 'instruments', 'church.png')),
            "Glitch": PhotoImage(file=os.path.join('images', 'instruments', 'glitch.png')),
            "Glow": PhotoImage(file=os.path.join('images', 'instruments', 'glow.png')),
            "Iron": PhotoImage(file=os.path.join('images', 'instruments', 'iron.png')),
            "Steal": PhotoImage(file=os.path.join('images', 'instruments', 'steal.png')),
            "Techno": PhotoImage(file=os.path.join('images', 'instruments', 'techno.png')),
            "Violin": PhotoImage(file=os.path.join('images', 'instruments', 'violin.png'))
        }
        self.load_sounds()

    def load_sounds(self):
        self.sounds = {
            "Q": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C.wav'), 0),
            "W": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'D.wav'), 1),
            "E": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'E.wav'), 2),
            "R": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'F.wav'), 3),
            "T": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'G.wav'), 4),
            "Y": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'A.wav'), 5),
            "U": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'H.wav'), 6),
            "I": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C1.wav'), 7),
            "O": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'D1.wav'), 8),
            "P": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'E1.wav'), 9),
            "[": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'F1.wav'), 10),
            "A": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'G1.wav'), 11),
            "S": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'A1.wav'), 12),
            "D": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'H1.wav'), 13),
            "F": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C2.wav'), 14),
            "G": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'D2.wav'), 15),
            "H": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'E2.wav'), 16),
            "J": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'F2.wav'), 17),
            "K": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'G2.wav'), 18),
            "L": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'A2.wav'), 19),
            ";": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'H2.wav'), 20),
            "'": Sound(os.path.join('../', 'sounds', self.musical_instrument, 'C3.wav'), 21)
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

        self.instrument_label = Label(self.main_window, image=self.instrument_images.get("Bass"))
        self.instrument_label.grid(row=0, column=1, sticky=E, padx=(0, 700), pady=(0, 400))
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

        self.sound_scale = Scale(self.main_window, from_=100, to=0, orient=VERTICAL, activebackground="#4c5fea")
        self.sound_scale.set(50)
        self.scale_changed()
        self.sound_scale.configure(command=self.check_scale(self.sound_scale.get()))
        self.sound_scale.grid(row=0, column=1, sticky=E, padx=(0, 200), pady=(0, 350))

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
            self.instrument_label.config(image=self.instrument_images.get(new_instrument))
            self.load_sounds()
        else:
            dialog = Dialog(self.main_window)
            self.main_window.wait_window(dialog.top)

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

    def check_scale(self, last):
        if not last == self.sound_scale.get():
            last = self.sound_scale.get()
            self.scale_changed()
        self.main_window.after(500, self.check_scale, last)

    def scale_changed(self):
        try:
            from subprocess import call
            call(["amixer", "-D", "pulse", "sset", "Master", str(self.sound_scale.get()) + "%"])
            print(self.sound_scale.get())
        except ImportError:
            print("Windows")


if __name__ == "__main__":
    harp = Harp()
    harp.create_window()

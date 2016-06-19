from tkFont import Font
<<<<<<< Updated upstream
from PIL import Image, ImageTk
=======
>>>>>>> Stashed changes

try:
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
from sound_player import *


class Dialog:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        top.resizable(width=tk.FALSE, height=tk.FALSE)

        variable = tk.StringVar(top)
        variable.set("a")

        tk.Label(top, text="Arduino on port: ", font=Font(family="Sans", size=-55), foreground='#7d7d7d').grid(row=0,
                                                                                                               column=0)
        dropdown = tk.OptionMenu(top, variable, "a", "b")
        dropdown.config(font=Font(family="Sans", size=-55))
        dropdown.config(bg="#3f51b5")
        dropdown.config(foreground="white")
        dropdown.config(activeforeground="white")
        dropdown.config(activebackground="#3f51b5")
        dropdown.grid(row=0, column=1)
        button = tk.Button(top, text="OK", command=self.ok)
        button.config(bg="#3f51b5")
        button.config(foreground="white")
        button.config(activeforeground="white")
        button.config(activebackground="#3f51b5")
        button.config(font=Font(family="Sans", size=-55))
        button.grid(row=1, column=0, columnspan=2)

    def ok(self):
        self.top.destroy()


class Harp:
    def __init__(self):
        self.last_key = 'last_key'
        self.musical_instrument = "Bass"
        self.main_window = tk.Tk()
        self.width = 1280#self.main_window.winfo_screenwidth()
        self.height = 800#self.main_window.winfo_screenheight()
        self.menu = ["Menu", "Bass", "Church", "Glitch", "Glow", "Iron", "Techno", "Steal", "Violin"]
        empty_image = Image.open("images/notes/empty.png").resize(
            (int(0.06770833333 * self.width + 1), int(0.363888889 * self.height)))
        self.empty = ImageTk.PhotoImage(empty_image)
        self.path_to_notes = [
            os.path.join('images', 'notes', 'second-space-bass.png'),
            os.path.join('images', 'notes', 'third-line-bass.png'),
            os.path.join('images', 'notes', 'third-space-bass.png'),
            os.path.join('images', 'notes', 'fourth-line-bass.png'),
            os.path.join('images', 'notes', 'fourth-space-bass.png'),
            os.path.join('images', 'notes', 'fifth-line-bass.png'),
            os.path.join('images', 'notes', 'first-overspace-bass.png'),
            os.path.join('images', 'notes', 'first-subline.png'),
            os.path.join('images', 'notes', 'first-subspace.png'),
            os.path.join('images', 'notes', 'first-line.png'),
            os.path.join('images', 'notes', 'first-space.png'),
            os.path.join('images', 'notes', 'second-line.png'),
            os.path.join('images', 'notes', 'second-space.png'),
            os.path.join('images', 'notes', 'third-line.png'),
            os.path.join('images', 'notes', 'third-space.png'),
            os.path.join('images', 'notes', 'fourth-line.png'),
            os.path.join('images', 'notes', 'fourth-space.png'),
            os.path.join('images', 'notes', 'fifth-line.png'),
            os.path.join('images', 'notes', 'first-overspace.png'),
            os.path.join('images', 'notes', 'first-overline.png'),
            os.path.join('images', 'notes', 'second-overspace.png'),
            os.path.join('images', 'notes', 'second-overline.png')
        ]
        self.keys = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "A", "S", "D", "F", "G", "H", "J", "K", "L",
                     ";", "'"]
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
        self.note_images = {
        }
        i = 0
        for key in self.keys:
            empty_image = Image.open(self.path_to_notes[i]).resize(
                (int(0.06770833333 * self.width + 1), int(0.363888889 * self.height)))
            self.note_images[key] = ImageTk.PhotoImage(empty_image)
            i += 1
        self.notes = []
        self.notes_playing = 0
        self.played_sounds = []
        self.labels = [
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0),
            tk.Label(self.main_window, image=self.empty, borderwidth=0, highlightthickness=0)
        ]
        self.instrument_images = {
            "Bass": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'bass.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height)))),
            "Church": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'church.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height)))),
            "Glitch": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'glitch.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height)))),
            "Glow": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'glow.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height)))),
            "Iron": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'iron.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height)))),
            "Steal": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'steal.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height)))),
            "Techno": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'techno.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height)))),
            "Violin": ImageTk.PhotoImage(Image.open(os.path.join('images', 'instruments', 'violin.png')).resize(
                (int(0.0984375 * self.width), int(0.125 * self.height))))
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
        if user_input in self.note_images.keys():
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
        padding = 0.0390625 * self.width
        for label in self.labels:
            label.grid(row=0, column=1, sticky=tk.NW, padx=(padding, 0), pady=(0.60185185185 * self.height, 0))
            padding += 0.06770833333 * self.width

    def create_window(self):
        self.items_font = Font(family="Sans", size=-int(self.height * 0.05092592593))
        self.notes_font = Font(family="Sans", size=-int(self.height * 0.23148148148))

        self.note_label = tk.Label(self.main_window, text="", font=self.notes_font, foreground='#7d7d7d')
        self.note_label.grid(row=0, column=1, sticky=tk.NW, padx=(int(self.width * 0.02604166667), 0),
                             pady=(int(self.height * 0.27777777778), 0))

        self.instrument_label = tk.Label(self.main_window, image=self.instrument_images.get("Bass"))
        self.instrument_label.grid(row=0, column=1, sticky=tk.NE, padx=(0, int(self.width * 0.3125)),
                                   pady=(int(self.height * 0.34722222222), 0))
        self.side_menu = tk.Listbox(self.main_window, selectmode=tk.EXTENDED, height=20, width=10, bg='#3f51b5',
                                    foreground="white",
                                    font=self.items_font, borderwidth=0, highlightthickness=0)

        for x in range(0, len(self.menu)):
            self.side_menu.insert(x, "  " + self.menu[x])

        self.side_menu.itemconfig(0, {'bg': '#4c5fea'})
        self.side_menu.bind("<<ListboxSelect>>", lambda event: self.instrument_changed(
            event.widget.get(event.widget.curselection()[0]).strip()))
        self.side_menu.grid(row=0, column=0)

        self.add_empty_stave()

        self.sound_scale = tk.Scale(self.main_window, from_=100, to=0, orient=tk.VERTICAL, activebackground="#4c5fea")
        self.sound_scale.set(50)
        self.scale_changed()
        self.sound_scale.configure(command=self.check_scale(self.sound_scale.get()))
        self.sound_scale.grid(row=0, column=1, sticky=tk.NE, padx=(0, int(self.width * 0.05989583333)),
                              pady=(int(self.height * 0.37037037037), 0))

        logo_image = ImageTk.PhotoImage(Image.open(os.path.join("images", "GDG_logo.png")).resize(
            (int(0.78177083333 * self.width), int(0.24166666667 * self.height))))
        logo_label = tk.Label(self.main_window, image=logo_image)
        logo_label.grid(row=0, column=1, sticky=tk.N)

        self.main_window.geometry(str(self.width) + "x" + str(self.height))
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
        padding = 0.0390625 * self.width
        for label in self.labels:
            label.grid(row=0, column=1, sticky=tk.NW, padx=(padding, 0), pady=(0.60185185185 * self.height, 0))
            padding += 0.06770833333 * self.width

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

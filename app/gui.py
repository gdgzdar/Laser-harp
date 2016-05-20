from tkFont import Font

from Tkinter import *

main_window = Tk()

musical_instruments = ["Menu", "Bass", "Church", "Glitch", "Glow", "Iron", "Techno", "Steal", "Violin"]

image = PhotoImage(file="images/notes/a.png")
empty = PhotoImage(file="images/notes/empty.png")

notes = []

images = {
    "g": PhotoImage(file="images/notes/g.png"),
    "a": PhotoImage(file="images/notes/a.png")
}

labels = [
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0),
    Label(main_window, image=empty, borderwidth=0, highlightthickness=0)
]


def callback(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index).strip()
    instrument_label.config(text=value[:1])


def rerender_notes():
    for x in range(0, len(notes)):
        labels[x].configure(image=images.get(notes[x]))
    padding = 75
    for label in labels:
        label.grid(row=0, column=1, sticky=NW, padx=(padding, 0), pady=(700, 0))
        padding += 130


def key(event):
    notes.append(str(event.char))
    rerender_notes()

items_font = Font(family="Sans", size=-55)

photo = PhotoImage(file="images/GDG_logo.png")
label = Label(main_window, image=photo)
label.grid(row=0, column=1, sticky=N)

sound_listbox = Listbox(main_window, selectmode=EXTENDED, height=20, width=10, bg='#3f51b5', foreground="white",
                        font=items_font)

for x in range(0, len(musical_instruments)):
    sound_listbox.insert(x, "  " + musical_instruments[x])

sound_listbox.itemconfig(0, {'bg': 'green'})

sound_listbox.bind("<<ListboxSelect>>", callback)

sound_listbox.grid(row=0, column=0)

instruments_font = Font(family="Sans", size=-250)

note_label = Label(main_window, text="a", font=instruments_font, foreground='#7d7d7d')
note_label.grid(row=0, column=1, sticky=NW, padx=(50, 0), pady=(300, 0))

instrument_label = Label(main_window, font=instruments_font, foreground='#7d7d7d', borderwidth=0, highlightthickness=0)
instrument_label.grid(row=0, column=1, sticky=NW, padx=(660, 0), pady=(350, 0))

padding = 75
for label in labels:
    label.grid(row=0, column=1, sticky=NW, padx=(padding, 0), pady=(700, 0))
    padding += 130

width = main_window.winfo_screenwidth()
height = main_window.winfo_screenheight()

main_window.geometry(str(width) + "x" + str(height))
main_window.bind("<Key>", key)
main_window.mainloop()

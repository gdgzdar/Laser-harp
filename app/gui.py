from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class Harp(Widget):
    first_part_of_stave = ObjectProperty(None)
    second_part_of_stave = ObjectProperty(None)
    third_part_of_stave = ObjectProperty(None)
    fourth_part_of_stave = ObjectProperty(None)
    fifth_part_of_stave = ObjectProperty(None)
    sixth_part_of_stave = ObjectProperty(None)
    seventh_part_of_stave = ObjectProperty(None)
    eighth_part_of_stave = ObjectProperty(None)
    ninth_part_of_stave = ObjectProperty(None)
    tenth_part_of_stave = ObjectProperty(None)
    eleventh_part_of_stave = ObjectProperty(None)
    twelfth_part_of_stave = ObjectProperty(None)
    notes_positions = {
        "C":  "third-line-bass",
        "D":  "third-space-bass",
        "E":  "fourht-line-bass",
        "F":  "fourht-space-bass",
        "G":  "fifth-line-bass",
        "H":  "first-overspace-bass",
        "C1":  "first-subline",
        "D1":  "first-subspace",
        "E1":  "first-line",
        "F1":  "first-space",
        "G1":  "second-line",
        "A1":  "second-space",
        "H1": "third-line",
        "C2": "third-space",
        "D2": "fourth-line",
        "E2": "fourth-space",
        "F2": "fifth-line",
        "G2": "first-overspace",
        "A2": "first-overline",
        "H3": "second-overspace",
        "C3": "second-overline"
    }


    def init_stave(self):
        self.stave = [
            self.first_part_of_stave, self.second_part_of_stave, self.third_part_of_stave, self.fourth_part_of_stave,
            self.fifth_part_of_stave, self.sixth_part_of_stave, self.seventh_part_of_stave, self.eighth_part_of_stave,
            self.ninth_part_of_stave, self.tenth_part_of_stave, self.eleventh_part_of_stave, self.twelfth_part_of_stave
        ]
        self.notes_played = []
        self.tone_played('G1')
        self.tone_played('D1')
        self.tone_played('F1')
        self.tone_played('D1')
        self.tone_played('E1')
        self.tone_played('H1')
        self.tone_played('C1')
        self.tone_played('G1')
        self.tone_played('C1')
        self.tone_played('H1')
        self.tone_played('C1')
        self.tone_played('A1')
        self.tone_played('G1')

    def tone_played(self, tone):
        self.notes_played.append(tone)
        self.rerender_stave(self.notes_positions[tone])

    def rerender_stave(self, position):
        for x in range(0, len(self.stave) - 1):
           self.stave[x].source = self.stave[x + 1].source
        self.stave[len(self.stave) - 1].source = "images/notes/" + position +".png"


class HarpApp(App):
    def build(self):
        harp = Harp()
        harp.init_stave()
        return harp


if __name__ == '__main__':
    HarpApp().run()

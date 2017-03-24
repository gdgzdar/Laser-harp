from kivy.app import App
from kivy.uix.widget import Widget

class InstrumentsList(Widget):
    pass


class HarpApp(App):
    def build(self):
        return InstrumentsList()


if __name__ == '__main__':
    HarpApp().run()
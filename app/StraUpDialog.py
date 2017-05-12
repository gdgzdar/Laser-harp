from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from audio import Reader
from kivy.uix.anchorlayout import AnchorLayout

# create a dropdown with 10 buttons
Builder.load_file('portsdropdown.kv')
class PortsDropDown(DropDown):
    pass

dropdown = DropDown()
list_of_ports = Reader.get_available_ports()


for i in range(len(list_of_ports)):
    btn = Button(text= list_of_ports[i], size_hint_y=None, height=44)
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)
    
mainbutton = Button(text='Select port', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

layout = AnchorLayout(
    anchor_x='center', anchor_y='top')
layout.add_widget(mainbutton)

runTouchApp(layout)

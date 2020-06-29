from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from grid import GridRow
import requests
import json

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass



GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

    def on_start(self):
        grid_row = self.root.ids['home_screen'].ids['grid_row']
        for row in range(0,5):
            r = GridRow(shit="shit")
            grid_row.add_widget(r)

MainApp().run()

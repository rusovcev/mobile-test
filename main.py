from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from functools import partial
from grid import Grid
import requests
import json
import os

class HomeScreen(Screen):
    pass

class TabScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    favourites = []

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        return GUI

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

    def on_start(self):
        if os.path.exists("favorites.json"):
            with open("favorites.json", "r") as favFile:
                self.favourites = json.load(favFile)
        # self.test()
        # self.get_coinmarketcap()
        self.test2()

    def test(self):
        #  grid_row = self.root.ids['home_screen'].ids['grid_row']
        grid_row = self.root.ids['tab_screen'].ids['grid_row']
        for row in range(0, 8):
            r = Grid(left_label_text="foo", right_label_text="bar")
            grid_row.add_widget(r)
        test_label = self.root.ids['home_screen'].ids['home_screen_top_label']
        test_label.text = "TEST!"

    def test2(self):
        grid_row = self.root.ids['tab_screen'].ids['grid_main']
        for row in range(10):
            leftImage = Image(
                source="images/icons/bitcoin.png", 
                size_hint=(.45, 1),
                pos_hint={"top": 1, "left": .1})

            leftLabel = Label(
                text="left text", 
                size_hint=(1, .5),
                pos_hint={"top": 1, "left": .5},
                color=get_color_from_hex("#0f0f0fff"))
            
            favBtn = ImageButton(
                source="images/icons/001-star.png",
                size=(10, 10),
                on_release=partial(self.set_favourite, "fav {}".format(row)))

            grid_row.add_widget(leftImage)
            grid_row.add_widget(leftLabel)
            grid_row.add_widget(favBtn)
    
    def set_favourite(self, favId, widget):
        print(favId)

    def get_coinmarketcap(self):
        apiUrl = "https://sandbox-api.coinmarketcap.com/v1/"
        service = "cryptocurrency/listings/latest"
        params = {"start": '1', "limit": "10", "convert": "USD"}
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": "9620bdd8-06ca-4b7d-9847-c0c68b5f36a7",}

        req = requests.get(apiUrl + service, params=params, headers=headers)
        if req.status_code == 200:
            # print(req.text)
            res = json.loads(req.text)
            test_label = self.root.ids['home_screen'].ids['home_screen_top_label']
            test_label.text = res['status']['timestamp']
            grid_row = self.root.ids['home_screen'].ids['grid_row']
            scroll_view = self.root.ids['home_screen'].ids['scroll_view']
            for item in res['data']:
                row = Grid(left_label_text=item['name'], right_label_text=str(item['quote']['USD']['price']))
                grid_row.add_widget(row)

    def on_request_close(self, *args):
        self.textpopup(title='Exit', text='Are you sure?')
        return True

    def textpopup(self, title='', text=''):
        """Open the pop-up with the name.

        :param title: title of the pop-up to open
        :type title: str
        :param text: main text of the pop-up to open
        :type text: str
        :rtype: None
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='OK', size_hint=(1, 0.25))
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
        mybutton.bind(on_release=self.stop)
        popup.open()
MainApp().run()

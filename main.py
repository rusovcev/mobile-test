from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from grid import Grid
import requests
import json

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
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

    def on_start(self):
        for root_id in self.root.ids:
            for screen_id in self.root.ids[root_id].ids:
                print(screen_id)
                for item in self.root.ids[root_id].ids[screen_id].ids:
                    print("\t", item)
        self.test()
        # self.get_coinmarketcap()
        pass

    def test(self):
        # grid_row = self.root.ids['home_screen'].ids['grid_row']
        grid_row = self.root.ids['tab_screen'].ids['grid_row']
        for row in range(0, 8):
            r = Grid(left_label_text="foo", right_label_text="bar")
            grid_row.add_widget(r)
        test_label = self.root.ids['home_screen'].ids['home_screen_top_label']
        test_label.text = "TEST!"
    
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


MainApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.graphics import Line, Color
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from grid import GridAll, MyGrid, TestGrid
import requests
import json
import os

# class TabScreen(Screen):
#     pass

class HomeScreen(Screen):
    pass

class TestScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):

    def build(self):
        return GUI

    def on_start(self):
        all_button = self.root.ids["test_screen"].ids["all_button"]
        all_button.active = True

        if os.path.exists("all.json"):
            with open("all.json", "r") as fp:
                self.all = json.load(fp)
            print("ALL-COINS loaded from local file...")
        else:
            cmcap = self.get_coinmarketcap()
            print("COINS list retrieved from the internet...")
            if cmcap is not False:
                self.all = cmcap
                with open("all.json", "w") as fp:
                    json.dump(self.all, fp)
                print("ALL-COINS list saved to local file...")
            else:
                self.all = {"data": []}
        
        if os.path.exists("favourites.json"):
            with open("favourites.json", "r") as fp:
                self.favourites = json.load(fp)
            print("loading favourites list from local file...")
        else:
            self.favourites = list()
            print("empty favourites list initialized...")


        self.test_populate(tab="all")
        # self.populate_grid(3)
        pass
    
    def on_pause(self):
        pass

    def on_resume(self):
        # self.textpopup(title='Exit', text='Are you sure?')
        pass

    def on_stop(self):
        with open("favourites.json", "w") as fp:
            json.dump(self.favourites, fp)
        print("files saved, exiting app...")

    def get_coinmarketcap(self):
        apiUrl = "https://sandbox-api.coinmarketcap.com/v1/"
        service = "cryptocurrency/listings/latest"
        params = {"start": '1', "limit": "10", "convert": "USD"}
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": "9620bdd8-06ca-4b7d-9847-c0c68b5f36a7",}

        req = requests.get(apiUrl + service, params=params, headers=headers)

        if req.status_code == 200:
            # print(req.text)
            res = json.loads(req.text)
            return res
        return False
    
    def add_to_favourites(self, id, *args):
        self.favourites.append(id)
        self.test_populate(favourites=False)

    def remove_from_favourites(self, id, *args):
        self.favourites.remove(id)
        self.test_populate(favourites=True)


    def test_populate(self, *args, **kwargs):
        favs = kwargs.get("favourites", False)
        grid = self.root.ids['test_screen'].ids['main_grid']
        grid.clear_widgets()
        for item in self.all['data'] if not favs else [a for a in self.all['data'] if a['id'] in self.favourites]:
            g = TestGrid(item=item, is_favourite=(item['id'] in self.favourites), favourites_list=favs)
            grid.add_widget(g)

    def populate_grid(self, length):
        grid = self.root.ids['test_screen'].ids['main_grid']
        grid.clear_widgets()
        for row in range(length):
            grid_row = MyGrid(
                widgets=[
                    (
                        "50dp",
                        {"type": "image", "source": "images/icons/bitcoin.png", "size_hint": (1, 1)},
                        [
                            {"type": "label", "text": "[b]a[/b]", "font_size": 17}, 
                            {"type": "label", "text": "b"},
                            {"type": "label", "text": "c"}
                        ],
                        [
                            {"type": "label", "text": "[b]{}[/b]".format(row), "font_size": 20},
                            {"type": "label", "text": "..."},
                            {"type": "label", "text": "[i]italic[/i]"}

                        ],
                    ),
                    (
                        "20dp",
                        {"type": "label", "text": "left"},
                        {"type": "label", "text": "middle"},
                        {"type": "label", "text": "right"}
                    )
                ],
                canvas_color=get_color_from_hex("#fffffcf"),
                row_default_height="50dp"
                )
            grid.add_widget(grid_row)

    def test(self):
        grid_row = self.root.ids['home_screen'].ids['grid_all']
        for row in range(10):
            grid = GridAll(shit="happens", cols=3)
            grid_row.add_widget(grid)
            pass
    
    def checked_button(self, button):
        print(button, "pressed")
        favourites_button = self.root.ids['test_screen'].ids["favourites_button"]
        all_button = self.root.ids["test_screen"].ids["all_button"]
        if button is "favourites":
            favourites_button.active = True
            all_button.active = False
            favourites_button.text = "[b]Favourites[/b]"
            all_button.text = "All Coins"
            # favourites_button.font_size = "22dp"
            # all_button.font_size = "18dp"
            # self.populate_grid(5)
            self.test_populate(favourites=True)
                
        elif button is "all":
            favourites_button.active = False
            all_button.active = True
            favourites_button.text = "Favourites"
            all_button.text = "[b]All Coins[/b]"
            # favourites_button.font_size = "18dp"
            # all_button.font_size = "22dp"
            # self.populate_grid(10)
            self.test_populate(favourites=False)
        else:
            pass

    # def test(self):
    #     grid_row = self.root.ids['tab_screen'].ids['grid_main']
    #     for row in range(10):
    #         leftImage = Image(
    #             source="images/icons/bitcoin.png", 
    #             size_hint=(.45, 1),
    #             pos_hint={"top": 1, "left": .1})

    #         leftLabel = Label(
    #             color=(0,0,0,1),
    #             text="left text", 
    #             size_hint=(1, .5),
    #             pos_hint={"top": 1, "left": .5}
    #             )
            
    #         # favBtn = ImageButton(
    #         #     # on_release=partial(self.set_favourite, "fav {}".format(row)),
    #         #     source="images/icons/001-star.png")

    #         grid_row.add_widget(leftImage)
    #         grid_row.add_widget(leftLabel)
    #         # grid_row.add_widget(favBtn)

MainApp().run()

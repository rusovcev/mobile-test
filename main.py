from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from grid import GridAll

# class TabScreen(Screen):
#     pass

class HomeScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):

    def build(self):
        return GUI

    def on_start(self):
        self.test()
        pass
    
    def on_pause(self):
        pass

    def on_resume(self):
        # self.textpopup(title='Exit', text='Are you sure?')
        pass

    def on_stop(self):
        pass

    def test(self):
        grid_row = self.root.ids['home_screen'].ids['grid_all']
        for row in range(10):
            grid = GridAll(shit="happens", cols=3)
            grid_row.add_widget(grid)
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

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior, Button
from kivy.graphics import Line, Color
from kivy.uix.image import Image
from kivy.properties import ListProperty, BooleanProperty
from grid import GridAll

# class TabScreen(Screen):
#     pass

class HomeScreen(Screen):
    pass

class TestScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class MyButton(Button):
    line_color = ListProperty()
    active = BooleanProperty(defaultvalue=False)

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
    
    def checked_button(self, button):
        print(button, "pressed")
        favourites_button = self.root.ids['test_screen'].ids["favourites_button"]
        all_button = self.root.ids["test_screen"].ids["all_button"]
        if button is "favourites":
            favourites_button.active = True
            all_button.active = False
            favourites_button.text = "[b]FAVOURITES[/b]"
            all_button.text = "All"
            favourites_button.font_size = "22dp"
            all_button.font_size = "18dp"
            # favourites_button.background_color = (0, 0, 255, 255)
            # all_button.background_color = (255, 255, 255, 255)
                
        elif button is "all":
            favourites_button.active = False
            all_button.active = True
            favourites_button.text = "Favourites"
            all_button.text = "[b]ALL[/b]"
            favourites_button.font_size = "18dp"
            all_button.font_size = "22dp"
            # favourites_button.background_color = (255, 255, 255, 255)
            # all_button.background_color = (0, 0, 255, 255)
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

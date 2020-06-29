from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex

class GridRow(GridLayout):
    rows = 1

    def __init__(self, **kwargs):
        print(kwargs)

        super(GridRow, self).__init__()

        # with self.canvas.before:
        #     Color(rgb=(get_color_from_hex("#555555")))
        #     Rectangle(size=self.size, pos=self.pos)

        left = FloatLayout()
        image = Image(source="images/icons/" + kwargs.get("left_image", "phone.png"), size_hint=(1, .8), pos_hint={"top": 1, "left": 1})
        label = Label(text=kwargs.get("left_label", "n/a"), size_hint=(1, .2), pos_hint={"top": .1, "left": .1})
        left.add_widget(image)
        left.add_widget(label)

        middle = FloatLayout()
        image = Image(source="images/icons/" + kwargs.get("middle_image", "bitcoin.png"), size_hint=(1, .6), pos_hint={"top": 1, "left": 1})
        label = Label(text=kwargs.get("middle_label", "middle"), size_hint=(1, .1), pos_hint={"top": 1, "left": .2})
        middle.add_widget(image)
        middle.add_widget(label)

        self.add_widget(left)
        self.add_widget(middle)
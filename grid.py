from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex

class Grid(GridLayout):
    # rows = 1
    cols = 2

    def __init__(self, **kwargs):
        # print(kwargs)

        super(Grid, self).__init__()
        # with self.canvas.before:
        #     Color(rgb=(get_color_from_hex("#555555")))
        #     Rectangle(size=self.size, pos=self.pos)

        leftWidget = FloatLayout()

        leftImage = Image(
            source="images/icons/" + kwargs.get("left_image_souce", "bitcoin.png"), 
            size_hint=(.45, 1),
            pos_hint={"top": 1, "left": .1})

        leftLabel = Label(
            text=kwargs.get("left_label_text", "left text"), 
            size_hint=(1, .5),
            pos_hint={"top": 1, "left": .5},
            color=get_color_from_hex("#0f0f0fff"))

        leftWidget.add_widget(leftImage)
        leftWidget.add_widget(leftLabel)

        rightWidget = FloatLayout()

        rightImage = Image(
            source="images/icons/" + kwargs.get("right_image_source", "phone.png"), 
            size_hint=(.4, 1), 
            pos_hint={"top": 1, "right": 1})

        rightLabel = Label(
            text=kwargs.get("right_label_text", "right text"), 
            size_hint=(1, .5),
            pos_hint={"top": 1, "right": .5},
            color=get_color_from_hex("#ff0000ff")
        )

        rightWidget.add_widget(rightImage)
        rightWidget.add_widget(rightLabel)

        self.add_widget(leftWidget)
        self.add_widget(rightWidget)
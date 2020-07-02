from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.utils import get_color_from_hex

class GridAll(GridLayout):
    # cols = 3

    def __init__(self, **kwargs):
        # super(Grid, self).__init__(**kwargs)
        # super(Grid, self).__init__()
        super().__init__()

        self.cols = kwargs.get("cols", 1)
        self.rows = kwargs.get("rows", 1)

        with self.canvas.before:
            Color(rgb=(get_color_from_hex(kwargs.get("canvasColor", "#ffffff"))))
            # self.rectangle = Rectangle(size=self.size, pos=self.pos)
            self.rectangle = RoundedRectangle(size=self.size, pos=self.pos, radius=[10,])
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)

        widget = FloatLayout()

        leftImage = Image(
            source="images/icons/" + kwargs.get("left_image_souce", "bitcoin.png"), 
            size_hint=(.6, .6),
            pos_hint={"top": .8, "left": 1})
        widget.add_widget(leftImage)
        self.add_widget(widget)

        widget = FloatLayout()

        topLabel = Label(
            text=kwargs.get("left_label_text", "top"), 
            size_hint=(1, .2),
            pos_hint={"top": .9, "left": 1},
            color=get_color_from_hex("#0f0f0fff"))
        midLabel = Label(
            text=kwargs.get("left_label_text", "middle"), 
            size_hint=(1, .2),
            pos_hint={"top": .6, "left": 1},
            color=get_color_from_hex("#0f0f0fff"))
        bottomLabel = Label(
            text=kwargs.get("left_label_text", "bottom"), 
            size_hint=(1, .2),
            pos_hint={"top": .3, "left": .5},
            color=get_color_from_hex("#0f0f0fff"))

        widget.add_widget(topLabel)
        widget.add_widget(midLabel)
        widget.add_widget(bottomLabel)
        self.add_widget(widget)

        widget = FloatLayout()

        label = Label(
            text=kwargs.get("left_label_text", "action"), 
            size_hint=(1, .2),
            pos_hint={"top": .9, "left": 1},
            color=get_color_from_hex("#0f0f0fff"))
        # widget.add_widget(label)
        self.add_widget(label)



        # rightWidget = FloatLayout()

        # rightImage = Image(
        #     source="images/icons/" + kwargs.get("right_image_source", "phone.png"), 
        #     size_hint=(.4, 1), 
        #     pos_hint={"top": 1, "right": 1})

        # rightLabel = Label(
        #     text=kwargs.get("right_label_text", "right text"), 
        #     size_hint=(1, .5),
        #     pos_hint={"top": 1, "right": .5},
        #     color=get_color_from_hex("#ff0000ff")
        # )

        # rightWidget.add_widget(rightImage)
        # rightWidget.add_widget(rightLabel)

        # self.add_widget(leftWidget)
        # self.add_widget(rightWidget)
    
    def update_rectangle(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size
        self.rectangle.radius = [20,]

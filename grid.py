from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import ListProperty, BooleanProperty
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.utils import get_color_from_hex
from functools import partial

class MyButton(Button):
    line_color = ListProperty()
    active = BooleanProperty(defaultvalue=False)

# class BGLabel(Label):
#     def on_size(self, *args):
#         self.canvas.before.clear()
#         with self.canvas.before:
#             Color(0, .9, .6, .5)
#             RoundedRectangle(pos=(self.x+self.width/10, self.y), size=(self.width*2.9, self.height*1.1))

class TestGrid(GridLayout):
    rows = 1
    cols = 1
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.item = kwargs.get("item")
        self.is_favourite = kwargs.get("is_favourite")
        self.favourites_list = kwargs.get("favourites_list")
        self._app = App.get_running_app()

        with self.canvas.before:
            Color(rgba=kwargs.get("canvas_color", get_color_from_hex("#00cf7f7f")))
            # self.rectangle = RoundedRectangle(size=(200, 100), pos=(self.get_center_x()+200, self.get_center_y()*10), radius=[10,])
            self.rectangle = RoundedRectangle(size=(self.width, self.height/2), pos=(self.get_center_x()+200, self.get_center_y()*10), radius=[10,])
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)

        f = FloatLayout()

        i = Image(
            source="images/icons/bitcoin.png",
            size_hint=(.3, .5),
            pos_hint={"top": 1, "left": 1}
        )
        f.add_widget(i)

        l1 = Label(
            text="{0} ([b]{1}[/b])".format(self.item['name'], self.item['symbol']),
            color=get_color_from_hex("#000000ff"),
            font_size=20,
            markup=True,
            size_hint=(1.0, 0.1),
            # size_hint=(None, None),
            pos_hint={"top": 0.9, "left": 1.0},
            halign="left",
            valign="middle",
            text_size=(self.width*2, self.height)
        )
        f.add_widget(l1)

        l2 = Label(
            text="Price: [b]${0:,.2f}[/b]".format(self.item['quote']['USD']['price']),
            color=get_color_from_hex("#000000ff"),
            font_size=17,
            markup=True,
            size_hint=(1.0, 0.1),
            # size_hint=(None, None),
            pos_hint={"top": 0.7, "left": 1.0},
            halign="left",
            valign="middle",
            text_size=(self.width*2, self.height),
        )
        f.add_widget(l2)

        l3 = Label(
            text="Market Cap: [b]${0:,.2f}[/b]".format(self.item['quote']['USD']['market_cap']),
            color=get_color_from_hex("#000000ff"),
            font_size=11,
            markup=True,
            size_hint=(0.7, 0.1),
            # size_hint=(None, None),
            pos_hint={"top": 0.5, "left": 1.0},
            halign="left",
            valign="middle",
            text_size=(self.width*2, self.height)
        )
        f.add_widget(l3)

        # r1 = Label(
        #     text="[b]Delete[/b]",
        #     color=get_color_from_hex("#7f0000ff"),
        #     font_size=18,
        #     markup=True,
        #     size_hint=(0.2, 0.1),
        #     # size_hint=(None, None),
        #     pos_hint={"top": 1.0, "right": 1.0},
        #     halign="right",
        #     valign="middle",
        # )
        # f.add_widget(r1)

        if self.favourites_list and self.is_favourite:
            btnRemove = Button(
                size_hint=(.1, .2),
                pos_hint={"top": .99, "right": 0.95},
                markup=True,
                font_size=18,
                text="[b]Remove[/b]",
                background_color=get_color_from_hex("#00000000"),
                color=get_color_from_hex("#ff0000af"),
                background_normal="",
                background_down="",
            )
            btnRemove.bind(on_release=partial(self._app.remove_from_favourites, self.item['id']))
            f.add_widget(btnRemove)

        elif not self.favourites_list and not self.is_favourite:
            btnAdd = Button(
                size_hint=(.1, .2),
                pos_hint={"top": .99, "right": 0.95},
                markup=True,
                font_size=18,
                text="[b]Add[/b]",
                background_color=get_color_from_hex("#00000000"),
                color=get_color_from_hex("#00afffaf"),
                background_normal="",
                background_down="",
            )
            # btnAdd.bind(on_release=partial(self.add_to_favourites, self.item['id']))
            btnAdd.bind(on_release=partial(self._app.add_to_favourites, self.item['id']))
            f.add_widget(btnAdd)




        r2 = Label(
            text="Volume 24h: [b]${0:,.2f}[/b]".format(self.item['quote']['USD']['volume_24h']),
            color=get_color_from_hex("#000000ff"),
            font_size=11,
            markup=True,
            size_hint=(0.5, 0.1),
            # size_hint=(None, None),
            pos_hint={"top": 0.5, "right": 0.85},
            halign="right",
            valign="middle",
            text_size=(self.width*3, self.height),
        )
        f.add_widget(r2)

        b1 = Label(
            text="1h: {0:+.2f}%".format(self.item['quote']['USD']['percent_change_1h']),
            color=get_color_from_hex("#008f4fff"),
            font_size=16,
            markup=True,
            size_hint=(0.33, 0.20),
            # size_hint=(None, None),
            pos_hint={"top": 0.25, "left": 0.15},
            halign="justify",
            valign="middle",
        )
        # g.add_widget(b1)
        f.add_widget(b1)

        b2 = Label(
            text="24h: {0:+.2f}%".format(self.item['quote']['USD']['percent_change_24h']),
            color=get_color_from_hex("#008f4fff"),
            font_size=16,
            markup=True,
            size_hint=(1.0, 0.20),
            # size_hint=(None, None),
            pos_hint={"top": 0.25, "left": 0},
            halign="justify",
            valign="middle",
        )
        # g.add_widget(b2)
        f.add_widget(b2)

        b3 = Label(
            text="7d: {0:+.2f}%".format(self.item['quote']['USD']['percent_change_7d']),
            color=get_color_from_hex("#008f4fff"),
            font_size=16,
            markup=True,
            size_hint=(0.33, 0.2),
            # size_hint=(None, None),
            pos_hint={"top": 0.25, "right": 1.0},
            halign="justify",
            valign="middle",
        )
        # g.add_widget(b3)
        f.add_widget(b3)
        # f.add_widget(g)

        f.id = "item_" + str(self.item['id'])
        self.add_widget(f)

    def update_rectangle(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = (self.width, self.height/3.3)
        self.rectangle.radius = [20,]
    
    # def remove_from_favourites(self, id, *args):
    #     print("remove", id, "from favourites")

    # def add_to_favourites(self, id, *args):
    #     print("adding", id, "to favourites")
    #     print(self.ids)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__()
        self.rows = kwargs.get("rows", len(kwargs.get("widgets", [])))
        self.cols = kwargs.get("cols", 1)
        self.spacing = 5
        # self.row_default_height=kwargs.get("row_default_height", "20dp")
        # self.row_force_default=True

        print(self.rows, self.cols)

        if "canvas_color" in kwargs:
            with self.canvas.before:
                Color(rgba=kwargs.get("canvas_color", get_color_from_hex("#0000ff1f")))
                self.rectangle = RoundedRectangle(size=self.size, pos=self.pos, radius=[10,])
            self.bind(pos=self.update_rectangle, size=self.update_rectangle)

        widgets = kwargs.get("widgets", [])

        for item in widgets:
            if isinstance(item, tuple):
                w = MyGrid(
                    widgets=item[1:], 
                    cols=len(item), 
                    rows=1, 
                    canvas_color=get_color_from_hex("#00ff001f"),
                    row_default_height=item[0]
                )
                self.add_widget(w)
                
            elif isinstance(item, list):
                w = MyGrid(
                    widgets=item, 
                    cols=1, 
                    rows=len(item), 
                    canvas_color=get_color_from_hex("#0000ff1f")
                )
                self.add_widget(w)

            elif isinstance(item, dict):
                itemType = item.get("type", None)
                f = GridLayout(cols=1)

                if itemType is None:
                    break

                elif itemType is "image":
                    # print("adding an image...")
                    w = Image(
                        source=item.get("source", "images/icons/bitcoin.png"),
                        size_hint=item.get("size_hint", (1, 1)), 
                        pos_hint=item.get("pos_hint", {"top": 1, "left": 1})
                        # width="100dp",
                        # height="100dp",
                    )
                    # w.height = "100dp"
                    f.add_widget(w)
                    self.add_widget(f)
                elif itemType is "label":
                    # print("adding label...")
                    w = Label(
                        text=item.get("text", "..."),
                        markup=item.get("markup", True),
                        font_size=item.get("font_size", 11),
                        size_hint=item.get("size_hint", (1, .2)),
                        pos_hint=item.get("pos_hint", {"top": .6, "left": 1}),
                        color=get_color_from_hex(item.get("color", "#000000ff")))
                    f.add_widget(w)
                    self.add_widget(f)

    def update_rectangle(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size
        self.rectangle.radius = [20,]

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

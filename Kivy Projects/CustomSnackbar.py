from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

KV = '''
<-Snackbar>
    MDCard:
        id: box
        size_hint_y: None
        height: dp(58)
        spacing: dp(5)
        padding: dp(10)
        y: -self.height
        x: root.padding
        md_bg_color: get_color_from_hex('323232')
        radius: (5, 5, 5, 5) if root.padding else (0, 0, 0, 0)
        elevation: 11 if root.padding else 0

        MDIconButton:
            pos_hint: {'center_y': .5}
            icon: root.icon
            opposite_colors: True
        MDLabel:
            id: text_bar
            size_hint_y: None
            height: self.texture_size[1]
            text: root.text
            font_size: root.font_size
            theme_text_color: 'Custom'
            text_color: get_color_from_hex('ffffff')
            shorten: True
            shorten_from: 'right'
            pos_hint: {'center_y': .5}

Screen:
    MDRaisedButton:
        text: "SHOW"
        pos_hint: {"center_x": .5, "center_y": .45}
        on_press: app.show()
'''


class CustomSnackbar(Snackbar):
    icon = StringProperty()


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show(self):
        CustomSnackbar(
            text="This is a snackbar!",
            icon="information",
            padding="20dp",
            button_text="ACTION",
            button_color=(1, 0, 1, 1)
        ).show()


Test().run()

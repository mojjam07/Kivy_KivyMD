from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"  # "Green", "Red"
        self.theme_cls.primary_hue = "200" # "500"


        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()

# OptionProperty is primary_palette
# Available options are: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’,
# ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’.

# Another available OptionProperties is:
# primary_hue
# Available options are: ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’,
# ‘A400’, ‘A700’.

# Another available OptionProperties is:
# primary_light_hue

# Another available OptionProperties is:
# primary_light_hue : primary_light_hue is an OptionProperty and defaults to ‘200’.

# Another available OptionProperties is:
# primary_dark_hue : primary_dark_hue is an OptionProperty and defaults to ‘700’.

# Another available OptionProperties is:
# primary_color : The color of the current application theme in rgba format.

# Another available OptionProperties is:
# primary_light : Colors of the current application color theme in rgba format (in lighter color).

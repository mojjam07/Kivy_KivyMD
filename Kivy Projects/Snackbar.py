from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
#:import Snackbar kivymd.uix.snackbar.Snackbar
Screen:
    MDRaisedButton:
        text: "Create simple snackbar"
        on_release: Snackbar(text="This is a snackbar!").show()
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: "20dp"

'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()

from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:
    MDLabel:
        text: "Hello, World!"
        halign: "center"
'''


class MainApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.fps_monitor_start()


MainApp().run()

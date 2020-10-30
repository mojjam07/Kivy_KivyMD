from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # Window bg color

class DemoApp(App):
    def build(self):
        label = Label(text='This is a text', font_size='20sp', bold=True,
                      color=(0,0,0,1),
                      italic=True)
        return label


DemoApp().run()


'''
In this lesson we created window screen, we add text, we changed its font size and style,
we changed its color
'''
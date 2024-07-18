from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker

KV = '''
FloatLayout:
    MDRaisedButton:
        text: "Open date picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
        on_release: app.show_date_picker()
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def  show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()


Test().run()

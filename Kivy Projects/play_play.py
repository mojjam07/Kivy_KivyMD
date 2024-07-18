from kivy.base import Builder
#from kivymd.uix.dialog import  MDDialog
from kivymd.app import MDApp

class m(MDApp):
	def build(self):
		return  Builder.load_string("""
#:import gch kivy.utils.get_color_from_hex

BoxLayout:
    orientation:"vertical"
    MDToolbar:
        id: toolbar
        pos_hint:{"top":1}
        title: 'El_Munjid'
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        background_hue: '500'
        elevation: 10
        left_action_items:[['menu', lambda x: app.toast("this is menu")]]
        right_action_items:[["backup-restore",lambda c : app.re()],["facebook",lambda c: app.facebook()]]
        
    
		""")

m().run()
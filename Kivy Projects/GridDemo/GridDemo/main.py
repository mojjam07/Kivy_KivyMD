from kivymd.app import MDApp
from kivy.lang import Builder

kv = """
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: "Demo App"
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["magnify", lambda x: x]]
            
        MDFloatLayout:
            ScrollView:
                MDGridLayout:
                    cols: 2
                    padding: dp(10)
                    spacing: dp(10)
                    adaptive_height: True
                    
                    ImageWidget:
                        source: "image1.png"
                    
                    ImageWidget:
                        source: "image2.png"
                    
                    ImageWidget:
                        source: "image3.png"
                    
                    ImageWidget:
                        source: "image4.png"
                    
                    ImageWidget:
                        source: "img1.png"
                    
                    ImageWidget:
                        source: "img2.png"
                    
                    ImageWidget:
                        source: "img3.png"
                    
                    ImageWidget:
                        source: "img4.png"
            

<ImageWidget@FitImage>:
    size_hint_y: None
    height: dp(120)
    radius: dp(20)
    
"""


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    DemoApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.config import Config
import main_muted
import main_asli

def call_mute():
    # Call necessary function from main_muted
    pass

def call_voice():
    # Call necessary function from main_asli
    pass

Config.set('graphics', 'resizable', True)
Window.clearcolor = (0,153/255,153/255,1)

class AntiApp(App):
    
    def build(self):
        layout=BoxLayout(orientation='vertical',spacing=10,padding=20)
        logo=Image(source="logo.png")
        btn=Button(text="SPEAKING",size_hint=(None,None),width=200,height=100,
                   pos_hint={'center_x':0.5},
                   background_color=(0,0,0,1))
        btn2 = Button(text="TYPING",size_hint=(None,None),width=200,height=100,
                   pos_hint={'center_x':0.5},
                      background_color=(5/255,5/255,5/255,1))
        
        label=Label(text="WELCOME, I AM TALK BOB.\nHOW WOULD YOU LIKE TO CONVERSE WITH ME",
                    font_size='17sp',bold=True,italic=True)
        layout.add_widget(label)
        layout.add_widget(logo)
        btn.bind(on_press= lambda a:call_voice())
        btn2.bind(on_press= lambda a:call_mute())
        layout.add_widget(btn)
        layout.add_widget(btn2)

        return layout

if __name__=="__main__":
     AntiApp().run()
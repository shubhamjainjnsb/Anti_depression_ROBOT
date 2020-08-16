from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.config import Config
def call_mute():
    import main_muted
def call_voice():
    import main_asli
Config.set('graphics', 'resizable', True)
Window.clearcolor = (0,153/255,153/255,1) #open RGB calculator take the values and divide by 255

class AntiApp(App):
    
    def build(self):
        layout=BoxLayout(orientation='vertical',spacing=10,padding=40)
        logo=Image(source="logo.png")
        btn=Button(text="SPEAKING",size_hint=(None,None),width=100,height=50,
                   pos_hint={'center_x':0.5},
                   background_color=(0,0,0,1))
        btn2 = Button(text="TYPING",size_hint=(None,None),width=100,height=50,
                   pos_hint={'center_x':0.5},
                      background_color=(5/255,5/255,5/255,1))
        
        label=Label(text="                     WELCOME, I AM TALK BOB."+"\n" +"HOW WOULDYOU LIKE TO CONVERSE WITH ME",
                    font_size='25sp',bold=True,italic=True)
        layout.add_widget(label)
        layout.add_widget(logo)
        btn.bind(on_press= lambda a:call_voice())
        btn2.bind(on_press= lambda a:call_mute())
        layout.add_widget(btn)
        layout.add_widget(btn2)


        return layout

if __name__=="__main__":
     AntiApp().run()
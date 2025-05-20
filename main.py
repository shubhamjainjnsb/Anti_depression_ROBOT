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
    main_muted.some_function()

def call_voice():
    main_asli.some_function()

Config.set('graphics', 'resizable', True)
Window.clearcolor = (0,153/255,153/255,1)

class AntiApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        logo = Image(source="logo.png")
        speaking_button = Button(text="SPEAKING", size_hint=(None,None), width=200, height=100,
                                 pos_hint={'center_x':0.5},
                                 background_color=(0,0,0,1))
        typing_button = Button(text="TYPING", size_hint=(None,None), width=200, height=100,
                               pos_hint={'center_x':0.5},
                               background_color=(5/255,5/255,5/255,1))

        label_text = """
                     WELCOME, I AM TALK BOB.
                     HOW WOULD YOU LIKE TO CONVERSE WITH ME
                     """
        label = Label(text=label_text, font_size='17sp', bold=True, italic=True)
        layout.add_widget(label)
        layout.add_widget(logo)
        speaking_button.bind(on_press= lambda a: call_voice())
        typing_button.bind(on_press= lambda a: call_mute())
        layout.add_widget(speaking_button)
        layout.add_widget(typing_button)

        return layout

if __name__=="__main__":
     AntiApp().run()

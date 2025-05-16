# Import necessary modules from kivy package
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.config import Config

# Function to call the muted version of the main program
def call_mute():
    import main_muted

# Function to call the voice version of the main program
def call_voice():
    import main_asli

# Set the graphics configuration
Config.set('graphics', 'resizable', True)

# Set the window color
Window.clearcolor = (0,153/255,153/255,1) #open RGB calculator take the values and divide by 255

# Main App class
class AntiApp(App):
    
    # Build the app layout
    def build(self):
        # Create a vertical layout with some spacing and padding
        layout=BoxLayout(orientation='vertical',spacing=10,padding=20)
        
        # Add logo image
        logo=Image(source="logo.png")
        
        # Create a button for speaking
        btn=Button(text="SPEAKING",size_hint=(None,None),width=200,height=100,
                   pos_hint={'center_x':0.5},
                   background_color=(0,0,0,1))
        
        # Create a button for typing
        btn2 = Button(text="TYPING",size_hint=(None,None),width=200,height=100,
                   pos_hint={'center_x':0.5},
                      background_color=(5/255,5/255,5/255,1))
        
        # Create a welcome label
        label=Label(text="                     WELCOME, I AM TALK BOB."+"\n" +"HOW WOULDYOU LIKE TO CONVERSE WITH ME",
                    font_size='17sp',bold=True,italic=True)
        
        # Add widgets to the layout
        layout.add_widget(label)
        layout.add_widget(logo)
        btn.bind(on_press= lambda a:call_voice())
        btn2.bind(on_press= lambda a:call_mute())
        layout.add_widget(btn)
        layout.add_widget(btn2)

        return layout

# Run the app
if __name__=="__main__":
     AntiApp().run()
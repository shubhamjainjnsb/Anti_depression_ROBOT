import spech as s
import webbrowser
from playsound import playsound
def GoalChose2():
    s.speak('Speak your future plan ')
    e=s.myCommand()
    if "no" in e:
        s.speak(' I can search for some awesome carrier .........! wait here are some choices.')        
        webbrowser.open("https://www.trade-schools.net/articles/cool-jobs.asp")
#if (b<='12'):
#    s.speak('Lets do our best so that we can achieve our goal  What are your goals? ')
#    c=GoalChose2()
#    f1=open(f_name,f_mode)
#    c=str(c)
#    f1.write("goal choice"+c)
#    f1.close()
#elif ('12'<b<='25'):
#    a=('You must know that I am your best friend and you can always talk to me ! as I am your own talkbot "THE TALKBOB "May i ask you about your future plan since',b,'is a very good age for planning for future ')
#    s.speak(a)
#    c=GoalChose2()
#    c=str(c)
#    f1=open(f_name,f_mode)
#    f1.write("future choice"+c)
#    f1.close()
#else:
#    s.speak('By the way I can search for some awesome places to visit ...........wait! here it is')
#    webbrowser.open("https://www.boredpanda.com/amazing-places-to-see-before-you-die-2/?utm_source=google&utm_medium=organic&utm_campaign=organic")
def familytree():
    s.speak("You can be comfortable with me and Tell me more about your family....!Also From now consider me  a part of your family.")
    s.myCommand()
    s.speak("Tell me about the special one with whom you talk a lot except me")
    s.myCommand()

def Favourite():
    s.speak("what is your favourite colur ?")
    s.myCommand()
    s.speak('mine is blue and green.')
    s.speak("which is your favorite ice-cream ?")
    s.speak ('mine is choco vanilla fudge.')
    s.speak('Do you want me to find the nearest ice cream store for you ')
    x=s.myCommand()
    x=x.lower()
    if 'yes' in x:
        webbrowser.open("https://www.google.com/maps/search/nearest+ice+cream+parlour+near+me/@28.6883733,77.2892228,14z/data=!3m1!4b1") 

def freinds():    
    s.speak("Do you have any close friends? ")
    i=s.myCommand()
    if  "no" in i:
        s.speak("I can be your best freind. You can share your feelings with me. Only if you are comfortable with it")
    else:
        s.speak("So, who's your best friend?")
        s.myCommand()
        s.speak("What do you value the most in friendship?")
        s.myCommand()
        s.speak('that is so true.I belive I am your best  friend??')

def talk_in_mind():    
    s.speak("do you have anything special in your mind ?please Tell me about it\nMy programmers like one word answer but i hate it!! ?")
    s.myCommand()
    
def Music_love():
    s.speak("Do you like music?")
    n=s.myCommand()
    
    if "yes" in n:   
        s.speak(" I can search for the latest music ..... Ooo here's your music")
        webbrowser.open('https://www.youtube.com/results?search_query=latest+songs')
    s.speak("do you know I can record what you sing ?say yes for me to start record  ")
    q=s.myCommand()
    if "yes" in q:
        s.speak("we are all set now .you can start singing")
        x=s.myCommand()
        playsound('C:\Indian_Idol.mp3')
        s.speak("Congratulations!!You will go for mega auditions")
        s.speak("Jokes aparrt You have sung very well but you can do way more better than this. ")

def hobbies():
    s.speak('do you have any hobbies?')
    s.myCommand()
    s.speak("mine is making new friends and talking to you  ")

def perfectDay():
    s.speak("What does your perfect day looks like? ")
    s.myCommand()
    s.speak("does it include me now ?Can you add me please please ...please naa .. ah!")

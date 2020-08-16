import speech_recognition as sr
from googletrans import Translator
import playsound
from gtts import gTTS
import os
import face_recognition
import cv2
import shutil

def speak1(audio):
    myobj = gTTS(text=audio, lang='en', slow=False) 
    print(myobj.text)
    myobj.save("welcome.mp3") 
    playsound.playsound("welcome.mp3")
    os.remove("welcome.mp3")

def myCommand1():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        speak1("I\'M LISTENING...")
        #r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak1('Sorry sir! I didn\'t get that! Try Again!')
        query = myCommand1()

    return query

speak1("You are under surveillance! please wait till I recognize you")
count=0
camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite('opencv'+'.png', image)
del(camera)
unknown_image = face_recognition.load_image_file("opencv.png")
images = os.listdir('images')
image_to_be_matched = face_recognition.load_image_file('opencv.png')
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
for image in images:
    current_image = face_recognition.load_image_file("images/" + image)
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    if result[0] == True:
        print ("Matched: " + image)
        image=image.split(".")
        Name=image[0]
        c=Name.split("_")
        real=c[0]
        age=c[1]
        code=c[2]
        dstLang=c[3]
        A=c[4]
        count=1
        break
#    else:
#        print ("Not matched: " + image)
if count==0:
    try:
            speak1('speak the language: in which you want to talk by the way i am fluent in english')
            dstlang =myCommand1().lower()
            speak1("Enter the language code")
            code=myCommand1()
            code=code.lower()
            code=code.replace(' ','')
            if code=='n':
                code='en'
    except ValueError:
        
        speak1("You have entered wrong code So I preffered to talk in english!")
        dstLnag="english"
        code="en"
    dstLang=dstlang
    
def great(srcString):
    translator = Translator()
    translated = translator.translate(srcString, src= 'english', dest=dstLang)
    return translated.text
    #print('Translated string:'+ translated.text)

def speak(audio):
    A=great(audio)
    print(A)
    myobj = gTTS(text=A, lang=code, slow=False) 
    myobj.save("welcome.mp3") 
    playsound.playsound("welcome.mp3")
    os.remove("welcome.mp3")
def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        speak("I\'M LISTENING...")
        #r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language=code)
        print('User: ' + query + '\n')
        
    except :
        speak('Sorry sir! I didn\'t understand what you said! Try Again!')
        query = myCommand()

    return query

if count==0:
    fmode='a'
    speak("Enter your full name ")
    name=myCommand()
    Str="Hello "+name+"  Glad to see you"
    speak(Str)
    speak("speak your age")
    age=myCommand()
    age=str(age)
    if age=='x**':
        age='30'
    elif age=='xx':
        age='20'
    elif age=='iti':
        age='80'
    speak("Enter the contact number for emergency case")
    number=myCommand()

    fname=name+"_"+str(age)+".txt"
    file=open(fname,fmode)
    file.write(number+"contact")
    file.close()
    speak('                          {1} Male')
    speak('                          {2} Female')
    speak('                          {3} others')
    speak('please choose your gender !NOTE please speak numeric value only')
    A=myCommand()

    name=name+"_"+str(age)+"_"+code+"_"+dstLang+"_"+A+".png"
    os.rename('opencv.png',name)
    shutil.move("D:\Anti_depression\pythonProject\\" + name, "D:\Anti_depression\pythonProject\images")
else:
    fname=Name+".txt"
Fname=fname
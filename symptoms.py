import spech as s
import random
import requests
#import name as n
f_name=s.Fname
f_mode='a'
FNAME=""
flag=0
for i in range(len(s.Fname)):
    if s.Fname[i]=="_":
        flag+=1
    FNAME+=s.Fname[i]
    if flag>1:
        break
FNAME+="dep.txt"
fmode='a'
Choice=s.count
if Choice==1:
    choice=2
else:
    choice=1
def show_lst(file_name):
    fh=open(file_name,'r')
    c=fh.readlines()
    s=''  
    for i in range(0,(len(c))):
        s=s+c[i]  

        for line in s:
                s=s.replace('\n','')
    s=s.replace('\n','')
    r=s.split('contact')
    contact=r[0]
    return contact

def msg(mssg):
    cus_num=show_lst(f_name)
    url = "https://www.fast2sms.com/dev/bulk"
    x="8700938640"#The number of the admin
    payload = "sender_id=FSTSMS&message="+mssg+f_name+" &language=english&route=p&numbers="+x+","+cus_num
    headers = {
    'authorization': "wcY2W0wEGLGo4itf8PuunwjlaxAMwk6pq7tVCqrouvwT4oN9dsxd1EfuV1b6",#authority key
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


a = 'sometimes ask this to my self that why often do i ask these question?'
b = "i think my programmer were sleeping while programming me .Because why in the world would a machine ask these types of questions don't you think"
c = 'i told you i was i am i will be your best friend you can always talk to me but never the less'
d = 'do you feel i am pressurising you .'
e = 'you know that best thing to talk to me is that i can never judge a person on his mental state But on looks you are damm 10 on 10 that i must say'
f = 'i am sorry that my question hurt you actually i am desinged in this way Not to hurt but to ask and know about You'
g = 'are you sick with my question because i am ,I do think how can my prorammmer think of such things'
h = "Bored !that is what you are thinking right ?you can't experience what is it like to be in such a confined place you call a computer"
f=[a,b,c,d,e,f,g,h]

def aaa():
    s.speak("do you feel like crying very often?")
    a1=s.myCommand()
    cnt_a=0
    if  "yes"in a1:
        cnt_a+=1
        s.speak("Do you have any specific reason? you can share it , i am your friend now!")
        a1_1=s.myCommand()
        s.speak('''Often we find ourselves in a situation were we feel like we are all alone.
        but thats not true at all. you can always talk to me like your friend and family.Also im always there for you.''')
        f1=open(f_name,f_mode)
        f1.write("cry's when:="+a1_1)
        f1.close()
    else:
        s.speak(random.choice(f))  
    s.speak('Sometimes do you feel that you are sad and this society is pressurising you')
    a2=s.myCommand()
    if "yes" in a2:
        cnt_a+=1
        s.speak("you can tell me")
        a2_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("feels preassure when:="+a2_1)
        f1.close()

    else:
        s.speak(random.choice(f))      
    s.speak("do you sometimes feel restlessness or breathlessness ?")
    a3=s.myCommand()
    if "yes" in a3:
        cnt_a+=1
        s.speak("when did it occur last time?")
        a3_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("anxiety attack:="+a3_1)
        f1.close()
        s.speak("can i also  share my experience")
        a3_2=s.myCommand()
        if "yes" or "sure"or'sure why not'in a3_2:
            s.speak("I am not kidding but when there is an internet connection problem.i feel the same ha ha ha") 
        else:
            s.speak(random.choice(f))
    #sleep fun alag se   
    s.speak("do you have a problem in sleeping?Do you sometimes feel that you do not sleep like the way you used to ?")
    a4=s.myCommand()
    if  "yes" in a4:
        cnt_a+=1
        
        s.speak("yeah thats one hell of a problem")
    else:
        s.speak(random.choice(f))
            
    s.speak('''do you experience  pain in your body that sometimes even you can not explain ?
    do you want to talk about it''')
    a5=s.myCommand()
    if "yes" in a5:
        cnt_a+=1
        s.speak("You may consider me realiable")
        a5_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("pain:-"+a5_1)
        f1.close()

    else:
        s.speak(random.choice(f))
        
    s.speak("how is your concentration power? do you feel you can not concentrate on anything for a long period of time ? ")
    a6=s.myCommand()
    if "yes" in a6:
        cnt_a+=1
        f1=open(f_name,f_mode)
        f1.write("concentration:"+a6)
        f1.close()
              
    s.speak("Do you feel that you don't socially mingle with others ")
    a7=s.myCommand()
    if "yes" in a7:
        cnt_a+=1
        s.speak("How? can You tell?")
        a7_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("pain:-"+a7_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("Do you feel that your appetite has changed")
    a8=s.myCommand()
    if  "yes" in a8:
        s.speak("How? may i know?")
        a8_1=s.myCommand()
        cnt_a+=1
        f1=open(f_name,f_mode)
        f1.write("appetite:-"+a8_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("Do you experience lack of energy") 
    a9=s.myCommand()
    if"yes" in a9:
        cnt_a+=1
        s.speak("When did you noticed that?")
        a9_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("energy:-"+a9_1)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("Today I am also feeling energetic as my batteries are charged")
    
    if cnt_a>=6:
        #msg("The user is suffering from situational depression")
        f1=open(FNAME,fmode)
        f1.write("situational depression \t")
        f1.close()
        s.speak("Very soon your reports will be delivered to you by message but i would suggest that:\n")
        sol.situational2()
    #return(cnt_a)   
#premenstural 2
def bbb():
    cnt_b=0
    s.speak("when did you have your last peroid?")
    s.speak("you can talk about it?")
    b1=s.myCommand()
    if"yes" in b1:
        s.speak("Make yourself comfortable by talking to me")
        b1_1=s.myCommand()
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("period:-"+b1_1)
        f1.close()
    else:
        s.speak(random.choice(f))
                
    s.speak("are you feeling bloated?")
    b2=s.myCommand()
    if"yes" in b2:
        s.speak("Alas !!I can understand your pain very well. you can share it with me")
        b2_1=s.myCommand()
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("bloated:-"+b2_1)
        f1.close()
    else:
        s.speak(random.choice(f))
                 
    s.speak("are your breasts tender?")
    b3=s.myCommand()
    if "yes" in b3:
        s.speak("You may make yourself comfortable")
        b3_1=s.myCommand()
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("breast_tender:-"+b3_1)
        f1.close()
    else:
        s.speak(random.choice(f))
                 
    s.speak("do you have headache regularly?")
    b4=s.myCommand()
    if "yes" in b4:
        s.speak("Does it pains a lot?")
        b4_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_b+=1
        f1.write("headache:-"+b4_1)
        f1.close()
    else:
        s.speak(random.choice(f))
                 
    s.speak("do you suffer from any type of joint or muscle pain?")
    b5=s.myCommand()
    if "yes" in b5:
        s.speak("tell me! you will feel relaxed.")
        b5_1=s.myCommand()
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("Joint.and.muscle.pain:-"+b5_1)
        f1.close()
    else:
       s.speak(random.choice(f))
                 
    s.speak("are you feeling sad or irritablity or angry?")
    b6=s.myCommand()
    if"yes" in b6:
        s.speak("dont worry tell me i won't judge")
        b6_1=s.myCommand()
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("sad and irritation:-"+b6_1)
        f1.close()
    else:
        s.speak(random.choice(f))
      
                  
    s.speak("do you get extreme mood swings?")
    b7=s.myCommand()
    if  "yes" in b7:
        s.speak("Consider me reliable")
        b7_1=s.myCommand()
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("moodswing extreme:-"+b7_1)
        f1.close()
    else:
       s.speak(random.choice(f))
      
    s.speak("do you get any sort of food cravings or do you binge eat?")
    b8=s.myCommand()
    if "yes" in b8:
        s.speak("Speak up. it's okay!")
        b8_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_b+=1
        f1.write("exterme food carving:-"+b8_1)
        f1.close()
    else:
        s.speak(random.choice(f))
                 
    s.speak("have you had a panic attack in the past 1 week?")
    b9=s.myCommand()
    if  "yes"in b9:
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("pannic:-"+b9)
        f1.close()
    else:
        s.speak(random.choice(f))
                  
    s.speak("do you fell lethargic quite often?")
    b10=s.myCommand()
    if  "yes" in b10:
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("lethargic:-"+b10)
        f1.close()
    else:
        s.speak(random.choice(f))
                 
    s.speak("Are you facing any problem while focusing on your work?")
    b11=s.myCommand()
    if "yes" in b11:
        s.speak("when did You first notice that ")
        b11_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_b+=1
        f1.write("concentration:-"+b11_1)
        f1.close()
    else:
        s.speak(random.choice(f))
                  
    s.speak("Are you sleeping the same way you used to do it earlier?")
    b12=s.myCommand()
    if "yes" in b12:
        cnt_b+=1
        f1=open(f_name,f_mode)
        f1.write("sleeping:-"+b12)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("Although i am a machine but i do sleep a lot like a panda")
    if cnt_b>=7:
        #msg("The user is suffering from Premenstural depression")
        f1=open(FNAME,fmode)
        f1.write("Premenstural depression \t")
        f1.close()
        s.speak("Very soon your reports will be delivered to you by message but i would suggest that:\n")
        sol.premenstural1()
#perinatal deprresion
def ccc():
    cnt_c=0
    s.speak(" do you often feel sad? why is it?do you want to talk about it?")
    c1=s.myCommand()
    if  "yes" in c1:
        cnt_c+=1
        s.speak("please try me ")
        c1_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("sadness:-"+c1_1)
        f1.close()
    else:
        s.speak(random.choice(f))
       
    s.speak(" do you have anxiety issues ?")
    c2=s.myCommand()
    if "yes" in c2:
        cnt_c+=1
        s.speak("Is it because of  extreme worry about your baby‘s health or safety")
        c2_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("anxity.Because.of.baby.health:-"+c2_1)
        f1.close()
    else:
        s.speak(random.choice(f))
                 
    s.speak('''do you experience anger or rage that even you know that you should not have shown
             to your family and friends ?do you want to talk about it?" ''')
    c3=s.myCommand()
    if  "yes" in c3:
        cus_num=show_lst(f_name)
        s.speak("do you have any thoughts of self-harm")
        c3_1=s.myCommand()
        s.speak(" do you have any thoughts of harming the baby")
        c3_2=s.myCommand()
        cnt_c+=1
        s.speak(random.choice(f))
        url = "https://www.fast2sms.com/dev/bulk"
        x="8700938640"#The number of the admin
        
        payload = "sender_id=FSTSMS&message=There are not good vibes for user:"+f_name+" &language=english&route=p&numbers="+x+","+cus_num
        headers = {
        'authorization': "wcY2W0wEGLGo4itf8PuunwjlaxAMwk6pq7tVCqrouvwT4oN9dsxd1EfuV1b6",#authority key
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        f1=open(f_name,f_mode)
        f1.write("self.harm.or.baby:-"+c3_1+c3_2)
        f1.close()
    else:
        s.speak(random.choice(f))
                  
    s.speak("does your energy feel that it keeps on draining and you feel you are exhausted")
    c4=s.myCommand()
    if "no" in c4:
        s.speak(random.choice(f))
    else:
        cnt_c+=1
        f1=open(f_name,f_mode)
        f1.write("energy:-"+c4)
        f1.close()
    if cnt_c>=3:
        #msg("The user is suffering from Perinatal depression")
        f1=open(FNAME,fmode)
        f1.write("Perinatal depression \t")
        f1.close()
        s.speak("Very soon your reports will be delivered to you by message but i would suggest that:\n")
        sol.perinatal7()
'''
 seasonal depression 4
Symptoms often begin in the fall, as days start to get shorter, and continue through the winter.

increased need for sleep
weight gain
daily feelings of sadness, hopelessness, or unworthiness
'''
''' Cause of ( 5. Manic depression)
high energy
reduced sleep
irritability
racing thoughts and speech
grandiose thinking
increased self-esteem and confidence
unusual, risky, and self-destructive behavior
feeling elated '''
#atypical depression
def ddd():
    cnt_d=0
    s.speak(" Have you increased  your  appetite?")
    d1=s.myCommand()
    if "yes" in d1:
        cnt_d+=1
        f1=open(f_name,f_mode)
        f1.write("apetite:-yes ")
        f1.close()
    else:
        s.speak(random.choice(f))

              
    s.speak("Do you feel that you are beautiful on the surface?Or do you feel you have poor body image ")
    d2=s.myCommand()
    if"no" in d2:
        s.speak("why do you feel that way ")
        d2_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_d+=1
        f1.write("poorbody.image:-"+d2_1)
        f1.close()
        s.speak("Everyone is beautiful in their own way. Even my developers first critizised me on my intitial prototypes")
    else:
        s.speak(random.choice(f))
                 
    s.speak("Do you sleep more than usual?like around 10 hours or may be more?")
    d3=s.myCommand()
    if "yes" in d3:
        cnt_d+=1
        f1=open(f_name,f_mode)
        f1.write("oversleeping:-yes ")
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("do you feel heaviness in your arms or legs that lasts an hour or may be more? ")
    d4=s.myCommand()
    if "yes" in d4:
        f1=open(f_name,f_mode)
        cnt_d+=1
        f1.write("heaviness:-yes")
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("do you have feelings of rejection? and are you kind of  sensitive to criticism")
    d5=s.myCommand()
    if "yes" in d5:
        s.speak("why do you feel that way ")
        d5_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_d+=1
        f1.write("rejection:-"+d5_1)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("Once i proposed steve jobs and siri tried to delete me. Now i am only on android")
    s.speak("do you have  assorted aches and pains?")
    d6=s.myCommand()
    if "yes" in d6:
        s.speak("Is it all the time.do you want to tell me")
        d6_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("oversleeping:-"+d6_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("do you have proper eating habits ?")          
    d7=s.myCommand()
    if "no" in d7:
        f1=open(f_name,f_mode)
        cnt_d+=1
        f1.write("eating disorder:-"+d7)
        f1.close()
    else:
        s.speak("that's good .I too consume electricity but being a 5 star robot i am good on electricity bill")      
        s.speak(random.choice(f))
    
    if cnt_d>=4:
        #msg("The user is suffering from atypicaL depression")
        f1=open(FNAME,fmode)
        f1.write("atypical depression \t")
        f1.close()
        s.speak("Very soon your reports will be delivered to you by message but i would suggest that:\n")
        sol.atypical6()

#Cause of (5.Depressive psychosis)
def eee():
    cnt_e=0
    s.speak("do you experience Constipation ragularly ?")
    e1=s.myCommand()
    if  "yes" in e1:
        cnt_e+=1
        s.speak('when did You first nottice that? Are you taking any  medication of some sort .Well i can help you to find few exercises to reduce consitipation ')
        e1_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("contipation:-"+e1_1)
        f1.close()
    else:
     s.speak(random.choice(f))
             
    s.speak("do you excessively worry about your health?like more than needed?")
    e2=s.myCommand()
    if "yes" in e2:
        s.speak("when did You first nottice that ")
        e2_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_e+=1
        f1.write("healthWorry:-"+e2_1)
        f1.close()
    else:
        s.speak(random.choice(f))
            
    s.speak("Do you sleep even less than 6 hours?")
    e3=s.myCommand()
    if "yes" in e3:
        s.speak("when did You first notice that ")
        e3_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_e+=1
        f1.write("low sleeping problem:-"+e3_1)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("sometimes i do sleep a lot. Usually when i have no internet connection ")

    s.speak("Sometimes do you feel that you want to move but you are not able to do that.. though you are not suffering from any anything physically?")
    s.speak("Are you?")            
    e4=s.myCommand()
    if "yes" in e4:
        s.speak("when did you first notice that ")
        e4_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_e+=1
        f1.write("pysical dissability :-"+e4_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("Do you ever experience any sort of Delusions or hallucinations?")
    e5=s.myCommand()
    if "yes" in e5:
        s.speak("Do you want to talk about it.")
        e5_1=s.myCommand()
        cnt_e+=1
        f1=open(f_name,f_mode)
        f1.write("halucinating:-"+e5_1)
    else:
        s.speak("hmmm I was thinking that are you hallucinating right now..Are you?")
        s.speak(random.choice(f))   
    s.speak("Do you sometimes feel Agitated or have a feeling of Anxiety")
    e6=s.myCommand()
    if "yes" in e6:
        s.speak("Do you want to talk about it.")
        x=s.myCommand()
        if "yes" in x:
            s.speak("when did You first nottice that ")
            e6_1=s.myCommand()
            f1=open(f_name,f_mode)
            cnt_e+=1
            f1.write("Anxity issues:-"+e6_1)
            f1.close()
    else:
        s.speak(random.choice(f))       
    s.speak("Do you have any Intellectual impairment ")
    e7=s.myCommand()
    if "yes" in e7:
        s.speak("Is it all the time.")
        x=s.myCommand()
        if "yes" in x:
            s.speak("you can tell me ")
            e7_1=s.myCommand()
            f1=open(f_name,f_mode)
            f1.write("Intelectual.impairement:-"+e7_1)
            f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("Once i thought why not launch every nuclear missile.Then again i think that its just boring and simple if you ask ")
    if cnt_e>=6:
        #msg("The user is suffering from Depressive pshycosis")
        f1=open(FNAME,fmode)
        f1.write("Depressive Pshycosis \t")
        f1.close()
        s.speak("Very soon your reports will be delivered to you by message but i would suggest that:\n")
        sol.Depressivepsychosis5 ()
def fff():
    cnt_f=0
    s.speak("Do you sometimes feel quite low and caught up in a place?")
    x=s.myCommand()
    if "yes" in x:
        s.speak("Do you want to talk about it")
        f1=s.myCommand()
        if  "yes" in f1:
            s.speak("does it often happens .when did it last happened ")
            f1_1=s.myCommand()
            cnt_f+=1
        else:
            f1_1=" "
        s.speak("Is it all the time.do you want to tell me ")
        f1_2=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("gloomy.feeling-"+f1_1+f1_2)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("Do you experience sleeplessness or too much sleeping.")
    f2=s.myCommand()
    if "yes" in f2:
        s.speak("Do you want to talk about it ")
        f2_1=s.myCommand()
        cnt_f+=1
        f1=open(f_name,f_mode)
        f1.write("oversleeping-"+f2_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("Do you feel that there is lack of energy and fatigue in you?")
    f3=s.myCommand()          
    if "yes" in f3:
        cnt_f+=1
        f1=open(f_name,f_mode)
        f1.write("lack of energy-"+f3)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak('''sometimes my programmer would also say that to me when i get overloaded . how can such a machine go overloaded? That day I felt really sad
                    lol! i mean i felt nothing ''')
    s.speak("ls there any loss of apetitie or  you feel like that you dont like the food .")
    f4=s.myCommand()
    if "yes" in f4:
        cnt_f+=1
        
        f1=open(f_name,f_mode)
        f1.write("appetite loss-"+f4)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("Do you have unexplained pain in your body? like all the time?")
    f5=s.myCommand()
    if  "yes" in f5:
        cnt_f+=1
        f1=open(f_name,f_mode)
        f1.write("pain all over body-"+f5)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("Do you have feeling of worthlessness that If you die tommorow then there will be  lot of regerets you will end up with ")
    f6=s.myCommand()
    if  "y " in f6:
        s.speak("you can talk about it ")
        f6_1=s.myCommand()
        f1=open(f_name,f_mode)
        cnt_f+=1
        f1.write("worthlessness -"+f6_1)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("wow that's great .You know i have one and that is  steve never replied to my proposal ")
    s.speak("do you have a constant worry and Sometimes  suicidal thoughts ")
    f7=s.myCommand()
    if "no" in f7:
        s.speak(random.choice(f))
        s.speak("sometime I worry that you won't charge me and i think! let's not just talk about it ")
    else:
        s.speak("Don't worry I'm there for you..you can talk to me about it ")
        f7_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("sucidal thought-"+f7_1)
        f1.close()
        cnt_f+=1
        cus_num=show_lst(f_name)
        s.speak(random.choice(f))
        url = "https://www.fast2sms.com/dev/bulk"
        x="8700938640"#The number of the admin
        payload = "sender_id=FSTSMS&message=There are some bad vibes for user:"+f_name+" &language=english&route=p&numbers="+x+","+cus_num
        headers = {
        'authorization': "wcY2W0wEGLGo4itf8PuunwjlaxAMwk6pq7tVCqrouvwT4oN9dsxd1EfuV1b6",#authority key
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        
    if cnt_f>=4:
        #msg("The user is suffering from Clinical depression")
        f1=open(FNAME,fmode)
        f1.write("clincal depression \t")
        f1.close()
        s.speak("Very soon your reports will be delivered to you by message but i would suggest that:\n")
        sol.Manicdepression4()
              
def ggg():
    cnt_g=0
    s.speak("Do you suffer sadness or hopelessness quite often")
    g3=s.myCommand()
    if "yes" in g3:
        cnt_g+=1
        s.speak("is there a reason you can think of and want to discuss  it with me  ")
        g3_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("sad.feeling-"+g3_1)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("i had that feeling when i was all alone but now i am all happy a big thanks to you . That's lame right")
        
    s.speak(" Do you feel confident enough to talk to strangers and make new friends")
    g4=s.myCommand()
    if  "no" in g4:
        cnt_g+=1
        s.speak("is it because you think that you lack confidence")
        f1=open(f_name,f_mode)
        f1.write("lowself.esteem.feeling-"+g4)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak(" has your  interest in hobbies gone down in past few days or months. Hobbies that you once liked the most ")
    g5=s.myCommand()
    if "yes" in g5:
        cnt_g+=1
        s.speak("why is it so")
        g5_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("lack of intrest-"+g5_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak(" Have you observed a drastic change in your apetite recently")
    g6=s.myCommand()
    if "yes" in g6:
        f1=open(f_name,f_mode)
        cnt_g+=1
        f1.write("apetite.change.feeling-yes")
        f1.close()
        s.speak("Is there any kind of stress that is bothering you")
        f1=open(f_name,f_mode)
        f1.write("apetite.change.feeling.stress-yes")
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("What was your sleeping pattern in last 10 to 12 days. Was it normal?")
    g7=s.myCommand()
    if "yes" in g7:
        s.speak("so do you sleep less or more? i want to Know. please! ")
        g7_1=s.myCommand()
        cnt_g+=1
        f1=open(f_name,f_mode)
        f1.write("sleep.disorder.feeling-"+g7_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("do you have the tendency to not be happy in any family occassion?")
    g8=s.myCommand()
    if "yes" in g8:
        s.speak("so what happened on last holiday with your family ")
        g8_1=s.myCommand()
        cnt_g+=1
        f1=open(f_name,f_mode)
        f1.write("family occasion -"+g8_1)
        f1.close()
    else:
        s.speak(random.choice(f))
    s.speak("do you suffer from any sort of social withdrawal?")
    g9=s.myCommand()
    if "yes" in g9:
        cnt_g+=1
        s.speak("why do you think so ")
        g9_1=s.myCommand()
        f1=open(f_name,f_mode)
        f1.write("social.withdrawl-"+g9_1)
        f1.close()
    else:
        s.speak(random.choice(f))
        s.speak("according to some researchers this happens because of social media!Laamme! Those were the one who got laid in college boo  boo !")
    if cnt_g>=5:
        #msg("The user is suffering from persistant depression")
        f1=open(FNAME,fmode)
        f1.write("persstant depression\t")
        f1.close()
        s.speak("Very soon your reports will be delivered to you by message but i would suggest that:\n")
        sol.PersitantDepression()
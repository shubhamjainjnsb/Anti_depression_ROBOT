import spech as s
import intro as t
import symptoms as st
import random
s.speak("Hi I'm your personal robot")
s.speak("THE TALK-BOB")

if s.count==1:
    ch=2
    Str="Hello "+s.real+"  happy to see you again"
    s.speak(Str)
else:
    ch=1
pasand=st.choice
a=s.A
if  pasand==2 or pasand == "2" or pasand=="two":
    t.familytree()
    t.Favourite()
    t.GoalChose2()
    t.hobbies()
else:#this ele is not wrking rest each and all is working excellent
    t.freinds()
    t.Music_love()
    t.perfectDay()
    t.talk_in_mind()

def talk():  
    if a =='1' or a==1:
        g="male"
    else:
        g="female"
    if g=="male":
        x=[1,3,4,5,6,7]
        r1=random.choice(x)
        
        if r1==1:
            st.aaa() 
        elif r1==3:
            st.ccc()
        elif r1==4:
            st.ddd()
        elif r1==5:
            st.eee()
        elif r1==6:
            st.fff()
        else:
            st.ggg()
        x.remove(r1)
        s.speak("Would you like to talk more? Please just say yes or no")
        x=s.myCommand()
        if x=='yes':
            talk()
        else:
            s.speak("I know these question were a bit hard on every one but this shows how i am programmed \n Also I want to learn about you ")
            s.speak("Bye sir")    
                                                
    else:
        x=[1,2,3,4,5,6,7]
        r1=random.choice(x)
        if r1==1:
            st.aaa()
        elif r1==2:
            st.bbb()
        elif r1==3:
            st.ccc()
        elif r1==4:
            st.ddd()
        elif r1==5:
            st.eee()
        elif r1==6:
            st.fff()
        else:
            st.ggg()
        x.remove(r1)
        s.speak("Would you like to talk more? Please speak yes or no only")
        x=s.myCommand()
        if "yes" in x:
            talk()
        else:
            s.speak("I know these question were a bit hard on every one but this shows how i am programmed")
            s.speak("Bye sir")    
            X=""
            flag=0
            for i in range(len(s.Fname)):
                if s.Fname[i]=="_":
                    flag+=1
                X+=s.Fname[i]
                if flag>1:
                    break
            X+="dep.txt"
            
            f1=open(X,"r")
            x=f1.readlines()
            string=""
            for i in range(len(x)):
                string+=x[i]
            if string!=" " or string!= "":
                st.msg("user",s.real,"is suffering from"+x+"Till the date hope so user will finish the theropy and i will keep you updted")
            else:
                st.msg("congratulation till the date user"+s.real+"has no mentl issue.")
            

talk()
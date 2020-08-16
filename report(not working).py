import spech as s
import solutions as sol
s.speak('Would you like to see your report?')
report=s.myCommand()
if "yes" in report:
    
    if cnt_a>=6:
        s.speak('Sorry sir! But you are diagonos with situational depression')
        speak ('would you like to find out its remedy ')
        s1=s.myCommand()
        if "yes" or 'sure' in s1:
            sol.situational2()
            
    if cnt_b>=7:
        s.speak('Sorry Madam! But you are diagonos with premenstural depression')
        speak ('would you like to find out its remedy ')
        s2=s.myCommand()
        if "yes" or 'sure' in s2:
             sol.premenstural1()
            
    if cnt_c>=3:
        s.speak('Sorry sir! But you are diagonos with perinatel depression')
        speak ('would you like to find out its remedy ')
        s3=s.myCommand()
        if "yes" or 'sure' in s3:
            sol.prinatal7()
            
    if cnt_d>=4:
        s.speak('Sorry sir! But you are diagonos with Atypical depression')
        speak ('would you like to find out its remedy ')
        s4=s.myCommand()
        if "yes" or 'sure' in s4 :
            sol.atypical6()
    if cnt_e>=4:
        s.speak('Sorry sir! But you are diagonos with depressive pshysocis')
        speak ('would you like to find out its remedy ')
        s5=s.myCommand()
        if "yes" or 'sure' in s5:
            sol.Depressivepsychosis5 ()
    if cnt_f>=4:
        s.speak('Sorry sir! But you are diagonos with depression Named Major depression')
        speak ('would you like to find out its remedy ')
        s6=s.myCommand()
        if "yes" or 'sure' in s6:
            sol.MajorDeppresion()
    if cnt_g>=5:
        s.speak('Sorry sir! But you are diagonos with persistant disorder')
    else:
        
        s.speak('congratulations!! you are all right !see ya soon')
        s.speak("I know these question were bit hard on every one but this shows how i am programmed \n Also I want to learn about you ")
        s.speak("Bye sir")

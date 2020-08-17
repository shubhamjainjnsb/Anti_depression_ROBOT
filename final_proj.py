import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from PIL import ImageTk, Image
window = tk.Tk()
window.title("Talk Bob")
window.geometry("850x600");
fontStyle = tkFont.Font(family="Lucida Grande", size=30, weight="bold")
string= text="WELCOME, I am Talk Bob."+"\n" +"How would you like to converse with me"
def withmic():
    import main_asli
def withoutmic():
    import dep_mute.main_muted
upperFrame=tk.Frame(window, bg='turquoise4', width=850, height=400)
lowerFrame=tk.Frame(window, bg='turquoise4', width=850, height=200)  

photo=PhotoImage(file="logo.png")
photo.zoom(120, 120)
  
#photo = PhotoImage(file = r"logo.png") 
#button=tk.Button(window, text = 'Click Me !', image = photo).pack()

button=tk.Button(upperFrame,text='PYTHON MAYHEM', height = 180, width = 130,image=photo, bg='white')


text=tk.Label(upperFrame, text=string,  fg="white", bg='turquoise4', font=fontStyle )    
button1=tk.Button(lowerFrame,text='SPEAKING', height = 4, width = 20,bg='black', command=withmic,fg="white")
button2=tk.Button(lowerFrame,text='TYPING', height = 4, width = 20,bg='black',command=withoutmic,fg="white")
button1.grid(row=1, column=0, padx=(100, 10))
button2.grid(row=2, column=0, padx=(100, 10)) 
upperFrame.pack()
lowerFrame.pack()
text.place(x=50,y=50)
button1.place(x=350,y=0)
button2.place(x=350,y=100)   
button.place(x=350,y=190)
window.mainloop()

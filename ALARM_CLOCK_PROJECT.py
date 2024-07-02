from tkinter import font 
from tkinter.ttk import *
from tkinter import *
from threading import *
from PIL import ImageTk,Image
from pygame import mixer

from datetime import datetime
from time import sleep 
bg_color='white'
col="blue"
col="black"
#window
window=Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)


#frames up
frame_line=Frame(window,width=400,height=5,bg=col)
frame_line.grid(row=0,column=0)

frame_body=Frame(window,width=400,height=290,bg=bg_color)
frame_body.grid(row=1,column=0)

#configuring and body
img=Image.open('icon.png')
img.resize((100,100))
img=ImageTk.PhotoImage(img)

app_image=Label(frame_body,height=100,image=img,bg=bg_color)
app_image.place(x=10,y=10)


name=Label(frame_body,text="ALARM",height=1,font=("Ivy 18 bold"),bg=bg_color)
name.place(x=125,y=10)


hour=Label(frame_body,text="Hour",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=col)
hour.place(x=127,y=40)
c_hour=Combobox(frame_body,width=2,font=("arial 15"))
c_hour['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=130,y=58)

mint=Label(frame_body,text="Min",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=col)
mint.place(x=177,y=40)
c_mint=Combobox(frame_body,width=2,font=("arial 15"))
c_mint['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_mint.current(0)
c_mint.place(x=180,y=58)

sec=Label(frame_body,text="Sec",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=col)
sec.place(x=230,y=40)
c_sec=Combobox(frame_body,width=2,font=("arial 15"))
c_sec['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=230,y=58)

period=Label(frame_body,text="Per",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=col)
period.place(x=277,y=40)
c_period=Combobox(frame_body,width=2,font=("arial 14"))
c_period['values']=("AM","PM")
c_period.current(0)
c_period.place(x=280,y=58)

def start_alarm():
    t=Thread(target=alarm)
    t.start()
def stop_alarm():
    print("Stop Alarm:",selected.get())
    mixer.music.stop()
    
selected=IntVar()


rad1=Radiobutton(frame_body,font=("aerial 10 bold"),value=1,text="Start",bg=bg_color,command=start_alarm,variable=selected)
rad1.place(x=125,y=95)

def sound_alarm():
    mixer.music.load("audio.mp3")
    mixer.music.play()
    selected.set(0)


    rad2=Radiobutton(frame_body,font=("aerial 10 bold"),value=2,text="Stop",bg=bg_color,command=stop_alarm,variable=selected)
    rad2.place(x=187,y=95)
    
def alarm():
    while True:
        control=1
        print(control)
        alarm_hour=c_hour.get()
        alarm_mint=c_mint.get()
        alarm_sec=c_sec.get()
        alarm_period=c_period.get()
        alarm_period=str(alarm_period).upper()
        
        now=datetime.now()
        
        hour=now.strftime("%I")
        mint=now.strftime("%M")
        sec=now.strftime("%S")
        period=now.strftime("%p")


        if control==1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_mint==mint:
                        if alarm_sec==sec:
                            print("Time to take a break!")
                            sound_alarm()
        sleep(1)

mixer.init()
window.mainloop()

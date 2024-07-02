from tkinter.ttk import*
from tkinter import*


from PIL import ImageTk,Image
bg_color='#ffffff'
col="blue"    
#window
window=Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)


#frames up
frame_line=Frame(window,width=400,height=5,bg=col)
frame_line.grid(row=0,column=0)



#configuring and body
img=Image.open("alarm.png")
img.resize((100,100))
img=ImageTk.PhotoImage(img)

app_image=Label(frame_body,height=100,image=img)
app_image.place(x=10,y=10)



window.mainloop()

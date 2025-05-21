#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk,filedialog
import random
import pyttsx3
import os
e=pyttsx3.init()

root=Tk()
root.geometry("620x800")
root.title('TEXT TO SPEECH CONVERTOR')

def talk():
    def check_voice():
        if(gender == 'male'and Langauge == 'EN'):
            e.setProperty('voice', v[2].id)
            e.setProperty('volume', (volume_) / 100)
            e.say(text)
            e.runAndWait()
        if(gender == 'Male'and Langauge == 'EN'):
            e.setProperty('voice', v[0].id)
            e.setProperty('volume', (volume_) / 100)
            e.say(text)
            e.runAndWait()
        if(gender == 'Female'and Langauge == 'EN'):
            e.setProperty('voice', v[1].id)
            e.setProperty('volume', (volume_) / 100)
            e.say(text)
            e.runAndWait()

    text = txt_area.get(1.0, END)
    Langauge = Language_combo.get()
    gender = gender_combo.get()
    speed = speed_combo.get()
    volume_ = scale_level.get()
    v = e.getProperty('voices')
    if (text):
        if (speed == 'Fast'):
            e.setProperty('rate', 300)
            check_voice()
        elif (speed == 'Normal'):
            e.setProperty('rate', 150)
            check_voice()
        else:
            e.setProperty('rate', 50)
            check_voice()

def Reset():
    txt_area.delete(1.0,END)
def download():
    def check_voice():
        if (gender == 'Male'):
            e.setProperty('voice', v[0].id)
            e.setProperty('volume', (volumes) / 100)
            path=filedialog.askdirectory()
            os.chdir(path)
            e.save_to_file(text,'music.mp3')
            e.runAndWait()
        else:
            e.setProperty('voice', v[1].id)
            e.setProperty('volume', (volumes) / 100)
            path = filedialog.askdirectory()
            os.chdir(path)
            e.save_to_file(text, 'file_generated.mp3')
            e.runAndWait()

    text=txt_area.get(1.0,END)
    gender=gender_combo.get()
    speed=speed_combo.get()
    volumes=scale_level.get()
    v=e.getProperty('voices')
    if(text):
        if(speed=='Fast'):
            e.setProperty('rate',300)
            check_voice()
        elif(speed=='Normal'):
            e.setProperty('rate',150)
            check_voice()
        else:
            e.setProperty('rate',50)
            check_voice()

lbl_title=Label(root,text="Text to Speech",font='arial 20')
lbl_title.place(x=0,y=0,relwidth=1)
Language_lbl=Label(root,text='Language',font='Impack 25 bold',width=15,bg='#303F9F',fg='#FFFFFF')
Language_lbl.place(x=10,y=50)
f1=Frame(root,relief=GROOVE,bd=5)
f1.place(x=10,y=100,width=600,height=300)

scrol_bar=Scrollbar(f1,orient=VERTICAL)
scrol_bar.pack(side=RIGHT,fill=Y)
txt_area=Text(f1,font=('times new rommon',15,'bold'),bg='#fafafa',yscrollcommand=scrol_bar.set,wrap=WORD)
txt_area.pack(fill=BOTH)

scrol_bar.config(command=txt_area.yview)

gender_lbl=Label(root,text='Gender',font='Impack 25 bold',width=12,bg='#0097A7',fg='#FFFFFF')
gender_lbl.place(x=10,y=410)

speed_lbl=Label(root,text='Speed',font='Impack 25 bold',width=12,bg='#0097A7',fg='#FFFFFF')
speed_lbl.place(x=230,y=410)

volume_lbl=Label(root,text='Volume',font='Impack 25 bold',width=8,bg='#0097A7',fg='#FFFFFF')
volume_lbl.place(x=450,y=410)

Language_combo=ttk.Combobox(root,values=['EN'],font='arial 12 bold',state='r')
Language_combo.place(x=350,y=60)
Language_combo.set('EN')

gender_combo=ttk.Combobox(root,values=['Male','Female'],font='arial 12 bold',state='r')
gender_combo.place(x=10,y=500)
gender_combo.set('Male')

speed_combo=ttk.Combobox(root,values=['Fast','Normal','slow'],font='arial 12 bold',state='r')
speed_combo.place(x=230,y=500)
speed_combo.set('Fast')

scale_level=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=160)
scale_level.place(x=450,y=480)
scale_level.set(50)


r_btn=Button(root,text='Reset',command=Reset)
r_btn.place(x=5,y=600)

play_btn=Button(root,text='Play',command=talk)
play_btn.place(x=203,y=600)

d_btn=Button(root,text='Download',command=download)
d_btn.place(x=400,y=600)

root.configure(bg='#C8E6C9')

root.mainloop()


# In[ ]:





# In[ ]:





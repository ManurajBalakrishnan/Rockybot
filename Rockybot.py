#rocky the bot


from tkinter import *  #this module is used to perform gui operations
from tkinter import messagebox as ms #importing messagebox from tkinter and nameing as ms
import pyttsx3 #this module is used to perform text to speech conversion
import random #this module is used to perform random numbers
import wikipedia #this module is used to get info from wikipedia
from datetime import datetime
import webbrowser #this module is used to perform web-based document to the user
import os #this module is used to perform os operations
import requests #this module is used for http requests


class widget(): # creating a class called widget

#-------------key word list
#-------------these keywords will be used by the bot

    greeting = ['Hey whats up! Buddy','Hello ! I am Rocky.. How can i help you',' Hi ! I am Rocky your assistant','Hi ! How can i help you','Hello Human...I am bot How can i help you']
    name = ['My name is Rocky','you can call me Rocky :)']
    created = ['I was made by Manu using Python ']
    how = ['I am Good...today what about you...!! ','I am great as always..!!','I am fine what about you..!!','I am happy today ..you?']
    can = ['I can do things like opening Apps then i can get you informations from wikipedia and i can say you the date and time,weather and much more  ']
    thanks = ['My pleasure...:)','your are welcome....Human ;)','your are so sweet..:)']
    datu = ["I did not get that",'I was Unable To Understand']


#Engine for bot to speak
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)



#Print function
#this functon prints the Rocky's response on the screen

    def printing_func(robo, out):
        #robo.text_box2.delete(1.0,END)
        robo.text_box1.insert(INSERT,"Rocky: "+out )
        robo.text_box1.insert(INSERT,"\n" )


#speaking functon
#this function speak the rocky's response

    def speaking_func(robo, s):
        robo.engine.say(s)
        robo.engine.runAndWait()

#send function
#this function is used to send userinput to Rocky

    def send_func(robo):
        user_input = robo.search_var.get().lower()
        robo.search_var.set('')
        #robo.text_box1.delete(1.0,END)
        robo.text_box1.insert(INSERT,'You: '+user_input)
        robo.text_box1.insert(INSERT,"\n" )

        if 'about' in user_input and 'you' in user_input:
            out="ok let me Introduce myself i am rocky i will be your assistant ... and i was created by Manuraj using python"
            robo.printing_func(out)
            robo.speaking_func(out)
#name condition
        elif 'name' in user_input:
            r = random.randint(0,len(robo.name)-1)
            out = robo.name[r]
            robo.printing_func(out)
            robo.speaking_func(out)
#you condition
        elif 'you' in user_input:
            if 'who' in user_input and 'are' in user_input:
                r = random.randint(0,len(robo.name)-1) # -1 is used because the end of the string has "/0"
                out = robo.name[r]
                robo.printing_func(out) #calling the Print_func
                robo.speaking_func(out) # calling the speaking_func

            elif 'how are' in user_input:
                r = random.randint(0,len(robo.how)-1)
                out = robo.how[r]
                robo.printing_func(out)
                robo.speaking_func(out)

            elif 'who made' in user_input:
                r = random.randint(0,len(robo.created)-1)
                out = robo.created[r]
                robo.printing_func(out)
                robo.speaking_func(out)

            elif 'do' in user_input:
                out = robo.can[r]
                robo.printing_func(out)
                robo.speaking_func(out)


            else:
                r = random.randint(0,len(robo.datu)-1)
                out = robo.datu[r]
                robo.printing_func(out)
                robo.speaking_func(out)


#thanks condition
        elif 'thanks' in user_input or 'thank' in user_input or 'thankyou' in user_input:
            r = random.randint(0,len(robo.thanks)-1)
            out =robo.thanks[r]
            robo.printing_func(out)
            robo.speaking_func(out)


#hello condition
        elif 'hello' in user_input or 'hi' in user_input:
            r = random.randint(0,len(robo.greeting)-1)
            out = robo.greeting[r]
            robo.printing_func(out)
            robo.speaking_func(out)



#weather condition
        elif 'weather' in user_input:
            try:
                if 'in' in user_input:
                    u = user_input.split()
                    for i in range(0,len(u)):
                        if u[i] == 'in':
                            city = u[i+1]
                    api='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                    url = api+city
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    out = f'Temperture In {city} is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    robo.printing_func(out)
                    robo.speaking_func(out)

            except:
                out = 'I was unable to connect to internet'
                robo.printing_func(out)
                robo.speaking_func(out)


#location condition
        elif 'where' in user_input and 'i' in user_input or 'location' in user_input:
            try:
                r = requests.get('https://ipinfo.io/')
                d = r.text.split()[4]
                out = 'your location is near to ' +d
                robo.printing_func(out)
                robo.speaking_func(out)

            except:
                out = 'i was unable to track ur location......please check your internet connection'
                robo.printing_func(out)
                robo.speaking_func(out)

#open apps condition
        elif 'open' in user_input:
            if 'google' in user_input:
                to_search = user_input
                out = 'Opening Google'
                robo.printing_func(out)
                robo.speaking_func(out)
                webbrowser.open('https://www.google.co.in/search?q=' + to_search)

            elif 'youtube' in user_input:
                to_search = user_input
                out = 'opening youtube'
                robo.printing_func(out)
                robo.speaking_func(out)
                webbrowser.open('https://www.google.co.in/search?q=' + to_search)

            elif 'facebook' in user_input:
                to_search = user_input
                out = 'opening facebook'
                robo.printing_func(out)
                robo.speaking_func(out)
                webbrowser.open('https://www.google.co.in/search?q=' + to_search)


            elif 'paint' in user_input:
                out='Opening Paint'
                robo.printing_func(out)
                robo.speaking_func(out)
                path = r'C:\Windows\System32\mspaint.exe'
                os.startfile(path)

            elif 'notepad' in user_input:
                out='Opening Note Pad'
                robo.printing_func(out)
                robo.speaking_func(out)
                path = r'E:\EXE_FILES\Text_editor\Text_editor.exe'
                os.startfile(path)

            elif 'browser' in user_input or 'chrome' in user_input:
                out = 'Opening Crome Browser'
                robo.printing_func(out)
                robo.speaking_func(out)
                path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(path)

            elif 'cmd' or 'command prompt' in user_input:
                out='Opening Command Prompt'
                robo.printing_func(out)
                robo.speaking_func(out)
                path = r'C:\Windows\System32\cmd.exe'
                os.startfile(path)

            else:
                r = random.randint(0,len(self.datu)-1)
                out = self.datu[r]
                robo.printing_func(out)
                robo.speaking_func(out)

#none condition
        elif user_input == '':
            out = 'You Said Nothing'
            robo.printing_func(out)
            robo.speaking_func(out)

#fine command
        elif 'fine' in user_input or 'good' in user_input or 'great' in user_input:
            out = ('That sounds good.....;')
            robo.printing_func(out)
            robo.speaking_func(out)

#time condition
        elif 'date' in user_input and 'time' in user_input:
            t = datetime.now().strftime('%H hours and %M minutes')
            o = t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')

            out = 'current time is : ' +time
            t2 =datetime.now().strftime("%d/%m/%y")
            out1 = 'Todays date is: ' +t2
            robo.printing_func(out)
            robo.printing_func(out1)
            robo.speaking_func(out)
            robo.speaking_func(out1)

        elif 'time' in user_input:
            t = datetime.now().strftime('%H hours and %M minutes')
            o = t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')

            out = 'current time is : ' +time
            robo.printing_func(out)
            robo.speaking_func(out)

        elif 'date' in user_input:
            t =datetime.now().strftime("%d/%m/%y")
            out = 'Todays date is: ' +t
            robo.printing_func(out)
            robo.speaking_func(out)



#wikipedia condition
        elif 'wikipedia' in user_input:
            w = list(user_input.split())
            w.remove('wikipedia')
            w.remove('in')
            to2 = ''.join(w)

            try:
                #out = 'According To Wikipedia ' + wikipedia.page(to2,2)
                out = 'According To Wikipedia ' + wikipedia.summary(to2, sentences=2)
                robo.printing_func(out)
                robo.speaking_func(out)
            except:
                out='cannot find'
                robo.printing_func(out)
                robo.speaking_func(out)

#os operations like shutdown,restart
        elif 'shutdown' in user_input:
            out = 'shutting down the system'
            robo.printing_func(out)
            robo.speaking_func(out)
            os.system('shutdown -s')
        elif 'restart' in user_input:
            out = 'restarting the system'
            robo.printing_func(out)
            robo.speaking_func(out)
            os.system('shutdown /r /t 1')




        else:

            to_search = user_input
            out = 'I can search that on google, May I?'
            robo.printing_func(out)
            robo.speaking_func(out)

            res = ms.askquestion('Google Search','May I Search That On Google.')

            if res == 'yes':
                out = 'opening Google Search'
                robo.printing_func(out)
                robo.speaking_func(out)
                webbrowser.open('http://www.google.co.in/search?q=' + to_search)
            else:
                out = 'okie'
                robo.printing_func(out)
                robo.speaking_func(out)


#constructer functon

    def __init__(robo):
        robo.win = Tk()
        robo.win.geometry('480x400')
        robo.win.resizable(0,0)
        robo.win.configure(bg='black')


        Label(robo.win, text='Rocky the Bot',font=('arial black',18),fg='green',width=30,bg='black',bd=5).pack()
        #Label(robo.win, text='You' , font=('arial black',20),fg='green',bg='black').place(x=50,y=50)
        #Label(robo.win, text='Rocky' , font=('arial black',20),fg='green',bg='black').place(x=300,y=50)

        robo.text_box1 = Text(robo.win, font=('arial black',13),width=40,height=12,bg='black',fg='green', wrap=WORD )
        robo.text_box1.place(x=10,y=50)

        #robo.text_box2 = Text(robo.win, font=('arial black',13),width=18,height=12,bg='black',fg='green', wrap=WORD )
        #robo.text_box2.place(x=250,y=100)


        robo.search_var = StringVar()
        Entry(robo.win, font=('arial black', 14), bg='black',fg='green',width=25,textvariable=robo.search_var,bd=5).place(x=10,y=350)
        send = Button(robo.win, text='Send', font=('arial black',10),bg='black',fg='green',bd=5,width=10,command=robo.send_func).place(x=370,y=350)

        def enter(*args):
            robo.send_func()

        robo.win.bind('<Return>',enter)

        robo.win.mainloop()

root = widget()

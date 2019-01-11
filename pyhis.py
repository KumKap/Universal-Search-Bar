from tkinter import *

from tkinter import ttk

from  tkinter.scrolledtext  import ScrolledText

import webbrowser

import speech_recognition as sr
root = Tk()

root.title(' Search Bar ')


icon = PhotoImage(file='mics.gif')
root.tk.call('wm', 'iconphoto', root._w, icon)

style = ttk.Style()

style.theme_use('winnative')

photo = PhotoImage(file='mic.png').subsample(15, 15)

label1 = ttk.Label(root, text='Searching:')

label1.grid(row=0, column=0)

entry1 = ttk.Entry(root, width=40)

entry1.grid(row=0, column=1, columnspan=4)

btn2 = StringVar()

def callback():
    if btn2.get() == 'google' and entry1.get() != '':

        webbrowser.open('http://google.com/search?q=' + entry1.get())



    elif btn2.get() == 'flkart' and entry1.get() != '':

        webbrowser.open('http://flipkart.com/search?q=' + entry1.get() + '&otracker=start&as-show=on&as=off')



    elif btn2.get() == 'amz' and entry1.get() != '':

        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + entry1.get())



    elif btn2.get() == 'ytb' and entry1.get() != '':

        webbrowser.open('https://www.youtube.com/results?search_query=' + entry1.get())



    else:

        pass


def get(event):
    if entry1.get() != '':
        f = open('history.txt', 'a+')
       
    if btn2.get() == 'google' and entry1.get() != '':

        webbrowser.open('http://google.com/search?q=' + entry1.get())
        f.write(' ')
        f.write('http://google.com/search?q=' + entry1.get()+"\n")


    elif btn2.get() == 'flkart' and entry1.get() != '':

        webbrowser.open('http://flipkart.com/search?q=' + entry1.get() + '&otracker=start&as-show=on&as=off')
        f.write('http://flipkart.com/search?q=' + entry1.get() + '&otracker=start&as-show=on&as=off'+"\n")


    elif btn2.get() == 'amz' and entry1.get() != '':

        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + entry1.get())
        f.write('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + entry1.get()+"\n")


    elif btn2.get() == 'ytb' and entry1.get() != '':

        webbrowser.open('https://www.youtube.com/results?search_query=' + entry1.get())
        f.write('https://www.youtube.com/results?search_query=' + entry1.get()+"\n")


    else:
        pass
    f.close()

def his():
    i=1
    dd=Tk()
    dd.title('History')
    dd.iconbitmap('his.ico')
    txt = ScrolledText(dd, undo=True, height=15, width=30)
    txt['font'] = ('consolas', '12')
    f = open('history.txt', 'r')
    while (1):
        line = f.readline()
        test=str(i)+"."
        test=test+line
        if (line == ""):
            break
        if ( line=="\n"):
            continue
        txt.insert('end', test)
        i=i+1
    f.close()
    txt.pack(expand=True, fill='both')


def buttonClick():
    pass
    
    r = sr.Recognizer()

    r.pause_threshold = 0.7

    r.energy_threshold = 400

    with sr.Microphone() as source:

        try:

            audio = r.listen(source, timeout=5)

            message = str(r.recognize_google(audio))

            entry1.focus()

            entry1.delete(0, END)

            entry1.insert(0, message)
            if message != '':
                f = open('history.txt', 'a+')
                

            if btn2.get() == 'google':

                webbrowser.open('http://google.com/search?q=' + message)
                f.write('http://google.com/search?q=' + message+"\n")


            elif btn2.get() == 'flkart':

                webbrowser.open('http://flipkart.com/search?q=' + message + '&otracker=start&as-show=on&as=off')
                f.write('http://flipkart.com/search?q=' + message + '&otracker=start&as-show=on&as=off'+"\n")


            elif btn2.get() == 'amz':

                webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + message)
                f.write('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + message+"\n")


            elif btn2.get() == 'ytb':

                webbrowser.open('https://www.youtube.com/results?search_query=' + message)
                f.write('https://www.youtube.com/results?search_query='  + message+"\n")


            else:

                pass
            f.close()


        except sr.UnknownValueError:

            print('Google Speech Recognition could not understand audio')



        except sr.RequestError as e:

            print('Could not request results from Google Speech Recognition Service')



        else:
            pass




entry1.bind('<Return>', get)

MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)

MyButton1.grid(row=0, column=6)

MyButton7 = ttk.Button(root, text='History', width=12, command=his)

MyButton7.grid(row=1, column=6)

MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)

MyButton2.grid(row=1, column=1, sticky=W)

MyButton3 = ttk.Radiobutton(root, text='Flkrt', value='flkart', variable=btn2)

MyButton3.grid(row=1, column=2, sticky=W)

MyButton4 = ttk.Radiobutton(root, text='Amz', value='amz', variable=btn2)

MyButton4.grid(row=1, column=3)

MyButton5 = ttk.Radiobutton(root, text='Ytb', value='ytb', variable=btn2)

MyButton5.grid(row=1, column=4, sticky=E)

MyButton6 = Button(root, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove',
                   relief='sunken')

MyButton6.grid(row=0, column=5)

entry1.focus()

root.wm_attributes('-topmost', 1)

btn2.set('google')

root.mainloop()

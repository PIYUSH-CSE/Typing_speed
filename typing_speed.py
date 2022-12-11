# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:00:09 2022

@author: Pro_Asus
"""
import tkinter as tkt
from tkinter import *
from PIL import ImageTk, Image
import random
from timeit import default_timer as timer


def Game():
    global x
    if x == 0:
        window.destroy()
        x = x + 1

    def Start():
        global start
        start = timer()
        b4.configure(bg='#09f705')
        b2.configure(state='normal')
        x4 = Label(windows, text='Timer Started...', bg='black', fg='#09f705', font='times')
        x4.place(x=350, y=110)

    def result():
        end = timer()
        original_word = words[word].split()
        user_word = (text.get(1.0, "end-1c")).split()
        if words[word] == text.get(1.0, "end-1c"):

            count = 0

            for i in range(len(original_word)):
                try:
                    if user_word[i] == original_word[i]:
                        count += 1
                except:
                    pass
            final_time = end - start
            accuracy = (count / len(original_word)) * 100
            wpm = len(text.get("1.0", 'end-1c')) * 60 / (5 * final_time)

            x3 = Label(windows, text='Time taken: ' + str(final_time) + ' sec' + '\nAccuracy: ' + str(
                accuracy) + '\nWpm: ' + str(wpm), bg='black', fg='white', font='times 15 bold')
            x3.place(x=165, y=270)


        else:
            count = 0
            for i in range(len(original_word)):
                try:
                    if user_word[i] == original_word[i]:
                        count += 1
                except:
                    pass

            accuracy = (count / len(original_word)) * 100
            final_time = end - start
            x3 = Label(windows, text='!!! Incorrect Sentence !!!' + '\nTime Taken: '+str(final_time)+'sec' + '\nAccuracy: ' + str(accuracy), bg='black',
                       fg='red', font='times 15 bold')
            x3.place(x=150, y=270)

    words = ['a short story is a piece of prose fiction that typically can be read in one sitting',
             'the short story is a crafted form in its own right.',
             'determining what exactly defines a short story has been recurrently problematic.',
             'some authors have argued that a short story must have a strict form.',
             'its never been done before and thats kind of the spirit everybodys taking it in',
             'president of Production for Marvel Studios, on constructing a shared film universe.']

    word = random.randint(0, (len(words) - 1))
    # start = timer()
    windows = Tk()
    windows.resizable(0, 0)
    windows.geometry('600x500')
    windows.config(bg='black')
    x2 = Text(windows, font="times 15", width=50, height=3, bg='black', fg='#f7f305', wrap="word")
    x2.place(x=40, y=10)
    x2.insert(1.0, words[word])
    x2.configure(state='disabled')
    x2.tag_configure("center", justify='center')
    x2.tag_add("center", 1.0, "end")
    x3 = Label(windows, text="Type the given sentence", font="times", bg='black', fg='red')
    x3.place(x=30, y=110)
    text = Text(windows, width=50, height=3, bg='black', fg='green', insertbackground="white", font='times 15',
                wrap="word")
    text.place(x=40, y=140)
    b2 = Button(windows, text='Done', command=result, width=12, bg='grey')
    b2.place(x=180, y=220)
    b2.configure(state='disabled')
    b3 = Button(windows, text='Exit', command=windows.destroy, width=12, bg='grey')
    b3.place(x=300, y=220)
    b4 = Button(windows, text='Start', command=Start, width=12, bg='grey')
    b4.place(x=230, y=110)

    windows.mainloop()


window = Tk()
start = 0
window.title('Speedometer')
window.geometry("450x250")
window.resizable(0, 0)
window.config(bg='yellow')
#img = Image.open("C:\\Users\\Pro_Asus\\Desktop\\python projects\\shutterstock_554314555_copy.jpg")
#bgk = ImageTk.PhotoImage(img)
#x0 = Label(window, image=bgk)
#x0.place(x=0, y=0)
#window.wm_attributes('-transparentcolor', '#ab23ff')

x = 0
x1 = Label(window, text='Welcome to Speedometer', font='times 20 bold', bg='yellow')
x1.place(x=80, y=50)
b1 = Button(window, text='Go', command=Game, width=12, bg='grey')
b1.place(x=180, y=120)

window.mainloop()
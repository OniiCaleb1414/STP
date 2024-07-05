import tkinter as tk
from tkinter import *
root = Tk()
root.title("Chatbot")
def send():
    send = " "+e.get()
    txt.insert(END, " "+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, " " + "Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, " " + "Hello ")
    elif(e.get() == "how are you"):
        txt.insert(END, " " + " fine! and you ")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, " " + " Great! how can I help you. ")
    else:
        txt.insert(END, " " + " Sorry! I didn't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
} 

import nltk
from nltk.chat.util import Chat, reflections

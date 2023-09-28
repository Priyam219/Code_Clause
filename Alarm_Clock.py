import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time, winsound


def createWidgets():

    label1 = Label(window, text="enter the time in hh:mm - ")
    label1.grid(row=0 , column=0, padx=5, pady=5)

    global entry1
    entry1 = Entry(window, width=15)
    entry1.grid(row=0, column=1)

    label2 = Label(window, text="Enter the message - ")
    label2.grid(row=1 , column=0, padx=5, pady=5)

    global entry2
    entry2 = Entry(window, width=15)
    entry2.grid(row=1, column=1)

    button = Button(window, text="Submit", width=10, command=submit)
    button.grid(row=2, column=1)

    global label3
    label3 = Label(window, text="")
    label3.grid(row=3,column=0)

def message1():

    global label3, entry1
    AlarmtimeLabel = entry1.get()
    label3.configure(text = "The alarm is counting ...")
    messagebox.showinfo("Alarm time is",f"The alarm time is : {AlarmtimeLabel}")

def submit():

    global entry1, entry2, label3
    Alarmtime = entry1.get()
    message1()
    CurrentTime = time.strftime("%H:%M")
    AlaemMessage = entry2.get()
    print(f"The alarm time is : {Alarmtime}")
    while Alarmtime != CurrentTime:
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime == CurrentTime:
        print("Playing Alarm Sound...")
        winsound.PlaySound("*", winsound.SND_ASYNC)
        label3.config(text="Alarm sound playing >>>>><<<<<<")
        messagebox.showinfo("Alarm message",f"The message is : {AlaemMessage}")

window = tk.Tk()
window.title("Alarm Clock")
window.geometry("400x150")

createWidgets()
window.mainloop()
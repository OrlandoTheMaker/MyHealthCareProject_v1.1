import tkinter
from tkinter import *
import os
import time
import sys
import googlesearch
import pyttsx3
import speech_recognition as sr

# Initialize speech recognition
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()


# This message gets printed on the screen once the app is opened
def user_guide(text):
    if len(text) > 0:
        label.config(text=label.cget("text") + text[0])
        app.after(100, user_guide, text[1:])


def process_user_input():
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        engine.say("Recognizing, plase hold on.")
        time.sleep(3)
        text = r.recognize_google(audio)
        engine.say('You Said' + text)

        # Perform tasks based on user input
        if "hello" in text:
            response = "Hello! How can I assist you?"
        elif "weather" in text:
            response = "The weather is sunny today."
        else:
            response = "I'm sorry, I couldn't understand. Can you please repeat?"

        # Speak the response
        engine.say(response)
        engine.runAndWait()

        # Update the label with the response
        label.config(text=label.cget("text") + "\nUser said: " + text + "\nAssistant: " + response)


    except sr.UnknownValueError:

        print("Speech Recognition could not understand audio")

        engine.say("I'm sorry, I couldn't understand what you said. Can you please repeat?")

        engine.runAndWait()


    except sr.RequestError as e:

        print("Could not request results from Speech Recognition service; {0}".format(e))

        engine.say("Sorry, there was an issue with the Speech Recognition service. Please try again later.")

        engine.runAndWait()


def antonio():
    # Add your code here to handle the tasks of the health care assistant

    # Example: Speak a welcome message
    engine.say("Hello, glad you're here, please tell me how i can be of assistant to you today.")
    engine.runAndWait()

    # Example: Perform some tasks based on user input
    # ...
    process_user_input()


# Tkinter initialization
app = tkinter.Tk()
app.geometry('1300x750')
app.title("Health Care Assistant")
app.config(bg='dodgerblue')
app.resizable(True, True)

# -- The Label Where Text Gets Printed -- #
frame = Frame(app, width=300, height=70)
frame.pack()

label = Label(app, text="")
label.pack()


def test():
    top = Frame(app, width=1300, height=70, bd=8, relief="raised")
    top.place(x=0, y=0)
    # -- the name in the frame --
    name = Label(app, text="AI Health Care Assistant", width=30, height=2, font=("Lucida Console", 14, "italic"))
    name.place(x=450, y=0)
    # --button--
    launchMe = Button(app, text="Launch Me!", width=20, height=3, activebackground='black', activeforeground='white',
                      command=antonio)
    launchMe.config(fg='green')
    launchMe.place(x=1100, y=650)

def exit():
    sys.exit(0)

cancel = Button(app, text="Cancel!", width=20, height=3, activebackground='red', activeforeground='black', command=exit())
cancel.config(fg='red')
cancel.place(x=0, y=650)


test()
user_guide("Kindly click the 'Launch Me!' button below\n")

app.mainloop()

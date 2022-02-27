# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:09:46 2022

@author: SAI
"""

import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as data_taker:
     print("Say Something")
    voice = listener.listen(data_taker)
    instruct = listener.recognize_google(voice)
    instruct = instruct.lower()
    print(instruct)
except:
    pass
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as data_taker:
     print("Say Something")
    voice = listener.listen(data_taker)
    instruct = listener.recognize_google(voice)
    instruct = instruct.lower()
    print(instruct)
    if'Max' in instruct:
        print(instruct)
except:
    pass
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Who are u? ')
engine.say('What is your name')
engine.say('what is your favourite color? ')
engine.say('How old you are ?')
engine.runAndWait()

try:
    with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        print(instruct)
        if'Max' in instruct:
            print(instruct)
except:
    pass





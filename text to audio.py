import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)  
engine.setProperty('volume', 1) 

text = "it's monday tomorrow and again back to normal!"

engine.say(text)

engine.runAndWait()
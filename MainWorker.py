import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
print("Tip: 0 ist die default voice")
print("Voice id:")
input1 = int(input())

friday = pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[input1].id)


def speak(audio):
    print('Asistant: ' + audio)
    friday.say(audio)
    friday.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak("It is")
    speak(Time)


def welcome():
    voices = friday.getProperty('voices')

    for voice in voices:
        # to get the info. about various voices in our PC
        print("Voices on your pc:")
        print("")
        print("Voice:")
        print("ID: %s" % voice.id)
        print("Name: %s" % voice.name)
        print("Age: %s" % voice.age)
        print("Gender: %s" % voice.gender)
        print("Languages Known: %s" % voice.languages)
        print("")
        print("")
        print("")
        print("")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        #c.pause_threshold = 1
        audio = c.listen(source)
        print("log- Starting.")
    try:
        query = c.recognize_google(audio, language='de-GE')
        print("Boss: " + query)
        print("log- successfull")
        return query
    except sr.UnknownValueError:
        #print('Sorry sir! I didn\'t get that! Try typing the command!')
        #query = str(input('Your order is: '))
        print("log- No input or not understood, going to start.")
        command()




if __name__ == "__main__":
    welcome()

    while True:
        query = command()
        #c_query = query.lower()
        # All the command will store in lower case for easy recognition
        speak(f'{query}')



import speech_recognition as sr
import requests, datetime
import pyttsx3

def happy_speaks(s):
    engine = pyttsx3.init()
    engine.say(s)
    engine.runAndWait()

url = "https://www.google.com"
timeout = 5
ts = datetime.datetime.now()

happy_speaks("Hello Sir! Happy here")
print("Engine Stars:", ts)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    happy_speaks('Please Say Somthing!')
    print('Please Say Somthing!')
    audio = r.listen(source)

try:
    request = requests.get(url, timeout=timeout)
    print("Connected to inernet")
    happy_speaks("Connected to internet")
    try:
        print("You said " + r.recognize_google(audio))
        happy_speaks('You Said'+ r.recognize_google(audio))
    except sr.UnknownValueError:
        happy_speaks("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        happy_speaks("Could not request results from Google Speech Recognition service; {0}".format(e))

except (requests.ConnectionError, requests.Timeout) as exception:
    happy_speaks("No internet connection.")
    try:
        happy_speaks("You said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        happy_speaks("Sphinx could not understand audio")
    except sr.RequestError as e:
        happy_speaks("Sphinx error; {0}".format(e))

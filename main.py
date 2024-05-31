import pyttsx3 as p
import speech_recognition as sr

from Google import infow1
from News import news
from YT_auto import music
from selenium_web import infow
import randfacts
from jokes import *
from weather import *
import datetime
from Spotify import music1
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()



r = sr.Recognizer()

def WishMe():
    hour = (datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return(" Good Morning")
    elif hour>=12 and hour<16:
        return(" Good Afternoon")
    else:
        return(" Good Evening")

speak("Hello sir,"+ WishMe() + "I m your voice assistant. how are you?")

with sr.Microphone() as source :

    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    
    audio = r.listen(source)

    
    text = r.recognize_google(audio)
    print(text)


if "what" and "about" and "you" in text:
    speak("I am also having a good day sir")
speak("What can i do for you") 


with sr.Microphone() as source :

    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    
    audio = r.listen(source)

    
    text2 = r.recognize_google(audio)
    print(text2)

if "information" in text2:
    speak("You need information related to which topic?")

    with sr.Microphone() as source :
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
    
        audio = r.listen(source)

    
        infor = r.recognize_google(audio)
    print("searching {} in wikipedia".format(infor))
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)


elif "play" and "video" in text2:
     speak("You want me to play which video?")
     with sr.Microphone() as source :
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
    
        audio = r.listen(source)
        #text2 = r.recognize_google(audio)

    
        vid = r.recognize_google(audio)
     print("Playing {} on Youtube".format(vid))
     speak("Playing {} on Youtube".format(vid))
     assist = music()
     assist.play(vid)




elif "news" in text2:
    print("Sure sir now i will read news for you")
    speak("Sure sir now i will read news for you")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i]) 
        

elif "fact" and "facts" in text2:
    speak("Sure Sir,")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that. " + x)



elif "joke" and "jokes" in text2:
    speak("Sure sir, get ready for some chuckles!")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "temperature" and "weather" in text2:
    print("Hello sir the temprature in Jaipur is " + str(temp()) + "and with  "  + str(des()))
    speak("Hello sir the temprature in Jaipur is " + str(temp()) + "and with"  + str(des()))



elif "date" and "time" in text2:
    speak("Sure Sir,")
    today_date = datetime.datetime.now()
   # print(today_date)
    print("Today is" + today_date.strftime("%d")  + "of" + today_date.strftime("%B") + ". And its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%S")) + (today_date.strftime("%p")) )
    speak("Today is" + today_date.strftime("%d")  + "of" + today_date.strftime("%B") + ". And its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%S")) + (today_date.strftime("%p")) )


elif "song" and "spotify" in text2:
     speak("You want me to play which song?")
     with sr.Microphone() as source :
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
    
        audio = r.listen(source)
        #text2 = r.recognize_google(audio)

    
        vid1 = r.recognize_google(audio)
     print("Playing {} on Spotify".format(vid1))
     speak("Playing {} on Spotify".format(vid1))
     assist = music1()
     assist.play1(vid1)

else :
    speak("You need information related to which topic?")

    with sr.Microphone() as source :
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
    
        audio1 = r.listen(source)

    
        infor1 = r.recognize_google(audio1)
    print("searching {} in google".format(infor1))
    speak("searching {} in google".format(infor1))
    assist = infow1()
    assist.get_info1(infor1)
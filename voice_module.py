import pyttsx3
import random

friday = pyttsx3.init('sapi5')
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id)

happy = ['thank you ,sir', 'you are so lovely ,sir']

apologize_accept = ['its ok but i im still angry,sir','but you always do this,sir',]

angry = ['i will not accept such kind of behaviour,sir', "don't cross your limit,sir",'im warning you sir dont speak with me with such rubbish language']

max_angry = ["you are too much,sir", "you dont have sense to speak with me,sir"]

no_need = ["im not angry its ok,sir"]


def friday_speak(n):
    friday.say(n)
    friday.runAndWait()


def friday_angry():
    m = random.choice(angry)
    print(m)
    friday_speak(m)



def friday_happy():
    n = random.choice(no_need)
    print(n)
    friday_speak(n)



def friday_quit():
    n = random.choice(max_angry)
    print(n)
    friday_speak(n)
    friday_offline()



def friday_offline():
    n="bye,Friday is offline"
    print(n)
    friday_speak(n)


def apolo_accept():
    n = random.choice(apologize_accept)
    print(n)
    friday_speak(n)


def friday_love():
    n = random.choice(happy)
    print(n)
    friday_speak(n)
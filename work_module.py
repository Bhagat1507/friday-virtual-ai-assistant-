import datetime
import webbrowser
import os
from voice_module import friday_speak
import smtplib
import wikipedia
import pywhatkit as pwt
import psutil
from voice_module import *

hour = datetime.datetime.now()
hour1 = hour.hour


def wish_me():
    if 0 <= hour1 < 12:
        friday_speak("Good morning,sir...")
    elif 12 <= hour1 < 18:
        friday_speak("Good afternoon,sir...")
    else:
        friday_speak("Good evening,sir...")


def date_module():
    date = hour.date()
    print(date)
    friday_speak(date)


def play_music():
    music_dir = 'C:\\Users\\amals\\Music'
    songs = os.listdir(music_dir)
    # print(songs)
    os.startfile(os.path.join(music_dir, songs[1]))


def open_shell():
    shell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    os.startfile(shell_path)


def open_rstudio():
    r_path = "C:\\Program Files\\RStudio\\bin\\rstudio.exe"
    os.startfile(r_path)


def open_pycharm():
    py_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe"
    os.startfile(py_path)


def open_google():
    webbrowser.open('https://www.google.com/')


def open_youtube():
    webbrowser.open('https://www.youtube.com/')


def open_website():
    webbrowser.open('https://psycoder1.wordpress.com/')


def open_hackerrank():
    webbrowser.open('https://www.hackerrank.com/access-account/')


def open_linkedin():
    webbrowser.open('https://www.linkedin.com/feed/')


def open_github():
    webbrowser.open('https://github.com/')


def send_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adibhagat1011@gmail.com', '9172180096')
    server.sendmail('adibhagat1011@gmail.com', to, content)
    server.close()


def try_mail():
    try:
        content = input('>> ')
        to = "snehalbhagat0595@gmail.com "
        send_mail(to, content)
        print("Email has been sent!")
    except Exception as e:
        print(e)
        print("Sorry error")


def open_excel():
    excel_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
    os.startfile(excel_path)


def open_powerpoint():
    ppt_path = 'C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE'
    os.startfile(ppt_path)


def open_cmd():
    cmd_path = 'C:\\Windows\\system32\\cmd.exe'
    os.startfile(cmd_path)


# pwt.sendwhatmsg("+917776018612","hello this is friday..",20,0)


def open_wikipedia(n):
    n = n.replace("search", "")
    n = n.replace("friday", "")
    results = wikipedia.summary(n, sentences=2)
    friday_speak("According to Wikipedia")
    print(results)
    friday_speak(results)


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def battery_info():
    battery = psutil.sensors_battery()
    bat_perc = battery.percent
    p = "The is Battery "+str(bat_perc)+" percent charge."
    print(p)

    t = battery.power_plugged
    t1 = "Battery charging status "+str(t)
    print(t1)
    if t == False:
        o = "Run time of battery is "
    else:
        o = 'Battery will fully charge in '


    battery_left = convertTime(battery.secsleft)
    x = (battery_left[:])
    y = x.split(':')
    r = (o+str(y[0])+" hours "+str(y[1])+' minutes and '+str(y[2])+' seconds')
    print(r)
    friday_speak(p)
    friday_speak(t1)
    friday_speak(r)

def friday_help():
    # print("____________________________________")
    # print('each command should contain friday')
    # print("open google")
    # print("open youtube")
    # print("open linkedin")
    # print("open website")
    # print("open github")
    # print("open hackerrank")
    # print("play songs")
    # print("r studio")
    # print("date")
    # print("power shell")
    # print("cmd")
    # print("battery")
    # print("search")
    # print("bye friday to quit")
    # print("____________________________________")
    print('''
______________________________________________
each command should contain friday in it.
friday open google - this command will open google
friday open youtube - this command will open youtube
friday open linkedin - this command will open linkedin
friday open github - this command will open github
friday open hackerrank - this command will open hackerrank
friday play songs - this command will play songs
friday open r studio - this command will open R-studio editor
friday what date is today - this command will tell current date
friday open power shell - this command will open power-shell
friday open cmd - this command will open command prompt
friday what is battery status - this command will tell the status of your device
friday search about "topic" - this command will search about topic and tell you
bye friday - this command will quit the program
______________________________________________''')











from work_module import *
from voice_module import *
from listen_module import *


def friday_work():
    bad_word = ['fuck', 'moron', 'bitch']
    appo_word = ['sorry']
    love_word = ['love you', 'you are the best']
    bw = 0

    while True:
        command = takeCommand().lower()
        understand = False
        n = bad_word[:] + appo_word[:] + love_word[:]
        cmd = command.split(" ")
        if 'friday' in command:
            for i in bad_word:
                if i in command:
                    friday_angry()
                    bw += 1
            for i in appo_word:
                if i in command:
                    if bw > 0:
                        apolo_accept()
                        bw -= 1
                    elif bw == 0:
                        friday_happy()
            for i in love_word:
                if i in command:
                    if bw == 0:
                        friday_love()
                    else:
                        friday_happy()
                        bw = 0

            if bw >= 3:
                friday_quit()
                break

            print(bw)

            if "google" in command:
                open_google()
                understand = True
            elif "youtube" in command:
                open_youtube()
                understand = True
            elif "github" in command:
                open_github()
                understand = True
            elif "my website" in command:
                open_website()
                understand = True
            elif "hackerrank" in command:
                open_hackerrank()
                understand = True
            elif "linkedin" in command:
                open_linkedin()
                understand = True
            elif "play songs" in command:
                play_music()
                understand = True
            elif "r studio" in command:
                open_rstudio()
                understand = True
            elif "hi friday" in command:
                wish_me()
                understand = True
            elif "date" in command:
                date_module()
                understand = True
            elif "power shell" in command:
                open_shell()
                understand = True
            elif "cmd" in command:
                open_cmd()
                understand = True
            elif "excel" in command:
                open_excel()
                understand = True
            elif "ppt" in command:
                open_powerpoint()
                understand = True
            elif "battery" in command:
                battery_info()
                understand = True
            elif "search" in command:
                open_wikipedia(command)
                understand = True
            elif "bye" in command:
                friday_speak("Bye sir..")
                friday_speak("friday is offline")
                understand = True
                break
            else:
                for i in cmd:
                    for j in n:
                        if i in j:
                            understand = True
            if not understand:
                n = "I dont understand what are you trying to say ,sir"
                print(n)
                friday_speak(n)

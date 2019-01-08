# This Python file uses the following encoding: utf-8

# Függvénykönyvtárak betöltése:
from sense_hat import SenseHat # uncomment on rPI
import pygame #pygame eseménykezelés miatt
from pygame.mixer import music as mp3 #zene lejátszáshoz
import os # mappa(ák) fájl(ok) kezelése
import time # log timestamp miatt
import datetime # log timestamp miatt
from time import sleep
import random # shuffle funkció miatt
import sys # csript mappájának meghatározása, szolgáltatásként futattva (sys.path[0])

# LOG FIle kezelés:
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H.%M.%S')
logpath=os.path.join(sys.path[0], "log", "rPI_music_box_")+timestamp+".log"
def newlogline(string):
    with open(logpath, "a") as log:
        log.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+" - ")
        log.write(string+"\n")

# Változók és konstansok definiálása:
index=0 # első zeneszám beállítása
vol=0.5 # kezdeti nagerő érték
playing = "" # kezdeti lejtászás státusz

g = (0, 100, 0) # Green
b = (0, 0, 0) # Black

musicpath=os.path.join(sys.path[0], "music") # platform függtlen elérési út definiálása
l = [] # számok listája

SONG_END = pygame.USEREVENT + 1 # szám vége esemény definiálása
mp3.set_endevent(SONG_END)

# Fügvények:
def displayCL(): #conslo-ra és logba írás egyszerűsítése
    global l
    global index
    newlogline("Playing:")
    newlogline(l[index])
    print("Playing:")
    print(l[index])  
    print("Next:")
    newlogline("Next:")
    if index == lSize-1: # index határérték kezelése
        print(l[0])
        newlogline(l[0])
    elif index < 0:
        print(l[lSize-1])
        newlogline(l[lSize-1])
    else:
        print(l[index+1])
        newlogline(l[index+1])

def play_pause():
    global playing
    if playing == True:
        mp3.pause()
        playing = False
        print("Paused")
        newlogline("Paused")
        displayH("pause")
    elif playing == False:
        mp3.unpause()
        playing = True
        displayCL()
        displayH("play")
    else:
        mp3.load(l[index])  # az első szám betöltése
        mp3.play()
        playing = True
        displayH("play")
        displayCL()

def next():
    global index
    global playing
    displayH("next")
    mp3.load(l[index])
    mp3.play()
    playing = True
    displayCL()
    sleep(1)
    displayH("play")

def previous():
    global index
    global playing
    displayH("previous")
    mp3.load(l[index])
    mp3.play()
    playing = True
    displayCL()
    sleep(1)
    displayH("play")

def shuffle(): #5 zene lista megkeverése
    global playing
    global index
    random.shuffle(l)
    index = 0
    mp3.load(l[index])
    mp3.play()
    playing = True
    displayH("shuffle") # uncomment on rPI
    newlogline("rPI Shuffled")
    print("rPI Shuffled")
    displayCL()
    sleep(1)
    displayH("play") # uncomment on rPI

def volup():
    global vol
    global playing
    vol += 0.02
    mp3.set_volume(vol)
    #cvol = mp3.get_volume()
    newlogline("Volume up")
    print(mp3.get_volume())
    sense.show_letter("+",text_colour=g,back_colour=b)
    sleep(0.3)
    if playing == False:
        displayH("pause")
    elif playing == True:
        displayH("play")
    else:
        displayH("smile")

def voldown():
    global vol
    global playing
    vol -= 0.02
    mp3.set_volume(vol)
    #cvol = mp3.get_volume()
    newlogline("Volume down")
    print(mp3.get_volume())
    sense.show_letter("-",text_colour=g,back_colour=b)
    sleep(0.3)
    if playing == False:
        displayH("pause")
    elif playing == True:
        displayH("play")
    else:
        displayH("smile")

def displayH(action): # logók mghivása
    sense.clear()
    if action == "play":
        pixels = [
            b, b, b, b, b, b, b, b,
            b, b, g, b, b, b, b, b,
            b, b, g, g, b, b, b, b,
            b, b, g, g, g, b, b, b,
            b, b, g, g, b, b, b, b,
            b, b, g, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b
        ]
    elif action == "pause":
        pixels = [
            b, b, b, b, b, b, b, b,
            b, g, g, b, g, g, b, b,
            b, g, g, b, g, g, b, b,
            b, g, g, b, g, g, b, b,
            b, g, g, b, g, g, b, b,
            b, g, g, b, g, g, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b
        ]
    elif action == "next":
        pixels = [
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, g, b, b,
            b, g, b, b, b, g, g, b,
            b, g, g, b, b, g, g, g,
            b, g, g, g, b, g, g, b,
            b, g, g, b, b, g, b, b,
            b, g, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b
        ]
    elif action == "previous":
        pixels = [
            b, b, b, b, b, b, b, b,
            b, b, g, b, b, b, b, b,
            b, g, g, b, b, b, g, b,
            g, g, g, b, b, g, g, b,
            b, g, g, b, g, g, g, b,
            b, b, g, b, b, g, g, b,
            b, b, b, b, b, b, g, b,
            b, b, b, b, b, b, b, b
        ]
    elif action == "shuffle":
        pixels = [
            b, b, b, b, b, b, g, b,
            b, b, b, b, g, g, g, g,
            g, g, b, g, b, b, g, b,
            b, b, g, b, b, b, b, b,
            b, b, g, b, b, b, b, b,
            g, g, b, g, b, b, g, b,
            b, b, b, b, g, g, g, g,
            b, b, b, b, b, b, g, b
        ]
    elif action == "smile":
        pixels = [
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, g, b, g, b, b, b,
            b, b, b, b, b, b, b, b,
            b, g, b, b, b, g, b, b,
            b, b, g, g, g, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b
        ]
    sense.set_pixels(pixels)

# Zeneszámok betöltése, rendezése, lejátszó inicializálása
if os.path.isdir(musicpath) == True: # zene könyvtár meglétének ellenőrzése
    print("==========================================")
    print("The music folder exists")
    print("==========================================")
    newlogline(("=========================================="))
    newlogline("The music folder exists")
    newlogline("==========================================")
    os.chdir(musicpath) # könyvtár váltás, hogy ne kelljen elérési utat definiálni a zenék lejátszásakor
    for files in os.listdir(musicpath): # zene könyvtár listázása
        if files.endswith(".mp3"): # mp3 kiterejsztésű fájlokra szűrés
            l.append(files) # lejatászi lista létrehozása
            print(files)
            newlogline(files)
    l.sort() # számok sorba rendezése
    lSize=len(l) # számok darabszámának tárolása
    newlogline("")
    newlogline("==========================================")
    print("")
    print("==========================================")

    """#START - PyGame event handler (ideiglenes SenseHat helyett)
    import sys # GUI kilépéshez
    pygame.display.init()
    screen = pygame.display.set_mode ( ( 320 , 240 ) )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("==========================================")
                if event.key == ord ( "đ" ):
                    print("Volume up") # Fel
                    volup()
                elif event.key == ord ( "Ē" ):
                    print("Volume down") # Le
                    voldown()
                elif event.key == ord ( "p" ):
                    play_pause() # P
                elif event.key == ord ( "Ĕ" ):
                    index -= 1
                    if index < 0:
                        index = lSize-1
                    print(index) # RPI-n nem kell
                    previous() # Bal
                elif event.key == ord ( "ē" ):
                    index += 1
                    if index == lSize:
                        index = 0
                    print(index) #RPI-n nem kell
                    next() # Jobb
                elif event.key == ord ( "s" ):
                    shuffle() # S
            elif event.type == SONG_END: # szám végének figyelése
                print("==========================================")
                print("The song ended!")
                index += 1
                if index == lSize:
                    index = 0
                print(index) #RPI-n nem kell
                next() # Jobb
    #END - PyGame event handler (ideiglenes SenseHat helyett)"""
    #START - SenseHat event handler
    sense = SenseHat() # semse Hat inicializálása
    # SYSTEMD BugFix
    import signal
    def handler(signum, frame):
        pass
        
    try:
        signal.signal(signal.SIGHUP, handler)
    except AttributeError:
        pass
    #_________________
    pygame.init() # pygame importált moduljaninak inicializálása
    mp3.set_volume(vol) # kezdeti hangerő beállítása
    sense.show_message("Welcome! Lets start listening...", scroll_speed=0.08, text_colour=g, back_colour=b) # üdvözlő üzenet
    displayH("smile") # smile jelzi, hogy betöltött a program
    while True:
        acceleration = sense.get_accelerometer_raw() # gyorsulámérő gyers adatok lekérése
        x = abs(acceleration['x'])
        y = abs(acceleration['y'])
        z = abs(acceleration['z'])
        if x > 2 or y > 2 or z > 2: # az eszköz "rázásának" érzékelése
            newlogline("==========================================")
            print("==========================================")
            shuffle()
        else:
            for event in sense.stick.get_events(): # senseHat események figyelése
                if event.action == "pressed":
                    newlogline("==========================================")
                    print("==========================================")
                    if event.direction == "up":
                        volup()
                    elif event.direction == "down":
                        voldown()
                    elif event.direction == "left":
                        index -= 1
                        if index < 0: # index határérték kezelése
                            index = lSize-1
                        previous()
                    elif event.direction == "right":
                        index += 1
                        if index == lSize: # index határérték kezelése
                            index = 0
                        next()
                    elif event.direction == "middle":
                        play_pause()
            for event in pygame.event.get(): # pygame események figyelése
                if event.type == SONG_END: # szám végének figyelése
                    newlogline("==========================================")
                    newlogline("The song ended!")
                    print("==========================================")
                    print("The song ended!")
                    index += 1
                    if index == lSize: # index határérték kezelése
                        index = 0
                    next()
    #END - SenseHat event handler
else:
    newlogline("The music folder is not exists")
    print("The music folder is not exists")

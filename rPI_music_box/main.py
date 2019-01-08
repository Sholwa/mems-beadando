# This Python file uses the following encoding: utf-8
# # senseHat (eszköz tesztelése)
#   függvénykönyvtárak betöltése
from sense_hat import SenseHat # uncomment on rPI
import pygame #zene lejátszáshoz
from pygame.mixer import music as mp3 #zene lejátszáshoz
import os # mappa(ák) fájl(ok) kezelése
from time import sleep
import random # shuffle funkció miatt

# Változók és konstansok definiálása:
index=0 # első zeneszám beállítása
vol=0.5 # kezdeti nagerő érték
playing = "" # kezdeti lejtászás státusz

g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

musicpath=os.path.join(sys.path[0], "music")
l = [] # számok listája

SONG_END = pygame.USEREVENT + 1 # szám vége esemény definiálása
mp3.set_endevent(SONG_END)
def play_pause():
    global playing
    if playing == True:
        mp3.pause()
        playing = False
        print("Paused")
        displayH("pause") # uncomment on rPI
    elif playing == False:
        mp3.unpause()
        playing = True
        print("Playing:")
        displayC(l[index])
        displayH("play") # uncomment on rPI
    else:
        mp3.load(l[index])  # az első szám betöltése
        mp3.play()
        playing = True
        print("Playing:")
        displayC(l[index])
        displayH("play") # uncomment on rPI
        print("Next:")
        print(l[index+1])

def next():
    global index
    global playing
    displayH("next") # uncomment on rPI
    mp3.load(l[index])
    mp3.play()
    playing = True
    print("Playing:")
    displayC(l[index])
    print("Next:")
    print(l[index+1])
    sleep(1)
    displayH("play") # uncomment on rPI

def previous():
    global index
    global playing
    displayH("previous") # uncomment on rPI
    mp3.load(l[index])
    mp3.play()
    playing = True
    print("Playing:")
    displayC(l[index])
    print("Next:")
    print(l[index+1])
    sleep(1)
    displayH("play") # uncomment on rPI

def shuffle(): #5 zene lista megkeverése
    global playing
    global index
    random.shuffle(l)
    index = 0
    mp3.load(l[index])
    mp3.play()
    playing = True
    displayH("shuffle") # uncomment on rPI
    print("Shuffle")
    print("Playing:")
    displayC(l[index])
    print("Next:")
    print(l[index+1])
    sleep(1)
    displayH("play") # uncomment on rPI

def volup():
    global vol
    vol += 0.02
    mp3.set_volume(vol)
    print(mp3.get_volume())

def voldown():
    global vol
    vol -= 0.02
    mp3.set_volume(vol)
    print(mp3.get_volume())

def displayC(string):
    print(string)

def displayH(action):
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
    sense.set_pixels(pixels)

# Zeneszámok betöltése, rendezése, lejátszó inicializálása
if os.path.isdir(musicpath) == True: # zene könyvtár meglétének ellenőrzése
    print("==========================================")
    print("The music folder exists")
    print("==========================================")
    os.chdir(musicpath) # könyvtár váltás, hogy ne kelljen elérési utat definiálni a zenék lejátszásakor
    for files in os.listdir(musicpath): # zene könyvtár listázása
        if files.endswith(".mp3"): # mp3 kiterejsztésű fájlokra szűrés
            l.append(files) # lejatászi lista létrehozása
            print(files)
    l.sort() # számok sorba rendezése
    lSize=len(l) # számok darabszámának tárolása
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
    sense = SenseHat()

    # SYSTEMD BugFix
    import signal
    def handler(signum, frame):
        pass
        
    try:
        signal.signal(signal.SIGHUP, handler)
    except AttributeError:
        pass
    #_________________
    pygame.init()
    mp3.set_volume(vol) # kezdeti hangerő beállítása
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = abs(acceleration['x'])
        y = abs(acceleration['y'])
        z = abs(acceleration['z'])
        if x > 2 or y > 2 or z > 2:
            print("==========================================")
            shuffle()
        else:
            for event in sense.stick.get_events():
                if event.action == "pressed":
                    print("==========================================")
                    if event.direction == "up":
                        volup()
                    elif event.direction == "down":
                        voldown()
                    elif event.direction == "left":
                        index -= 1
                        if index < 0:
                            index = lSize-1
                        previous() # Bal
                    elif event.direction == "right":
                        index += 1
                        if index == lSize:
                            index = 0
                        next() # Jobb
                    elif event.direction == "middle":
                        play_pause()
            for event in pygame.event.get():
                if event.type == SONG_END: # szám végének figyelése
                    print("==========================================")
                    print("The song ended!")
                    index += 1
                    if index == lSize:
                        index = 0
                    print(index) #RPI-n nem kell
                    next() # Jobb
    #END - SenseHat event handler
else:
    print("The music folder is not exists")

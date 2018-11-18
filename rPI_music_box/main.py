# senseHat (eszköz tesztelése)
#   függvénykönyvtárak betöltése
#from sense_hat import SenseHat # uncomment on rPI
import pygame #zene lejátszáshoz
from pygame.mixer import music as mp3 #zene lejátszáshoz
import os # mappa(ák) fájl(ok) kezelése
from time import sleep

index=0
vol=0.2
playing = ""

#Fügvények
def play_pause():
    global playing
    if playing == True:
        mp3.pause()
        playing = False
        print("Paused")
    elif playing == False:
        mp3.unpause()
        playing = True
        print("Playing:")
        displayC(l[index])
        #displayH(l[index]) # uncomment on rPI
    else:
        mp3.load(l[index])  # az első szám betöltése
        mp3.play()
        playing = True
        print("Playing:")
        displayC(l[index])
        #displayH(l[index]) # uncomment on rPI

def next():
    global index
    global playing
    index += 1
    mp3.load(l[index])
    mp3.play()
    playing = True
    print("Playing:")
    displayC(l[index])
    #displayH(l[index]) # uncomment on rPI

def previous():
    global index
    global playing
    index -= 1
    mp3.load(l[index])
    mp3.play()
    playing = True
    print("Playing:")
    displayC(l[index])
    #displayH(l[index]) # uncomment on rPI

def schuffle(): # gyro szezorok segítségével(rPI eszköz megrázásával) a zene lista megkeverése
    print("Schuffle")

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

def displayH(string):
    sense.show_message(string, text_colour=red, back_colour=blue, scroll_speed=0.05)

path="c:/rPI_music_box/music"
os.chdir(path) # könyvtár váltás, hogy ne kelljen elérési utat definiálni a zenék lejátszásakor
l = []
if os.path.isdir(path) == True: # zene könyvtár meglétének ellenőrzése
    print("==========================================")
    print("The music folder exists")
    print("==========================================")
    for files in os.listdir(path): # zene könyvtár listázása
        if files.endswith(".mp3"): # mp3 kiterejsztésű fájlokra szűrés
            l.append(files) # lejatászi lista létrehozása
            print(files)
    print("")
    print("==========================================")
    pygame.mixer.init() # lejátszó inicializálása
    mp3.set_volume(vol)

    #START - PyGame event handler (ideiglenes SenseHat helyett)
    import sys # GUI kilépéshez
    pygame.display.init()
    screen = pygame.display.set_mode ( ( 320 , 240 ) )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                """ elif event.type == pygame.KEYDOWN:
                    print ("{0}: You pressed {1:c}".format ( index , event.key ))
                elif event.type == pygame.KEYUP:
                    print ("{0}: You released {1:c}".format ( index , event.key ))
                index += 1 """
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
                    previous() # Bal
                elif event.key == ord ( "ē" ):
                    next() # Jobb
                elif event.key == ord ( "s" ):
                    schuffle() # S
    #END - PyGame event handler (ideiglenes SenseHat helyett)
    
    #START - SenseHat event handler
    """ # uncomment on rPI
    sense = SenseHat()
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    play() # Fel
                elif event.direction == "down":
                    stop() # Le
                elif event.direction == "left": 
                    previous() # Bal
                elif event.direction == "right":
                    next() # Jobb
                elif event.direction == "middle":
                    sense.show_letter("K")      # Közép
                sleep(0.5)
                sense.clear()
                """
    #END - SenseHat event handler
else:
    print("The music folder is not exists")
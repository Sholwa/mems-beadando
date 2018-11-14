# senseHat (eszköz tesztelése)
#   függvénykönyvtárak betöltése
#from sense_hat import SenseHat
import pygame #zene lejátszáshoz
import os # mappa(ák) fájl(ok) kezelése

index=0

#Fügvények
def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def next():
    global index
    index += 1
    pygame.mixer.music.load(l[index])
    pygame.mixer.music.play()

def previous():
    global index
    index -= 1
    pygame.mixer.music.load(l[index])
    pygame.mixer.music.play()
    
#Schuffle
#Display

path="c:/rPI_music_box/music"
os.chdir(path) # könyvtár váltás, hogy ne kelljen elérési utat definiálni a zenék lejátszásakor
l = []
if os.path.isdir(path) == True: # zene könyvtár meglétének ellenőrzése
    print("The folder exists")
    for files in os.listdir(path): # zene könyvtár listázása
        if files.endswith(".mp3"): # mp3 kiterejsztésű fájlokra szűrés
            l.append(files) # lejatászi lista létrehozása
            print(files)
    print("")
    print("==========================================")
    pygame.mixer.init() # lejátszó inicializálása
    pygame.mixer.music.load(l[index]) # az első szám betöltése

    #START - PyGame event handler (ideiglenes SenseHat helyett)
    import sys # GUI kilépéshez
    pygame.display.init()
    screen = pygame.display.set_mode ( ( 320 , 240 ) )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     print ("{0}: You pressed {1:c}".format ( index , event.key ))
            # elif event.type == pygame.KEYUP:
            #     print ("{0}: You released {1:c}".format ( index , event.key ))
            # index += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == ord ( "đ" ):
                    play()
                    print(index)
                    print("Play current song: "+l[index])
                    print("")
                elif event.key == ord ( "Ē" ):
                    stop()
                    print("Stop")
                elif event.key == ord ( "Ĕ" ):
                    previous()
                    print(index)
                    print("Previous song: "+l[index])
                    print("")
                elif event.key == ord ( "ē" ):
                    next()
                    print(index)
                    print("Next song: "+l[index])
                    print("")
    #END - PyGame event handler (ideiglenes SenseHat helyett)
else:
    print("The folder is not exists")

"""
mp3=os.path.join(path,l[0])
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
from time import sleep
sleep(5)
"""
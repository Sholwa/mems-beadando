# függvénykönyvtárak betöltése
#       senseHat (eszköz tesztelése)
#       zene lejátszás
import vlc
# mappa(ák) fájl(ok) kezelése
import os
# from os.path import join


#print(os.path.isdir("C:\Users\dpazsitni\Documents\GitHub\mems-beadando\rPI_music_box"))
path="c:/Users/dpazsitni/Documents/GitHub/mems-beadando/rPI_music_box/music"
if os.path.isdir(path) == True:
    print("The folder exists")
    l=os.listdir(path)
    
    mp3=os.path.join(path,l[0])
    #onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    player=vlc.MediaPlayer(mp3)
    player.play()
    
    input()
    from time import sleep
    sleep(10)
    player.stop()
    
else:
    print("The folder is not exists")

# Várakozás parancsra
#while expression:
 #   pass

#Fügvények
    #play

    #pause

    #next

    #previous

    #Schuffle

    #Display




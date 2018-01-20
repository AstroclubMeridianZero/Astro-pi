# aceasta va fi libraria de emoji-uri


##def sun():

from sense_hat import  SenseHat
import time
    
    
sense = SenseHat()

#matrice soare

def sun():
    
    x = (255,255,0)
    o = (0,0,100)
    

    sun_mark = [
        x, x, x, x, o, x, x, o,
        x, x, x, o, o, o, o, o,
        x, x, o, o, x, o, o, o,
        x, o, o, o, o, x, o, o,
        o, o, x, o, o, o, o, o,
        x, o, o, x, o, o, o, o,
        x, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o
        ]
    sense.set_pixels(sun_mark)
    sense.set_rotation(90)
    time.sleep(1)
    sense.set_rotation(180)
    time.sleep(1)
    sense.set_rotation(270)
    time.sleep(1)
    sense.set_rotation(0)
    time.sleep(1)

#matrice luna
    
def moon():
    
    y = (255,255,255)
    u = (120,120,120)
    t = (50,50,50)
    o = (0,0,0)
    

    moon_mark = [
        o, o, t, t, y, y, o, o,
        o, u, o, o, o, y, y, o,
        t, o, o, o, o, o, y, y,
        t, o, o, o, o, o, y, y,
        t, o, o, o, o, o, y, y,
        t, o, o, o, o, o, y, y,
        o, u, o, o, o, y, y, o,
        o, o, t, t, y, y, o, o
        ]
    sense.set_pixels(moon_mark)
    sense.set_rotation(90)
    time.sleep(1)
    sense.set_rotation(180)
    time.sleep(1)
    sense.set_rotation(270)
    time.sleep(1)
    sense.set_rotation(0)
    time.sleep(1)

def smile ():
    

    z = (0,255,0)
    o = (0,0,100)
    s = (255,255,0)
    
    

    smile_mark = [
        o, o, z, z, z, z, o, o,
        o, z, o, o, o, o, z, o,
        z, o, s, o, o, s, o, z,
        z, o, o, o, o, o, o, z,
        z, o, s, o, o, s, o, z,
        z, o, o, s, s, o, o, z,
        o, z, o, o, o, o, z, o,
        o, o, z, z, z, z, o, o
        ]
    sense.set_pixels(smile_mark)
    sense.set_rotation(90)
    time.sleep(1)
    sense.set_rotation(180)
    time.sleep(1)
    sense.set_rotation(270)
    time.sleep(1)
    sense.set_rotation(0)
    time.sleep(1)
  
  
  
def smiley():
    

    smiley_face = [
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, ye, ye, bl, bl, ye, ye, bl,
        bl, ye, ye, bl, bl, ye, ye, bl,
        bl, bl, bl, bl, bl, bl, bl, bl,
        ye, bl, bl, bl, bl, bl, bl, ye,
        bl, ye, bl, bl, bl, bl, ye, bl,
        bl, bl, ye, ye, ye, ye, bl, bl,
        bl, bl, bl, bl, bl, bl, bl, bl
        ]
    sense.set_pixels(smiley_face)
    sense.set_rotation(90)
    time.sleep(1)
    sense.set_rotation(180)
    time.sleep(1)
    sense.set_rotation(270)
    time.sleep(1)
    sense.set_rotation(0)
    time.sleep(1)

def winky():
        
    winky_face = [
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, bl, bl, bl, bl, ye, ye, bl,
        bl, ye, ye, bl, bl, ye, ye, bl,
        bl, bl, bl, bl, bl, bl, bl, bl,
        ye, bl, bl, bl, bl, bl, bl, ye,
        bl, ye, bl, bl, bl, bl, ye, bl,
        bl, bl, ye, ye, ye, ye, bl, bl,
        bl, bl, bl, bl, bl, bl, bl, bl
        ]
    sense.set_pixels(winky_face)
    sense.set_rotation(90)
    time.sleep(1)
    sense.set_rotation(180)
    time.sleep(1)
    sense.set_rotation(270)
    time.sleep(1)
    sense.set_rotation(0)
    time.sleep(1)

def sad():
        
    sad_face = [
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, red, red, bl, bl, red, red, bl,
        bl, red, red, bl, bl, red, red, bl,
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, bl, red, red, red, red, bl, bl,
        bl, red, bl, bl, bl, bl, red, bl,
        red, bl, bl, bl, bl, bl, bl, red,
        bl, bl, bl, bl, bl, bl, bl, bl
        ]
    sense.set_pixels(sad_face)
    sense.set_rotation(90)
    time.sleep(1)
    sense.set_rotation(180)
    time.sleep(1)
    sense.set_rotation(270)
    time.sleep(1)
    sense.set_rotation(0)
    time.sleep(1)

#lansare

ye = (255, 255, 0)# yellow
bl = (0, 0, 150)  # blank
green = (0, 255, 0)
red =(255, 0, 0)
    
sun()

moon()

smile()

smiley()

winky()

sad()
      
sense.clear()
    
   
    
##########################################
    #   prg principal- afisez pe rand toate emoji
##sun()
    
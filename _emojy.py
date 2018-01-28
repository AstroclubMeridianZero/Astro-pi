# aceasta va fi libraria de emoji-uri


##def sun():

from sense_hat import  SenseHat
import time
    
    
sense = SenseHat()

#matrice soare

def sun ():
    

    z = (255,0,0)
    o = (50,50,50)
    s = (255,255,0)
    s1= (200,200,0)
    s2= (130,130,0)
    

    sun_mark = [
        o, o, o, s2, o, o, o, o,
        o, s2, o, s1, o, s2, o, o,
        o, o, s1, s, s1, o, o, o,
        s2, s1, s, s, s, s1, s2, o,
        o, o, s1, s, s1, o, o, o,
        o, s2, o, s1, o, s2, o, o,
        o, o, o, s2, o, o, o, o,
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

def smile():
    

    z = (0,255,0) # verde
    x = (0,47,0) # verde slab
    o = (0,0,100) # albastru
    s = (0,255,0) # galben
    a = (0,255,0) # alb
    
    

    smile_mark = [
        x, x, a, a, a, a, x, x,
        x, a, x, x, x, x, a, x,
        a, x, s, x, x, s, x, a,
        a, x, x, x, x, x, x, a,
        a, x, s, x, x, s, x, a,
        a, x, x, s, s, x, x, a,
        x, a, x, x, x, x, a, x,
        x, x, a, a, a, a, x, x
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
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, ye, bl, bl, bl, bl, ye, bl,
        bl, bl, ye, ye, ye, ye, bl, bl,
        bl, bl, bl, bl, bl, bl, bl, bl
        ]
    smiley_face = [
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, ye, ye, bl, bl, ye, ye, bl,
        bl, ye, ye, bl, bl, ye, ye, bl,
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, ye, bl, bl, bl, bl, ye, bl,
        bl, bl, ye, ye, ye, ye, bl, bl,
        bl, bl, bl, bl, bl, bl, bl, bl
        ]
    sense.set_rotation(90)
    sense.set_pixels(winky_face)
    time.sleep(1)
    sense.set_pixels(smiley_face)
    time.sleep(0.33)
    sense.set_pixels(winky_face)
    time.sleep(0.33)
    
    sense.set_rotation(180)
    sense.set_pixels(winky_face)
    time.sleep(1)
    sense.set_pixels(smiley_face)
    time.sleep(0.33)
    sense.set_pixels(winky_face)
    time.sleep(0.33)
    
    sense.set_rotation(270)
    sense.set_pixels(winky_face)
    time.sleep(1)
    sense.set_pixels(smiley_face)
    time.sleep(0.33)
    sense.set_pixels(winky_face)
    time.sleep(0.33)
    
    sense.set_rotation(0)
    sense.set_pixels(winky_face)
    time.sleep(1)
    sense.set_pixels(smiley_face)
    time.sleep(0.33)
    sense.set_pixels(winky_face)
    time.sleep(0.33)
    
def sad():
        
    sad_face = [
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, red, red, bl, bl, red, red, bl,
        bl, red, red, bl, bl, red, red, bl,
        bl, bl, bl, bl, bl, bl, bl, bl,
        bl, bl, red, red, red, red, bl, bl,
        bl, red, bl, bl, bl, bl, red, bl,
        bl, bl, bl, bl, bl, bl, bl, bl,
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


moon()

sun()

smile()

# smiley()

winky()

sad()
      
sense.clear()
    
   
    
##########################################
    #   prg principal- afisez pe rand toate emoji
##sun()
    
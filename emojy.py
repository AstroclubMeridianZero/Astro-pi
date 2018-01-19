# aceasta va fi libraria de emoji-uri


##def sun():

from sense_hat import  SenseHat
import time
    
    
sense = SenseHat()
    
    #.show_message("Hello", text_colour = (255,0,0))
##red = (255,0,0)
##sense.set_pixels(3,3,red)
x = (255,255,0)
o = (150,150,150)
s = (0,0,0)

sun_mark = [
    o, o, o, o, o, o, o, s,
    o, x, o, x, o, x, o, s,
    o, o, x, x, x, o, o, s,
    o, x, x, x, x, x, o, s,
    o, o, x, x, x, o, o, s,
    o, x, o, x, o, x, o, s,
    o, o, o, o, o, o, o, s,
    s, s, s, s, s, s, s, s
    ]
    
sense.set_pixels(sun_mark)
   
time.sleep(1)  
sense.set_rotation(90)
time.sleep(1)    
sense.set_rotation(180)
time.sleep(1)    
sense.set_rotation(270)
time.sleep(1)    
sense.set_rotation(0)
time.sleep(1)    
    
sense.clear()
    
    
    
##########################################
    #   prg principal- afisez pe rand toate emoji
    
##    sun()
    
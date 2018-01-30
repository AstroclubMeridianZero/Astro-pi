from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)


def wave():
    G = blue
    R = red
    O = nothing
    logo = [
    O, O, G, G, O, O, O, O, 
    O, G, G, G, G, O, O, G,
    G, G, O, O, G, G, G, G, 
    G, O, O, O, O, G, G, O,
    O, O, G, G, O, O, O, O, 
    O, G, G, G, G, O, O, G,
    G, G, O, O, G, G, G, G, 
    G, O, O, O, O, G, G, O,
    ]
    return logo

def wave1():
    G = blue
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, O, O, G, 
    G, G, G, G, O, O, G, G,
    G, O, O, G, G, G, G, O, 
    O, O, O, O, G, G, O, O,
    O, G, G, O, O, O, O, G, 
    G, G, G, G, O, O, G, G,
    G, O, O, G, G, G, G, O, 
    O, O, O, O, G, G, O, O,
    ]
    return logo

def wave2():
    G = blue
    R = red
    O = nothing
    logo = [
    G, G, O, O, O, O, G, G, 
    G, G, G, O, O, G, G, G,
    O, O, G, G, G, G, O, O, 
    O, O, O, G, G, O, O, O,
    G, G, O, O, O, O, G, G, 
    G, G, G, O, O, G, G, G,
    O, O, G, G, G, G, O, O, 
    O, O, O, G, G, O, O, O,
    ]
    return logo
    
def wave3():
    G = blue
    R = red
    O = nothing
    logo = [
    G, O, O, O, O, G, G, O, 
    G, G, O, O, G, G, G, G,
    O, G, G, G, G, O, O, G, 
    O, O, G, G, O, O, O, O,
    G, O, O, O, O, G, G, O, 
    G, G, O, O, G, G, G, G,
    O, G, G, G, G, O, O, G, 
    O, O, G, G, O, O, O, O,
    ]
    return logo

def wave4():
    G = blue
    R = red
    O = nothing
    logo = [
    O, O, O, O, G, G, O, O, 
    G, O, O, G, G, G, G, O,
    G, G, G, G, O, O, G, G, 
    O, G, G, O, O, O, O, G,
    O, O, O, O, G, G, O, O, 
    G, O, O, G, G, G, G, O,
    G, G, G, G, O, O, G, G, 
    O, G, G, O, O, O, O, G,
    ]
    return logo


images = [wave,wave1,wave2,wave3,wave4]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1

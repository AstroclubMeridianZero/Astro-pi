import math
import time
from datetime import datetime
import ephem

# #################################
# Aflam pozitia geografica a ISS
# Parameter calculated :
# lat = latitudinea in grade (numerical)
# longs = longitudinea in grade (numerical)
# home_date_ISS = data si ora stabilirii coordonatelor ISS cu precizia la secunde

time_remains=1

global lat
lat=0

degrees_per_radian = 180.0 / math.pi
home = ephem.Observer()
home.long = '0'   # +E
home.lat = '100'      # +N
home.elevation = 100 # meters
# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
    '1 25544U 98067A   18011.65344505  .00003116  00000-0  53990-4 0  9994' ,
    '2 25544  51.6426  79.0696 0003478   2.6590 144.2138 15.54293905 94174'
)
degrees_per_radian=180/math.pi

# while True:             # aceasta linie este necesara cand facem bucla de debug pt a afisa poz ISS tot la 1s
                        # only for debug

if time_remains > 0:     # acesta linie este necesara cand fisierul ruleaza in combinatie cu celelalte module

    home.date = datetime.utcnow()
    home_date_ISS=home.date
    #print('Date & time from locating ISS ' + str(home_date_ISS))
    iss.compute(home)
    lats=[]
    longs=[]
    lats=str(iss.sublat).split(':')
    longs=str(iss.sublong).split(':')
    #lat=int(lats[0])
    
    lat=int(lats[0])

#    lat_min=(int(lats[1]))    #  aici incercam sa lucram la precizie de minute de arc nu la precizia de grade
#    lat_zecimal=00.00
#    lat_zecimal=lat+lat_min/100
#    lat=lat+lat_min/60
    
#    long=int(longs[0])+10
    longs=int(longs[0])
   
#    print("ISS geografic positin is lat: " +str(lat)+ " long: "+str(longs))  # se va printa din programul principal

#    time.sleep(1.0)             #  acesta linie este necesara cand afisam succesiv la 1s poz ISS
                                # only for debug
                                
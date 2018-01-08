import math
import time
from datetime import datetime
import ephem

degrees_per_radian = 180.0 / math.pi
home = ephem.Observer()
home.long = '0'   # +E
home.lat = '100'      # +N
home.elevation = 100 # meters
# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
    '1 25544U 98067A   18019.79291932  .00016717  00000-0  10270-3 0  9165' ,
    '2 25544  51.6408  38.4938 0003331  18.7509 341.3766 15.54122770 15438'
)
degrees_per_radian=180/math.pi


while True:
    home.date = datetime.utcnow()
    print(home.date)
    iss.compute(home)
    #e=ephem.Ecliptic(iss)
    
    #print('lat '+str(e.lat) )
    #print('lon '+str(e.lon) )
    #print('alt: '+str(alt)+' az: '+str(az))
    lats=[]
    longs=[]
    lats=str(iss.sublat).split(':')
    longs=str(iss.sublong).split(':')
    #lat=int(lats[0])
    
    lat_min=(int(lats[1]))
    lat=int(lats[0])
    lat_zecimal=00.00
    lat_zecimal=lat+lat_min/100
    
    
    lat=lat+lat_min/60
    
    long=int(longs[0])+10
    print("lat: " +str(lat)+ " long: "+str(long))
    time.sleep(1.0)
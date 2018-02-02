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

def iss_pos():

	time_remains=1
	
	global lat
	global longs
	global home_date_ISS
	global lats_sec
	global long_sec
	
	
	degrees_per_radian = 180.0 / math.pi
	home = ephem.Observer()
	home.long = '0'   # +E
	home.lat = '100'      # +N
	home.elevation = 100 # meters
	
	# Always get the latest ISS TLE data from:
	# http://www.n2yo.com/satellite/?s=25544  
	
	iss = ephem.readtle('ISS',
	
	
		                    '1 25544U 98067A   18032.92935684 +.00002966 +00000-0 +52197-4 0  9991' ,
		                    '2 25544 051.6438 332.9972 0003094 062.2964 046.0975 15.54039537097480'
	
	
		    )
	degrees_per_radian=180/math.pi
	
	# while True:             # aceasta linie este necesara cand facem bucla de debug pt a afisa poz ISS tot la 1s
							# only for debug
	
	if time_remains > 0:     # acesta linie este necesara cand fisierul ruleaza in combinatie cu celelalte module
	
		home.date = datetime.utcnow()
		home_date_ISS=home.date
		iss.compute(home)
		
		lats=[]
		longs1=[]
		lats=str(iss.sublat).split(':')
		longs1=str(iss.sublong).split(':')
		#lat=int(lats[0])
	
		lat=int(lats[0])
		lats_sec=iss.sublat
		lat_deg=lats[0]
		lat_min=lats[1]
		lat_sec=lats[2]
	
	
	#    lat_min=(int(lats[1]))    #  aici incercam sa lucram la precizie de minute de arc nu la precizia de grade
	#    lat_zecimal=00.00
	#    lat_zecimal=lat+lat_min/100
	#    lat=lat+lat_min/60
	
	#    long=int(longs[0])+10
		longs=int(longs1[0])
		long_sec=iss.sublong
		longs_deg=longs1[0]
		longs_min=longs1[1]
		longs_sec=longs1[2]
	
	
	
	#    print("ISS geografic positin is lat: " +str(lat)+ " long: "+str(longs))  # se va printa din programul principal
	
	#    time.sleep(1.0)             #  acesta linie este necesara cand afisam succesiv la 1s poz ISS
									# only for debug
	
	
	




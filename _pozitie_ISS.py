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
	
	
		                    '1 25544U 98067A   18023.42079641 +.00001825 +00000-0 +34732-4 0  9996' ,
		                    '2 25544 051.6422 020.3976 0003528 040.8951 111.5306 15.54200902096004'
	
	
		    #'1 25544U 98067A   18011.65344505  .00003116  00000-0  53990-4 0  9994' ,
		    #'2 25544  51.6426  79.0696 0003478   2.6590 144.2138 15.54293905 94174'
	
	
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
	
	
	




print('................................')
print('......  Hello Astro-pi !  ......')
print('................................')



# ###################################
# ###################################
# ###################################
# IMPORT LIB

# from picamera import PiCamera
# import picamera


import math
import time
from datetime import datetime
import ephem


import os

import csv            # pentru citire scriere fisiere csv

from csv import reader

from subprocess import call  # necesar pentru a putea executa , lansa alte fisiere .py call(["python", "your_file.py"])

import time           # necesar pentru comenzi de timp

import datetime

from datetime import datetime

import numpy as np    # necesar pt cv2 , este librarie pt proesarea matematica acelas cu math

from PIL import Image # librarie necesara procesarii imaginilor

import _pozitie_ISS   # ruleaza prg de locating ISS pt a avea acces la variabilele lui

# import _poza_change.py  # va schimbapoza studiata de la 1 la 14





# ###################################
# ###################################
# ###################################
# FUNCTIONAL PARAMETER MANUAL DEFINITION




total_time_processing = 10                                  # durata de functionare (procesare) a programului nostru in secunde (noi avem ladispozitie pe ISS fix 3ore!)
#total_time_processing = 180*60


calibrare_imagine = 80                                      # in procente, iseamna ca  numai calibrare_imagine % din imagine va fi procesat(patratul din mijloc) 0 ... 99
										# cutting image for minimal spherical aberration


limita_luminozitate_medie_pixel_zi = 105                    # aceasta constatnta face diferentirea intr zi si noapte 0 ... 255


verde = 1                                                   # stabilim limitele de culori de unde se considera ca a gasit verde 0 ... 255
rosu = 80
albastru = 60


filepath = 'Data_astropi/'				   # creem un director data_astropi pt salvare date
directory = os.path.dirname(filepath)
if not os.path.exists(directory):
	os.makedirs(directory)


now = datetime.now()					   # creem fisierul de data cu numele data + ora
filename_data = 'Data_astropi/' + '_data' + '_' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + '.csv'
f= open(filename_data,"w+")
f.close()





# ###################################
# ###################################
# ###################################
# FUNCTIONS LIB



# ###################################
# Procesam imaginea pentru cazul in care este noapte
# Noaptea cautam doar negru max si afisam un happy verde sau sorry / luna

def rutina_noapte():

	print 
	print ('Este noapte  :)  yessss!!!')
	print

	latura_patrat = int(calibrare_imagine * ys / 100)
	print ('Media de luminozitate al pozei este : ' + str(average_pixel)) + '.'
	print ('Procesam ' + str(latura_patrat) + '/' + str(latura_patrat) + ' pixeli din ' + str(xs) + '/' + str(ys) + '.')
	print

	print("Calibrating pixels accuracy for nightlight.")
	print
	# !!!  set latura patratului care va fi procesata in procente
	# calibrare_imagine = 90        # in procente, iseamna ca  numai calibrare_imagine% din imagine va fi procesat(patratul din mijloc)


	# prima data aflam cel mai negru pixel
	cel_mai_negru_pixel=255*3
	for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)): # procesam doar pixelii care se afla in interiorul patratului de calibrare imagine
		for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):     
			[r, g, b] = img[x , y]
			if cel_mai_negru_pixel > r + g + b :
				cel_mai_negru_pixel = r + g + b


	print("Cel mai negru pixel gasit este : " + str(cel_mai_negru_pixel) + '.')
	print





	# prima data aflam nr de elemente al sirului cel mai lung care se potriveste cu conditiile noastre
	lungime_max_negru=1 # lungimea sirului verde max
	for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)):          # procesam doar pixelii care se afla in interiorul patratului de calibrare imagine
		for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):     
			[r, g, b] = img[x , y]
			if cel_mai_negru_pixel == r + g + b :

				lungime=1
				for z in range(x+1, int((xs+latura_patrat)/2)):
					[r, g, b] = img[z, y]
					if cel_mai_negru_pixel == r + g + b :
						lungime = lungime + 1
					else:
						break
				lungime_max_negru = max(lungime_max_negru, lungime)

	print("Lungimea maxima a sirului de pixeli intunecati gasiti etse " + str(lungime_max_negru) + '.')
	print

	# salvam datele in csv file
	nr_pozitii_salvate=0
	for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)):
		# procesam doar pixelii care se afla in interiorul patratului de calibrare imagine
		for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):
			[r, g, b] = img[x , y]
			if cel_mai_negru_pixel == r + g + b :

				lungime=1
				for z in range(x+1, int((xs+latura_patrat)/2)):

					[r, g, b] = img[z, y]
					if cel_mai_negru_pixel == r + g + b :
						lungime = lungime + 1
					else:
						break
				if lungime_max_negru == lungime :
					nr_pozitii_salvate = nr_pozitii_salvate+1
					#  aici se face adaugarea in csv file  !!!!!!!!!!!!!
					# salvare data la o noua poza in csv file
					[r, g, b] = img[x , y]
					
					f=open(filename_data,'a') 
					f.write(time.strftime("%d/%m/%y")+','+time.strftime("%H:%M:%S")+','+str(_pozitie_ISS.lat)+','+str(_pozitie_ISS.lats_sec)+ ','+ str(_pozitie_ISS.longs)+ ','+ str(_pozitie_ISS.long_sec)+ ',' + str(r) + ',' + str(g) + ',' + str(b)+ ',' + str(x)+ ',' + str(y) + ',' + str(cel_mai_negru_pixel)+',' + str(lungime_max_negru)+',' + str(nr_poza_procesata)+',' + str('no comment')+'\n')
					f.close()					

	print ('Total  '+str(nr_pozitii_salvate)+'  de pozitii de intuneric maxim adaugate! ')                     
	print

	print ('Gata cu rutina de noapte  ........')






# ###################################
# Procesam imaginea pentru cazul in care este ziua
# Ziua cautam doar verdele si afisam un happy verde sau sorry / soare

def rutina_zi():

	print 
	print ('Este zi  :(  ')
	print

	latura_patrat = int(calibrare_imagine * ys / 100)
	print ('Media de luminozitate al pozei este : ' + str(average_pixel)) + '.'
	print ('Procesam ' + str(latura_patrat) + '/' + str(latura_patrat) + ' pixeli din ' + str(xs) + '/' + str(ys) + '.')
	print

	print("Calibrating pixels accuracy for daylight.")
	print
	# !!!  set latura patratului care va fi procesata in procente
	# calibrare_imagine = 90        # in procente, iseamna ca  numai calibrare_imagine% din imagine va fi procesat(patratul din mijloc)


	# prima data aflam nr de elemente al sirului cel mai lung care se potriveste cu conditiile noastre
	# !!!  set nuanta de verde limita care se salveaza
	#    verde = 3          # stabilim limitele de culori de unde se considera ca a gasit verde
	#    rosu = 80
	#    albastru = 60
	lungime_max_verde=1 # lungimea sirului verde max
	for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)):          # procesam doar pixelii care se afla in interiorul patratului de calibrare imagine
		for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):     
			[r, g, b] = img[x , y]
			if g > verde and r < rosu and b < albastru :
				lungime=1
				for z in range(x+1, int((xs+latura_patrat)/2)):
					[r, g, b] = img[z, y]
					if g > verde and r < rosu and b < albastru :
						lungime = lungime + 1
					else:
						break
				lungime_max_verde = max(lungime_max_verde, lungime)

	print("Lungimea maxima de pixeli verzi gasita este " + str(lungime_max_verde) + '.')
	print

	# salvam datele in csv file
	nr_pozitii_salvate=0
	for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)):          # procesam doar pixelii care se afla in interiorul patratului de calibrare imagine
		for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):     
			[r, g, b] = img[x , y]
			if g > verde and r < rosu and b < albastru :
				lungime=1
				for z in range(x+1, int((xs+latura_patrat)/2)):
					[r, g, b] = img[z, y]
					if g > verde and r < rosu and b < albastru :
						lungime = lungime + 1
					else:
						break
				if lungime_max_verde == lungime :
					nr_pozitii_salvate = nr_pozitii_salvate+1
				#  aici se face adaugarea in csv file  !!!!!!!!!!!!!

	print ('Total  '+str(nr_pozitii_salvate)+'  de pozitii de verde adaugate! ')                     
	print

	nr_verde = 0
	for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)):          # procesam doar pixelii care se afla in interiorul patratului de calibrare imagine
		for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):     
			[r, g, b] = img[x, y]
			if g > verde and r < rosu and b < albastru :
				nr_verde = nr_verde + 1

	print("Am gasit verde de " + str(nr_verde) + '.')
	print
	print ('Gata cu rutina de zi  ........')



def gata():

	# trebuie desetat camera de pe long expouser

	print 
	print ('.........................')
	print ('... We just finished! ...')
	print ('.........................')
	print ('........  E N D  ........')
	print ('.........................')
	print 
	exit()
	print ('Gata cu programul, daca ajungi aici inseamna ca ai dat gres...')










# ###################################
# ###################################
# ###################################
# START  PROGRAM


# Salvam ora min si sec cand am pornit programul, pt ca apoi dupa 180 min inchidem automat programul.
time_start = time.clock()


# Facem back la fisierul CSV cel vechi

f=open('_config.csv','a') 
f.write('calibrare,darkness,color_green,filename_data,\n')	
f.close()


f=open(filename_data,'a') 
f.write('data, ora,latitudine,lat_hi-prec,longitudine,long_hi-prec,rouge,green,blue,pos_x_img,pos_y_img,darkness,diameter_of_black,nr_poza_procesata,commentaire \n')	
f.close()

# salvare data la o noua poza in csv file de test
#f=open(filename_data,'a') 
#f.write(time.strftime("%d/%m/%y")+','+time.strftime("%H:%M:%S")+','+str(_pozitie_ISS.lat)+ ','+ str(_pozitie_ISS.longs)+'\n')
#f.close()



# Setarile aparatul pe foto picamera de noapte long exposure.
# with picamera.PiCamera() as camera:
	# camera.resolution = (1280,960)
	# camera.exposure_mode = 'off'
	# camera.framerate =1
	# camera.shutter_speed = 6000000
	# camera.iso = 1600
	# camera.capture('_processed_image.jpg')



# Deschidem bucla do while timpul de executare a pozelor trece

nr_poza_procesata=0
while ( time.clock()- time_start) < total_time_processing:
	
	nr_poza_procesata=nr_poza_procesata+1
	
#	call(["python", "_poza_change.py"])
#	print ('Am inlocuit poza cu nr'+str(_poza_change.nr_poza))

	
	
	#  !!!!!!!!!!!!!!!!!    aici am ramas cu scrierea programului = adauga la fisier data
	img_proc='_processed_image' + str(nr_poza_procesata) + '.jpg'
	
	
	print
	print ('#################' + ' Image processed nr: ' + str(nr_poza_procesata) + ' #####')
	print ('Mai avem la dispozitie '+ str(int(total_time_processing-(time.clock() - time_start))) + ' secunde.')

	
	# Aflam pozitia ISS








#	degrees_per_radian = 180.0 / math.pi
#	home = ephem.Observer()
#	home.long = '0'   # +E
#	home.lat = '100'      # +N
#	home.elevation = 100 # meters
	
	# Always get the latest ISS TLE data from:
	# http://www.n2yo.com/satellite/?s=25544  
	

#	iss = ephem.readtle('ISS',
	
	
#		            '1 25544U 98067A   18023.42079641 +.00001825 +00000-0 +34732-4 0  9996' ,
#	                    '2 25544 051.6422 020.3976 0003528 040.8951 111.5306 15.54200902096004'
	
	
		                    #'1 25544U 98067A   18011.65344505  .00003116  00000-0  53990-4 0  9994' ,
		    #'2 25544  51.6426  79.0696 0003478   2.6590 144.2138 15.54293905 94174'
	
	
#		    )
#	degrees_per_radian=180/math.pi
	
	# while True:             # aceasta linie este necesara cand facem bucla de debug pt a afisa poz ISS tot la 1s
							# only for debug
#	time_remains=1
#	if time_remains > 0:     # acesta linie este necesara cand fisierul ruleaza in combinatie cu celelalte module
	
#		home.date = datetime.utcnow()
#		home_date_ISS=home.date
		#print('Date & time from locating ISS ' + str(home_date_ISS))
#		iss.compute(home)
#		lats=[]
#		longs1=[]
#		lats=str(iss.sublat).split(':')
#		longs1=str(iss.sublong).split(':')
		#lat=int(lats[0])
	
#		lat=int(lats[0])
#		lat_deg=lats[0]
#		lat_min=lats[1]
#		lat_sec=lats[2]
	
	
	#    lat_min=(int(lats[1]))    #  aici incercam sa lucram la precizie de minute de arc nu la precizia de grade
	#    lat_zecimal=00.00
	#    lat_zecimal=lat+lat_min/100
	#    lat=lat+lat_min/60
	
	#    long=int(longs[0])+10
#		longs=int(longs1[0])
#		longs_deg=longs1[0]
#		longs_min=longs1[1]
#		longs_sec=longs1[2]













#	_pozitie_ISS.main()
	
	


	print
#	call(["python", "_pozitie_ISS.py"])
#        execfile('_pozitie_ISS.py')
        _pozitie_ISS.iss_pos()
	
	print('Date & time from locating ISS ' + str(_pozitie_ISS.home_date_ISS))
	print("ISS geografic positin is lat: " +str(_pozitie_ISS.lat)+ " long: "+str(_pozitie_ISS.longs))











	# Facem poza


	# Salvam pe disk (suprascriem) poza sub denumirea "_processed_image.jpg"



	# Import the file to be analyzed!

	img_file = Image.open(img_proc)
	#img_file = Image.open("_processed_image.jpg")
	img = img_file.load()  # salvam toti pixeli in matricea img

	# Get image width & height in pixels

	[xs, ys] = img_file.size      # xs lungimea in pixeli    ys  latimea in pixeli ai img

	#  Examine min max averrage in each pixel in the image file

	low_pixel = 255 * 3      # valoarea cea mai mica gasita in img
	hi_pixel = 0             # valoarea cea mai mare gasita in img
	nr_low_pixel = 0         # cati pixeli cu val cea mai mica 
	average_pixel = 0        # val medie a pixelilor din intreaga img

	
	latura_patrat = int(calibrare_imagine * ys / 100)
	for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)):
		for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):
			#  Get the RGB color of the pixel
			[r, g, b] = img[x, y]

			sum_pixel = r + b + g    # salvam val cea mai mica
			if low_pixel > sum_pixel:
				low_pixel = r + g + b 
				nr_low_pixel = nr_low_pixel + 1

			average_pixel = average_pixel + sum_pixel



	#  Stabilim Zi sau Noapte - caculand media pixelilor in the image file 
	#  Mergem la rutina de calcul pentru Zi si pt Noapte continuam aici

	average_pixel = average_pixel/xs
	average_pixel = average_pixel/ys
	average_pixel = average_pixel/3
	# print ('Media de luminozitate al pozei este : ' + str(average_pixel))


	# !!!  set val ;a care se face diferentierea intre zi si noapte
	# la calcul practic aceasta val se compara cu suma r + g + b
	#limita_luminozitate_medie_pixel_zi = 15                    # aceasta constatnta facediferentirea intr zi si noapte


	if average_pixel > limita_luminozitate_medie_pixel_zi  :   # mergem la rutina de procesare img pt zi cand avem media de pixeli peste 15  
		rutina_zi()
	else:
		rutina_noapte()                                       #  Continuam cu programul pentru cazul de noapte











gata()    #  Inchei programul  , pe ISS se va ajunge aici doar cand trec cele 180 de minute.

# ###################################
# ###################################
# ###################################
# STOP  PROGRAM












# ###################################
# ###################################
# ###################################
# Libraria back up



# ###################################


#Citim un pixel :

im = Image.open('image.gif')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

print(r, g, b)
(65, 100, 137)

#citim un pixel a doua varianta

import scipy.misc
im = scipy.misc.imread('um_000000.png', flatten=False, mode='RGB')
print(im.shape)
gives

(480, 640, 3)
#so it is (height, width, channels). So the pixel at position (x, y) is

color = tuple(im[y][x])
r, g, b = color



############################################
#covertimin grayscale

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




#Varianta 2:
#Conversion from color to grey scale:

# Mat img = imread("image.jpg"); // loading a 8UC3 image
# Mat grey;
# cvtColor(img, grey, CV_BGR2GRAY);



##############################################
#Afisam poza:

#Mat img = imread("image.jpg");

#namedWindow("image", CV_WINDOW_AUTOSIZE);
#imshow("image", img);
#waitKey();





############################################
#Exemplu de min max, prima data convertim

#Mat img = imread("image.jpg");
#Mat grey;
#cvtColor(img, grey, CV_BGR2GRAY);

#Mat sobelx;
#Sobel(grey, sobelx, CV_32F, 1, 0);

#double minVal, maxVal;
#minMaxLoc(sobelx, &minVal, &maxVal); //find minimum and maximum intensities
#Mat draw;
#sobelx.convertTo(draw, CV_8U, 255.0/(maxVal - minVal), -minVal * 255.0/(maxVal - minVal));

#namedWindow("image", CV_WINDOW_AUTOSIZE);
#imshow("image", draw);
#waitKey();



#############################################
#scriem un fisier de salvare data    data_FM.csv


f=open('data_FM.csv','a') 
f.write('timestamp,humidite,accX,accY,accZ,latitude,longitude,commentaire \n')	
f.close()




###############################################
# Pozitia ISS download cea mai noua

# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
                    '1 25544U 98067A   14167.50911759  .00016717  00000-0 10270-3 0  9003',
    '2 25544  51.6458 102.9444 0003960 102.9396 257.2197 15.50725128 11228'
)


#Programul

import math
import time
from datetime import datetime
import ephem
degrees_per_radian = 180.0 / math.pi
home = ephem.Observer()
home.lon = '-122.63'   # +E
home.lat = '45.56'      # +N
home.elevation = 80 # meters
# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
                    '1 25544U 98067A   11290.51528320  .00016717  00000-0  10270-3 0  9006',
    '2 25544  51.6378 264.9380 0016170 337.7557  22.2896 15.60833726 20019'
)
while True:
	home.date = datetime.utcnow()
	iss.compute(home)
	print('iss: altitude %4.1f deg, azimuth %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
	time.sleep(1.0)



####################################################3

from random import randint
from astro_pi import AstroPi
import ephem
import datetime
import time
## [...]
ap = AstroPi()

name = "ISS (ZARYA)";            
#line1 = "1 25544U 98067A   15178.42973832  .00011523  00000-0  17276-3 0  9998"
#line2 = "2 25544  51.6456  32.8760 0003760  98.7829 323.8559 15.55421066949635"

line1 = "1 25544U 98067A   15185.95963984  .00006354  00000-0  98170-4 0  9990"
line2 = "2 25544  51.6454 355.2696 0003202 121.3230  14.1346 15.55509232950800"

def countdown():
	for i in reversed(range(0, 6)):
		ap.show_letter(str(i))
		time.sleep(1)

countdown()        
ap.clear()
while True:
	temp = str(ap.get_temperature())
	pressure =  str(ap.get_pressure())
	orientation =  ap.get_orientation_degrees()

	time.sleep(0.5)
	tle_rec = ephem.readtle(name, line1, line2)
	tle_rec.compute()

	#convert to strings#
	lat2string = str(tle_rec.sublat)
	long2string = str(tle_rec.sublong)

	lati = lat2string.split(":")
	longt = long2string.split(":")

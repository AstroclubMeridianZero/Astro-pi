# ###################################
# ###################################
# ###################################
# IMPORT LIB

import time           # necesar pentru comenzi de timp

import numpy as np    # necesar pt cv2 , este librarie pt proesarea matematica acelas cu math

from PIL import Image # librarie necesara procesarii imaginilor





# ###################################
# ###################################
# ###################################
# FUNCTIONAL PARAMETER MANUAL DEFINITION


total_time_processing = 10                                  # durata de functionare (procesare) a programului nostru in secunde (noi avem ladispozitie pe ISS fix 3ore!)
#total_time_processing = 180*60


calibrare_imagine = 80                                      # in procente, iseamna ca  numai calibrare_imagine % din imagine va fi procesat(patratul din mijloc) 0 ... 99
     # cutting image for minimal spherical aberration


limita_luminozitate_medie_pixel_zi = 15                     # aceasta constatnta face diferentirea intr zi si noapte 0 ... 255


verde = 1                                                   # stabilim limitele de culori de unde se considera ca a gasit verde 0 ... 255
rosu = 80
albastru = 60



# ###################################
# ###################################
# ###################################
# FUNCTIONS LIB



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

print('................................')
print('......  Hello Astro-pi !  ......')
print('................................')


# Salvam ora min si sec cand am pornit programul, pt ca apoi dupa 180 min inchidem automat programul.

# Trebuie setat aparatul pe foto de noapte long exposure.

# Facem back la fisierul CSV cel vechi

# Deschidem bucla do while timpul de executare a pozelor trece

# Golim fisierul CSV

# Aflam pozitia ISS

# Facem poza

# Salvam in CSV pozitia ISS si timpul (momentul exact incare se face poza pt a putea contraverifica daca poz ISS este buna)

# Salvam pe disk (suprascriem) poza sub denumirea "_processed_image.jpg"



# Import the file to be analyzed!

img_file = Image.open("_processed_image.jpg")
img = img_file.load()  # salvam toti pixeli in matricea img

# Get image width & height in pixels

[xs, ys] = img_file.size      # xs lungimea in pixeli    ys  latimea in pixeli ai img

#  Examine min max averrage in each pixel in the image file

low_pixel = 255 * 3      # valoarea cea mai mica gasita in img
hi_pixel = 0             # valoarea cea mai mare gasita in img
nr_low_pixel = 0         # cati pixeli cu val cea mai mica 
average_pixel = 0        # val medie a pixelilor din intreaga img

for x in range(1, xs):
     for y in range(1, ys):
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

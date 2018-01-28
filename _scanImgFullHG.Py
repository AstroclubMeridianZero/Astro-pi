print('................................')
print('......  Hello Astro-pi !  ......')
print('................................')
print('........  Calibration ..........')
print('................................')


from sense_hat import SenseHat
sense = SenseHat()
sense.show_message('Hello AstroPi !')



# ###################################
# ###################################
# ###################################
# IMPORT LIB

from sense_hat import SenseHat

from picamera import PiCamera

from time import sleep

import _emojy         # afiseaza emoji

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

sense = SenseHat()
sense.show_message('Starting !')

total_time_processing = 50                                  # durata de functionare (procesare) a programului nostru in secunde (noi avem ladispozitie pe ISS fix 3ore!)
#total_time_processing = 180*60


calibrare_imagine = 75                                      # in procente, iseamna ca  numai calibrare_imagine % din imagine va fi procesat(patratul din mijloc) 0 ... 99
calibrare_imagine_zi = 100   										# cutting image for minimal spherical aberration


limita_luminozitate_medie_pixel_zi = 40                    # aceasta constatnta face diferentirea intr zi si noapte 0 ... 255
								# din experiente se considera 117 o val rezonabila intre zi si noapte


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
    _emojy.moon()
    print

    latura_patrat = int(calibrare_imagine * ys / 100)
    print ('Media de luminozitate al pozei este : ' + str(average_pixel) + '.')
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


    print("Cel mai negru pixel gasit este : " + str(int(cel_mai_negru_pixel/3)) + '.')
    print





    # prima data aflam nr de elemente al sirului cel mai lung care se potriveste cu conditiile noastre
    lungime_max_negru = 1 # lungimea sirului verde max
    lungime = 1
    for y in range(int((ys-latura_patrat)/2), int((ys+latura_patrat)/2)):          # procesam doar pixelii care se afla in interiorul patratului de calibrare imagine
            for x in range(int((xs-latura_patrat)/2), int((xs+latura_patrat)/2)):     
                    [r, g, b] = img[x , y]
                    if cel_mai_negru_pixel == r + g + b and lungime < latura_patrat + 1 :

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

    # salvam datele in csv file cu doua comditii
    # 1- lungimea sirului de negru sa fie mai mica decat 1/4 din latura_patrat
    # 2- nr de siruri gasite sa fie sub 100, ce este peste 100 se pierd
    nr_pozitii_salvate=0
    if lungime_max_negru < latura_patrat/4:
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

                                            # salvam data la primele 100 de pozitii ale sirului
                                            # restul le pierdem
                                            if nr_pozitii_salvate < 100:
                                                    #  aici se face adaugarea in csv file  !!!!!!!!!!!!!
                                                    # salvare data la o noua poza in csv file
                                                    [r, g, b] = img[x , y]
                                                    f=open(filename_data,'a') 
                                                    f.write(time.strftime("%d/%m/%y")+','+time.strftime("%H:%M:%S")+','+str(_pozitie_ISS.lat)+','+str(_pozitie_ISS.lats_sec)+ ','+ str(_pozitie_ISS.longs)+ ','+ str(_pozitie_ISS.long_sec)+ ',' + str(r) + ',' + str(g) + ',' + str(b)+ ',' + str(x)+ ',' + str(y) + ',' + str(int(cel_mai_negru_pixel/3))+',' + str(lungime_max_negru)+',' + str(nr_poza_procesata)+',' + str('no comment')+'\n')
                                                    f.close()
                                            else:
                                                    nr_pozitii_salvate = 100
                                                    print
                                                    print ('Avem muulte locatii intunecate !!  ')							
    else:
            print
            print ('Nori sau ocean :(  ')


    print ('Total  '+str(nr_pozitii_salvate)+'  de pozitii de intuneric maxim adaugate! ')                     
    print
    if nr_pozitii_salvate > 0 :
        _emojy.smiley()
    else:
        _emojy.sad()
        
    print ('Gata cu rutina de noapte  ........')






# ###################################
# Procesam imaginea pentru cazul in care este ziua
# Ziua cautam doar verdele si afisam un happy verde sau sorry / soare

def rutina_zi():

    print 
    print ('Este zi  :(  ')
    _emojy.sun()
    print

    latura_patrat = int(calibrare_imagine_zi * ys / 100)
    print ('Media de luminozitate al pozei este : ' + str(average_pixel) + '.')
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
                    if g > r + 20 and g > b + 30 :
                            lungime=1
                            for z in range(x+1, int((xs+latura_patrat)/2)):
                                    [r, g, b] = img[z, y]
                                    if g > r + 20 and g > b + 30 :
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
                    if g > r + 20 and g > b + 30 :
                            lungime=1
                            for z in range(x+1, int((xs+latura_patrat)/2)):
                                    [r, g, b] = img[z, y]
                                    if g > r + 20 and g > b + 30 :
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
                    if g > r + 20 and g > b + 30 :
                            nr_verde = nr_verde + 1

    print("Am gasit verde de " + str(nr_verde) + '.')
    if nr_pozitii_salvate > 0 :
        _emojy.smile()
        sense.show_message('Look vegetation !')        
    else:
        _emojy.sad()
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
	#exit()
	sensehat=1
	while sensehat > 0:
            sense.show_message('Finish !!!   End  program !!!')
	
	
	
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


#  !!!!!!!!!!!!!!!!!!!!!!!!!!  aici tre activate pt a face pozele real timp
# Setarile aparatul pe foto picamera de noapte long exposure.
#with picamera.PiCamera() as camera:
camera=PiCamera()
#camera.resolution = (1280,960)
camera.exposure_mode = 'off'
camera.framerate =1
camera.shutter_speed = 6000000
camera.iso = 1600
#camera.capture('_processed_image.jpg')

average_pixel = 100



# Deschidem bucla do while timpul de executare a pozelor trece

nr_poza_procesata=0
while ( time.clock()- time_start) < total_time_processing:

    nr_poza_procesata=nr_poza_procesata+1

    #       Denumim fisierul procesat cu incrementare manuala
    #	print ('Am inlocuit poza cu nr'+str(_poza_change.nr_poza))



    #img_proc='_processed_image' + str(nr_poza_procesata) + '.jpg'
    img_proc='_processed_image' + '.jpg'

    print
    print ('#################' + ' Image processed nr: ' + str(nr_poza_procesata) + ' #####')
    print ('Mai avem la dispozitie '+ str(int(total_time_processing-(time.clock() - time_start))) + ' secunde.')


    # Facem poza

    # !!!!!!!!!!!!!!!!!    aici tre activate liniile pt a face poze real time
    
    if average_pixel > limita_luminozitate_medie_pixel_zi  :# mergem la rutina de procesare img pt zi cand avem media de pixeli peste 15  
        # rutina_zi()
        camera.exposure_mode = 'auto'
        camera.framerate =30       #  cea default
        camera.shutter_speed = 0   # valoarea 0 inseamna auto
        camera.iso = 0   # 0 inseamna auto
    else:
        # rutina_noapte()     
        #camera.resolution = (1280,960)
        camera.exposure_mode = 'off'
        camera.framerate =1
        camera.shutter_speed = 6000000
        camera.iso = 1600

    _emojy.winky()
    camera.start_preview()
    sleep(1)
    camera.capture('_processed_image.jpg')
    camera.stop_preview()

    
    
    
    # Aflam pozitia ISS


    _pozitie_ISS.iss_pos()

    print
    print('Date & time from locating ISS ' + str(_pozitie_ISS.home_date_ISS))
    print("ISS geografic positin is lat: " +str(_pozitie_ISS.lat)+ " long: "+str(_pozitie_ISS.longs))




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

    average_pixel = average_pixel/latura_patrat
    average_pixel = average_pixel/latura_patrat
    average_pixel = average_pixel/3
    # print ('Media de luminozitate al pozei este : ' + str(average_pixel))


    # !!!  seam val la care se face diferentierea intre zi si noapte
    # la calcul practic aceasta val se compara cu suma r + g + b
    #limita_luminozitate_medie_pixel_zi = 15                    # aceasta constatnta facediferentirea intr zi si noapte


    if average_pixel > limita_luminozitate_medie_pixel_zi  :# mergem la rutina de procesare img pt zi cand avem media de pixeli peste 15  
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


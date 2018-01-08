# ######################################################
import time;        # necesar pentru comenzi de timp
#Import numpy:      #necesar pt cv2
import cv2;          # necesar pentru comanda waitkey()
import sys;
import pillw

from pil import Image
#import Image

print 'Asteapta 10S!'
time.sleep(10)


#char c = cv::waitKey(0);
#if ('q' == c)
#     QuitProgram();






print 'Hello, world!'
print 'Astept sa apesi o tasta'
cv2.waitKey()
#waitKey();
print 'Ai apasat o tasta'

# ############################
# Inceputul






# (1) Import the file to be analyzed!

img_file = Image.open("thedress.jpg")
img = img_file.load()

# (2) Get image width & height in pixels
[xs, ys] = img_file.size
max_intensity = 100
hues = {}

# (3) Examine each pixel in the image file
for x in xrange(0, xs):
     for y in xrange(0, ys):
          # (4)  Get the RGB color of the pixel
          [r, g, b] = img[x, y]









          # (5)  Normalize pixel color values
          r /= 255.0
          g /= 255.0
          b /= 255.0




###################################
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





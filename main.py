import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import pytesseract


image = cv.imread("Escaneo.jpg")


separation_names = image[370:1570,150:625]
separation_signatures = image[370:1570,625:1100]

names = pytesseract.image_to_string(separation_names)
names = names.strip().split("\n\n")
#print(names)


separation_signatures_gray = cv.cvtColor(separation_signatures, cv.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.float32)/25
separation_signatures_gray = cv.filter2D(separation_signatures_gray,-1,kernel)


plt.imshow(separation_signatures_gray,cmap='gray', vmin=0, vmax=255)
plt.title('Imaxe1')
plt.show()


th3 = cv.adaptiveThreshold(separation_signatures_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
separation_signatures_gray = cv.bitwise_not(th3)


plt.imshow(th3,cmap='gray', vmin=0, vmax=255)
plt.title('Imaxe1')
plt.show()


kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(separation_signatures_gray,kernel,iterations = 1)

plt.imshow(dilation,cmap='gray', vmin=0, vmax=255)
plt.title('Imaxe1')
plt.show()






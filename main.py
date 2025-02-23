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

separation_signatures= cv.cvtColor(separation_signatures, cv.COLOR_BGR2GRAY)

cnts,hierarchy = cv.findContours(separation_signatures, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cnts2,hierarchy2 = cv.findContours(separation_signatures, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
conContornos = cv.cvtColor(separation_signatures,cv.COLOR_GRAY2RGB)

for contorno in cnts:
    M = cv.moments(contorno)
    area = cv.contourArea(contorno)
    print(M)
    print(f"Área: {area}")

    perimeter = cv.arcLength(contorno, True)
    
    approx = cv.approxPolyDP(contorno, 0.04 * perimeter, True)
    
    if len(approx) == 4:
        ratio = area / (perimeter * perimeter)
        
        if 0.8 < ratio < 1.2:
            print(f"El contorno con {len(approx)} vértices parece un cuadrado")
        else:
            print(f"El contorno con {len(approx)} vértices parece un rectángulo")
    else:
        print(f"El contorno con {len(approx)} vértices no parece un cuadrado")
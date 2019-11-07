# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 07:47:36 2019

@author: mohamed
"""

import glob
import os
import numpy as np
import cv2
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

images = glob.glob("*.jpg")
names = []

i = 0
cwd = os.getcwd()

if not os.path.exists('Output_Images'):
        os.makedirs('Output_Images')

path_output = cwd+'\\Output_Images\\'

for image in images:
    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 99, 30)
    path_output = cwd+'\\Output_Images\\' + str(i)+'.jpg'
    i += 1
    cv2.imwrite(path_output, gaus)
    #cv2.imshow(image,img)
    
IMGS = images = glob.glob(cwd+"\\Output_Images\\*.jpg")
for i in range(len(IMGS)):
    text = tess.image_to_string(IMGS[i])
    with open(cwd+"\\Output_Images\\"+str(i)+".txt", "w") as text_file:
        text_file.write(text)

print('Done')
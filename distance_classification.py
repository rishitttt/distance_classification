import numpy as np
import cv2
import matplotlib.pyplot as plt


fimg = cv2.imread('Plaksha_Faculty.jpg')
simg = cv2.imread('Dr_Shashi_Tharoor.jpg')

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(fimg)

plt.subplot(1, 2, 2)
plt.imshow(simg)

plt.show()

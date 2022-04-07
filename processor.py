import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./testimg.jpg', 0)
plt.imshow(img, cmap='gray')

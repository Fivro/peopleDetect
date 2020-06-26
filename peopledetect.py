# Detect People from an image by python
import cv2 
image = cv2.imread("japan-220696_1920.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

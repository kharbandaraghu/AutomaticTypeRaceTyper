# Necessary Imports
import cv2
import pytesseract
import keyboard
import time
img = cv2.imread('asd.png') # load the image
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(img)
text = text.replace('\n',' ').replace('\r',' ').replace('|','I') # Preprocess the text to remove line breaks
time.sleep(2)# Some time to quickly switch cursors
# start typing
for i in text:
    keyboard.write(i)
    time.sleep(0.07) # How much time you want to wait before each word is typed
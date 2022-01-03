import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

# Detecting or decoding Barcode or Qrcode using webcam

cap = cv.VideoCapture(0)  # 0 is id for our webcam
cap.set(3, 640)  # 3 denotes Width of window
cap.set(4, 480)  # 4 denotes Height of window

while True:
    istrue, img = cap.read()
    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,(255,0,255),5)
        pts2=barcode.rect
        cv.putText(img,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    cv.imshow('Video', img)
    cv.waitKey(1)

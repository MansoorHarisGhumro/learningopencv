import cv2
#key = input()
img = cv2.imread('C:/baby.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('ImageWindow', img)
cv2.waitKey(0)
cv2.imshow('ImageWindow', gray)
cv2.waitKey(0)
cv2.imshow('ImageWindow', hsv)
cv2.waitKey(0)

'''
if key == 'c':
    cv2.imshow('ImageWindow', img)
    cv2.waitKey(0)
if key == 'b':
    cv2.imshow('ImageWindow', gray)
    cv2.waitKey(0)
'''


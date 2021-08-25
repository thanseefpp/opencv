import cv2


img = cv2.imread('images/cat.png')

cv2.imshow('output',img)
cv2.waitKey(5000)
print('exited image')
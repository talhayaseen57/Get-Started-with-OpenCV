import cv2 as cv

image_path = "Photos/park.jpg"
img = cv.imread(image_path)

cv.imshow("Original Image", img)

cv.waitKey(0)

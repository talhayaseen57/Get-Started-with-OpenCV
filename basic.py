import cv2 as cv

img_path = "Photos/park.jpg"
image = cv.imread(img_path)

cv.imshow("Original Image", image)

# # Convert to Grayscale image
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscal Image", gray_image)

# # Blur an image
blur_image = cv.GaussianBlur(image, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blurred Image", blur_image)

# # Edge Cascade
canny_edges = cv.Canny(image, 100, 200)
cv.imshow("Canny Edges", canny_edges)

# Cropping an image
cropped_image = image[50:200, 200:400]
cv.imshow("Cropped Image", cropped_image)

cv.waitKey(0)

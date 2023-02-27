import cv2 as cv
import numpy as np

image_path = "Photos/park.jpg"
img = cv.imread(image_path)

cv.imshow("Original Image", img)


def traslateImage(image, x, y):
    """
    translation of image
    -x --> Left
    -y --> Up
    x ---> Right
    y ---> Down
    """
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, translation_matrix, dimensions)


# translated_image = traslateImage(img, 100, 100)
# cv.imshow("Translated Image", translated_image)


def rotateImage(image, rotation_angle, rotation_point=None):
    """
    This function rotates image with given rotation angle.
    -ive angle will rotate image anti-clockwise.
    +ive angle will rotate image clockwise.
    """
    height, width = image.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(
        rotation_point, rotation_angle, 1.0)
    dimensions = (height, width)

    return cv.warpAffine(image, rotation_matrix, dimensions)


# rotated_image = rotateImage(img, 45)
# cv.imshow("Rotated Image", rotated_image)


# Resizing the image
"""
cv.INTER__AREA ---> (default) for shrinking the image
cv.INTER_LINEAR --> for enlarging the image
cv.INTER_CUBIC ---> to enlarge too, slower but better results
"""
# resized_image = cv.resize(img, (730, 730), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized Image", resized_image)


# Flipping the image
"""
flipCode:
    0 ---> horizontally (on x-axis)
    1 ---> vertically (on y-axis)
    -1 --> both horizontally & vertically
"""
# flipped_image = cv.flip(img, 0)
# cv.imshow("Flipped Image", flipped_image)

cv.waitKey(0)

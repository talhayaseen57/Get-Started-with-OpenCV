import cv2 as cv

import show

image = "Photos/cat.jpg"
video = "Videos/dog.mp4"

# show.showImage(image)
# show.showVideoWithChangedDimensions(video, size_ratio=0.2)
show.showImageChangedDimensions(image, size_ratio=1.5)

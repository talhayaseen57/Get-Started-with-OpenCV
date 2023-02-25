import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    length = int(frame.shape[0] * scale)

    dimensions = (width, length)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

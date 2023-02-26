import cv2 as cv
import numpy as np

blank = np.zeros((480, 630, 3), dtype='uint8')
# cv.imshow("Blank", blank)

# blank[:] = 255, 0, 0
# cv.imshow("Blue", blank)

# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2),
#              (255, 0, 0), thickness=cv.FILLED)
# cv.imshow("Rectangle", blank)

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
#           50, (255, 0, 0), thickness=cv.FILLED)
# cv.imshow("Circle", blank)

# cv.line(blank, (56, 35),
#         (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=2)
# cv.imshow("Line", blank)

cv.putText(blank, "Talha Yaseen Bhatti", (150, 230),
           cv.FONT_HERSHEY_COMPLEX, 0.80, (255, 0, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)

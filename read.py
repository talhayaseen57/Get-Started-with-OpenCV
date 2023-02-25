import cv2 as cv


def readImage(image_path):
    img = cv.imread(image_path)
    cv.imshow("Cat Image", img)
    cv.waitKey(0)


def readVideo(video_path):
    capture = cv.VideoCapture(video_path)

    while True:
        is_true, frame = capture.read()

        cv.imshow("Dog Video", frame)

        if cv.waitKey(20) and 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

import cv2 as cv

import rescale


def showImage(image_path):
    img = cv.imread(image_path)
    cv.imshow(image_path.split('/')[-1], img)
    cv.waitKey(0)


def showVideo(video_path):
    try:
        capture = cv.VideoCapture(video_path)

        while True:
            is_true, frame = capture.read()

            cv.imshow(video_path.split('/')[-1], frame)

            if cv.waitKey(20) and 0xFF == ord('d'):
                break

    except cv.error:
        capture.release()
        cv.destroyAllWindows()


def showVideoWithChangedDimensions(video_path, size_ratio=0.75):
    try:
        capture = cv.VideoCapture(video_path)

        while True:
            is_true, frame = capture.read()
            changed_frame = rescale.rescaleFrame(frame, size_ratio)

            if changed_frame == []:
                break

            cv.imshow("Resized " + video_path.split('/')[-1], changed_frame)

            if cv.waitKey(20) and 0xFF == ord('d'):
                break

    except cv.error:
        capture.release()
        cv.destroyAllWindows()

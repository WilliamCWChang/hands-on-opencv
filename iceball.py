import sys
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)

    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=70, maxRadius=90)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(frame, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(frame, center, radius, (255, 0, 255), 3)
            print(radius, center)

    # r = frame.copy()
    # g = frame.copy()
    # b = frame.copy()
    # # r[:, :, 0] = 0
    # # r[:, :, 1] = 0

    # # b[:, :, 2] = 0
    # # b[:, :, 1] = 0

    # # g[:, :, 0] = 0
    # # g[:, :, 2] = 0

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # cv2.imshow('B', b)
    # cv2.imshow('G', g)
    # cv2.imshow('R', r)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

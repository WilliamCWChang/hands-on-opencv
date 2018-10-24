import numpy as np
import cv2
from pprint import pprint
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    blur_image = cv2.medianBlur(gray, 5)
    # blur_image = gray
    cimg = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(blur_image, cv2.HOUGH_GRADIENT, 1, minDist=100,
                               param1=50, param2=30, minRadius=20, maxRadius=100)

    # print("================================")
    # print(circles)
    # print("================================")
    if circles is None:
        print("No Circle")
    else:
        circles = np.uint16(np.around(circles))
        pprint(circles[0, :])

        max = [0, 0, 0]
        for i in circles[0, :]:
            if max[2] < i[2]:
                max = i

        cv2.circle(cimg, (max[0], max[1]), max[2], (0, 255, 0), 2)
        cv2.circle(cimg, (max[0], max[1]), 2, (0, 0, 255), 3)

        # for i in circles[0, :]:
        #     # draw the outer circle
        #     cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        #     # draw the center of the circle
        #     cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimg)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

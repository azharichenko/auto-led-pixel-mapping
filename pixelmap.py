from pathlib import Path

import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)
temp  = None

def locate_led_coord()


def write_to_csv():
    output = Path.cwd() / "output.csv"
    exit()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv = cv2.GaussianBlur(hsv, (7, 7), 0)

    # define range of blue color in HSV
    lower_blue = np.array([0, 110, 130])
    upper_blue = np.array([10, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    res = cv2.cvtColor(res, cv2.COLOR_HSV2RGB)
    res = cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)

    ret, res = cv2.threshold(res, 1, 255, cv2.THRESH_BINARY)

    if temp is None:
        temp = res
    else:
        temp += res
        blurred = cv2.GaussianBlur(temp, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

        # find contours in the thresholded image
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        if len(cnts) == 300:
            # write_to_csv(cnts)
            pass
        # loop over the contours
        for c in cnts:
            # compute the center of the contour
            M = cv2.moments(c)
            if M["m00"] == 0.0:
                continue
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            cv2.drawContours(res, [c], -1, (0, 255, 0), 2)
            cv2.circle(res, (cX, cY), 7, (255, 255, 255), -1)

    # Display the resulting frame
    cv2.imshow('res', cv2.GaussianBlur(res, (5,5), 0))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt
import numpy as np

def nothing(x):
    pass


# reading and resizing the image
frame = cv2.imread('p3.png')
frame = cv2.resize(frame,(500,500))

# converting the image into hsv
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


# collecting all the value for hue saturation value
hue = []
saturation = []
value = []
for i in hsv:
    for j in i:
        hue.append(j[0])
        saturation.append(j[1])
        value.append(j[2])

# taking average and adding the a constant  for better result in of hue,saturation, value
lh = int(sum(hue)/len(hue) - 5)
ls = int(sum(saturation)/len(saturation) + 8)
lv = int(sum(value)/len(value) - 100)

# creating the trackbars for tracking
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", lh, 255, nothing)
cv2.createTrackbar("LS", "Tracking", ls, 255, nothing)
cv2.createTrackbar("LV", "Tracking", lv, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    # getTrackbarPos with get the value from trackbar if the position of trackbar changes
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    cv2.imshow("original", frame)
    cv2.imshow("result", mask)

    key = cv2.waitKey(1)
    plt.imshow(mask)
    plt.show()
    cv2.waitKey(0)
    if key == 27:
        break

cv2.destroyAllWindows()


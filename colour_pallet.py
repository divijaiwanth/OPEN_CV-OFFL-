import numpy as np
import cv2 as cv

drawing = False
ix, iy = -1, -1

def nothing():
    pass

# Create a black window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('paint')

# Create the trackbar for change color
cv.createTrackbar('Blue', 'paint', 0, 255, nothing)
cv.createTrackbar('Green', 'paint', 0, 255, nothing)
cv.createTrackbar('Red', 'paint', 0, 255, nothing)
cv.createTrackbar('Brush Size', 'paint', 0, 20, nothing)

# Function Get current position of four trackers
def get_position():
    global r, g, b, s
    b = cv.getTrackbarPos('Blue', 'paint')
    g = cv.getTrackbarPos('Green', 'paint')
    r = cv.getTrackbarPos('Red', 'paint')
    s = cv.getTrackbarPos('Brush Size', 'paint')
    return (b, g, r, s)

# Function to draw as per mouse event
def draw(event, x, y, flags, param):
    global drawing, ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        x, y = ix, iy
    elif event == cv.EVENT_MOUSEMOVE:
        drawing = True
        cv.circle(img, (x, y), s, (b, g, r), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img, (x, y), s, (b, g, r), -1)


while (1):
    cv.imshow('paint', img)
    if cv.waitKey(1) == 27:
        break
    else:
        get_position()
        cv.setMouseCallback('paint', draw)
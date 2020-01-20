import pyautogui    #pyautogui
import cv2  # opencv
import numpy as np #numpy
from thinning import guo_hall_thinning
import matplotlib.pyplot as plt

# converts the picture to an array of points
def getPoints(image):
    window = image[0:1042,0:1042] # crops image pixels to desired window size
    _, filtered = cv2.threshold(window, 200, 255, cv2.THRESH_BINARY_INV)
    window = guo_hall_thinning(filtered)

    plt.imshow(window)
    plt.show()
    
    points = []

    # add to array
    for pt in np.argwhere(window.T != 0):
        point = []
        point.append(pt[0]) # add x coordinate
        point.append(pt[1]) # add y
        points.append(point)

    return points

# connects the points in a stroke from starting point
def getStroke(point, stack):
    print(stack)
    if (stack > 980):
        pyautogui.click()
        pyautogui.mouseUp()
        pyautogui.mouseUp()
        pyautogui.mouseUp()
        return
    pyautogui.moveTo(point[0] + 300, point[1] + 200)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    continued = False
    # adds point to stroke
    # stroke.append(point)
    # removes points that have been added
    points.remove(point)
    # surrounding pixels are all potential neighbors
    potentialNeighbors =    [[point[0] - 1, point[1] - 1], [point[0], point[1] - 1], [point[0] + 1, point[1] - 1], 
                            [point[0] - 1, point[1]], [point[0] + 1, point[1]], 
                            [point[0] - 1, point[1] + 1], [point[0], point[1] + 1], [point[0] + 1, point[1] + 1]]

    # recursive step
    for potentialNeighbor in potentialNeighbors:
        if potentialNeighbor in points:
            result = potentialNeighbor
            continued = True
            getStroke(potentialNeighbor, stack + 1)
    if (not continued):
        pyautogui.click()
        pyautogui.mouseUp()
        pyautogui.mouseUp()
        pyautogui.mouseUp()

pyautogui.PAUSE = 0
image = cv2.imread("C:/Users/Gary/Desktop/podcats1.png", 0)    # reads image
points = getPoints(image)
print(len(points))
stroke = []

# screenWidth, screenHeight = pyautogui.size()    # sets window of pyautogui control to our screen
# pyautogui.moveTo(points[0][0] + 300, points[0][1] + 200)                      # clicks a few times to ensure window is selected
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()
# pyautogui.mouseDown()
# while (points):
#     getStroke(points[0], 0)
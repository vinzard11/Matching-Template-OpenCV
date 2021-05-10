import argparse
import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, 
	            help="path to input image where we'll apply template matching")
ap.add_argument("-t", "--template", type=str, required=True, 
	            help="path to template image")
ap.add_argument("-th", "--threshold", type=float, default=0.8,
	            help="threshold for multi-template matching")    
ap.add_argument("-s", "--scale_per", type=float, default=60,
	            help="percentage for scaling the image")                 
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
template = cv2.imread(args["template"])

scale_percent = 60
w1 = int(image.shape[1] * scale_percent / 100)
h1 = int(image.shape[0] * scale_percent / 100)
dim1 = (w1, h1)
image = cv2.resize(image, dim1)

w2 = int(template.shape[1] * scale_percent / 100)
h2 = int(template.shape[0] * scale_percent / 100)
dim2 = (w2, h2)
template = cv2.resize(template, dim2)

(tH, tW) = template.shape[:2]

cv2.imshow("image", image)
cv2.imshow("template", template)

iGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
tGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(iGray, tGray, cv2.TM_CCOEFF_NORMED)

model = str(input("For detecting 1 instance of the provided template press 1, else press 2 for detecting multiple instaces: "))
if model == '1':
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    (startX, startY) = maxLoc
    endX = startX + template.shape[1]
    endY = startY + template.shape[0]
    cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
    cv2.imshow("Output", image)
    cv2.waitKey(0)

else:
    (yC, xC) = np.where(result >= args['threshold'])
    image1 = image.copy()
    print("{} matching locations before NMS".format(len(yC)))
    
    for (x,y) in zip(xC, yC):
        cv2.rectangle(image1, (x,y), (x+tW, y+tH), (255,0,0), 3)
    cv2.imshow("before NMS", image1)
    cv2.waitKey(0)
    
    rects = []
    for (x,y) in zip(xC, yC):
        rects.append((x, y, x+tW, y+tH))
    
    #non-maxima suppression
    true = non_max_suppression(np.array(rects))
    print("{} matching locations after NMS".format(len(true)))

    for (startX, startY, endX, endY) in true:
        cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)

    cv2.imshow("After NMS", image)
    cv2.waitKey(0)
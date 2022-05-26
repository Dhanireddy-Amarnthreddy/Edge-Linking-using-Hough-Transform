import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("road.png")
smoothImage = cv2.GaussianBlur(image,(3,3),0)
plt.imshow(smoothImage)
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",image)
cv2.imshow("Gray Image",grayImage)
cannyEdges = cv2.Canny(smoothImage,120,200)
plt.imshow(cannyEdges,cmap='gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])
plt.show()
lines = cv2.HoughLinesP(cannyEdges,1,np.pi/180,threshold=100,minLineLength = 50,maxLineGap = 250)
for line in lines:
    x1, y1, x2, y2 = line [0]
    cv2.line(image,(x1, y1),(x2, y2),(255, 0, 0),3)
plt.title("Hough Transform")
plt.imshow(image)
plt.show()





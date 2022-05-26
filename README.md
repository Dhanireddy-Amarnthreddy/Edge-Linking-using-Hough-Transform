# Edge-Linking-using-Hough-Transform
## Aim:
To write a Python program to detect the lines using Hough Transform.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import the required modules.
### Step2:
Import the image to operate on.
### Step3:
Convert the imported image from BGR to GRAYSCALE.
### Step4:
Find the edges using canny edge detector and display the image.
### Step5:
Detect the points that form a line using hough transform.
### Step6:
Draw the lines on the image
### Step7:
Display the output
### Step8:
End the program.


## Program:

# Read image and convert it to grayscale image
import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("road.jpeg")
smoothImage = cv2.GaussianBlur(image,(3,3),0)
plt.imshow(smoothImage)
grayImage = cv2.cvtColor(smoothImage,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",image)
cv2.imshow("Gray Image",grayImage)

# Find the edges in the image using canny detector and display

cannyEdges = cv2.Canny(smoothImage,120,200)
plt.imshow(cannyEdges,cmap='gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])
plt.show()


# Detect points that form a line using HoughLinesP

lines = cv2.HoughLinesP(cannyEdges,1,np.pi/180,threshold=80,minLineLength = 50,maxLineGap = 250)

# Draw lines on the image

for line in lines:
    x1, y1, x2, y2 = line [0]
    cv2.line(image,(x1, y1),(x2, y2),(255, 0, 0),3)



# Display the result
plt.title("Hough Transform")
plt.imshow(image)
plt.show()

## Output

### Input image and grayscale image
<img width="304" alt="Road3" src="https://user-images.githubusercontent.com/94165103/170533913-fc7a4032-765f-442e-8df0-777824cb0539.png">
<img width="305" alt="Road2" src="https://user-images.githubusercontent.com/94165103/170533931-252dc661-546d-43de-8947-ce543e52d4ef.png">
### Canny Edge detector output
<img width="479" alt="Road1" src="https://user-images.githubusercontent.com/94165103/170534022-3fa91b2e-26b8-441b-81b2-c2aab8436634.png">

### Display the result of Hough transform
<img width="480" alt="Road4" src="https://user-images.githubusercontent.com/94165103/170534051-3568b8fb-d3f1-4a46-a2bb-f8a26ca12ce2.png">


## Result:
Thus the program is written with python and OpenCV to detect lines using Hough transform. 

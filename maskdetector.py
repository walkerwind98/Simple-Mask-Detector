#Walker Wind
#HW1-- testing some OpenCV camera use and Servo Motor 

#Description: For this homework, I am demonstrating certain uses for my Raspberry Pi,
#that I will later be using to control robotics projects. Though I have all the parts for the Pi Zero,
#I happen to own a Pi 4b, with 4 GB of ram. For this homework, I have set up the Pi 4 to connect 
#through ssh to my VS Code. The purpose of this code is to use a few commonly-used python libraries to
#play around with my camera and see if I can identfiy my black mask.
#that we were all given

#I used this tutorial to help with the color detection
#If I had more time, I would probably use machine learning,
#or some sort of shape recognition algorithm, but I am only looking for the color of the mask
#in the lighting of my apartment. 
#https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
#https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv


#Python Libraries:
from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`
image = frame
cv2.imwrite('testimage.jpg', image)


#create numpy arrays for the boundaries of colors
lower = np.array([0,0,0],dtype = "uint8")
upper = np.array([15, 15, 15],dtype = "uint8")

#find colors in boundary and apply mask
mask = cv2.inRange(image,lower,upper)
colorpixels = cv2.countNonZero(mask)
print("The number of pixels in the mask are: ", colorpixels)
print("The number of pixels in the total image are: ", mask.size)
print(colorpixels/mask.size)
if(colorpixels/mask.size > .02) :
    print("Thank you for wearing a mask")
else:
    print("You better put on a mask!")

output = cv2.bitwise_and(image,image,mask = mask)

#show the image
cv2.imwrite("mask.jpg",mask)
#cv2.imwrite("maskmask.jpg",np.hstack([image, output]))

cap.release()



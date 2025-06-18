import cv2
import numpy as np

# Mastering Computer Vision with OpenCV | Mouse Click and Color Detection Using OpenCV | Keyboard Mouse Binding Opencv
def draw(event,x,y,flags,param):
    print("X=",x)
    print("y=",y)
    print("even=",event)
    print("param=",param)
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),50,(255,255,255),7)
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+80,y+80),(0,0,255),3)

# creating window and binding to mouse
img = np.zeros((500,500,3), np.uint8)
cv2.namedWindow(winname='mywin')
cv2.setMouseCallback('mywin',draw)

while True:
    cv2.imshow('mywin',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()

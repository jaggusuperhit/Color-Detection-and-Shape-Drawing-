import cv2
import numpy as np

# drawing function
def draw(event,x,y,flags,param):
    poslist = []
    chanlist = []

    if event==cv2.EVENT_LBUTTONDOWN:
        xycord = "X="+str(x)+", Y="+str(y)
        if xycord:
            cv2.putText(img,xycord,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
            poslist.append([x,y])

    if event==cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        bgr = "B="+str(b)+",G="+str(g)+",R="+str(r)
        if bgr:
            cv2.putText(img,bgr,(x,y),cv2.FONT_ITALIC,1,(0,0,255),3)
            chanlist.append([b,g,r])
    print(chanlist)



# creating window and binding to mouse
img = cv2.imread('img.png') # rbg image
img = cv2.resize(img,(500,550))
# img = cv2.resize(img,(600,600)) # black image
cv2.namedWindow(winname='mywin')
cv2.setMouseCallback('mywin',draw)

# infinite loop
while True:
    cv2.imshow('mywin',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
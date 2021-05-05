import cv2
import numpy as np

# Function to resize image

def resize(image):
   scale_percent = 20 # percent of original size
   width = int(image.shape[1] * scale_percent / 100)
   height = int(image.shape[0] * scale_percent / 100)
   dim = (width, height)
   return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


# Function for vertical and Horizontal stacking of images
def concat_list(list):
   return cv2.vconcat([cv2.hconcat(list_2)
                                    for list_2 in list])


# Function to get contours of image
def getContours(img):
   contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
   for cnt in contours:
      area = cv2.contourArea(cnt) # Finding area under each contour
      print(area)
      if area> 500:   # removing small area under 500 pixels which may act as noise 
         cv2.drawContours(imgCopy,cnt,-1,(255,0,0),2) # Drawing contour on imgCopy
         peri = cv2.arcLength(cnt,True)  # Getting perimeter of contours
         # print(peri)
         approx = cv2.approxPolyDP(cnt,0.01*peri,True) # To approximate number of edges
         print(len(approx))
         # Creating Bounding Box
         objCor = len(approx)
         x, y, w, h = cv2.boundingRect(approx)
        
         # Conditional statement for Name of Shapes 
         if objCor == 3: 
            objectType = "Triangle"
         elif objCor == 4:
            aspRatio = w/h
            if aspRatio >0.95 and aspRatio< 1.12:
               objectType = "Square"
            else: 
               objectType = "Rectangle"
         elif objCor == 5:
            objectType = "Pentagon"
         elif objCor == 6:
            objectType = "Hexagon"
         elif objCor == 7:
            objectType = "Heptagon" 
         elif objCor == 8:
            objectType = "Octagon"  
         elif objCor == 9:
            objectType = "Nonagon" 

         else:
            aspRatio2 = w/h
            if aspRatio2> 0.95 and aspRatio2< 1.2:
               objectType = "Circle"
            else:
               objectType = "Oval"
            
         cv2.rectangle(imgCopy,(x, y),(x+w,y+h),(0,255,0))
         cv2.putText(imgCopy,objectType,(int(x+(w/2)-30),int(y+(h/2))+7),cv2.FONT_HERSHEY_COMPLEX,0.45,(0,0,0),2)
         

img_org = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Polygon.png")
img = resize(img_org)
img = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Polygon_new.png",img)
img = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Polygon_new.png")
imgCopy = img.copy()

# Converting original image to Gray image, saving the Gray image and reading saved Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Gray.png",imgGray)
imgGray = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Gray.png")

# Converting original image to Gray image, saving the Gray image and reading saved Gray image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgBlur = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Blur.png",imgBlur)
imgBlur = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Blur.png")


# Detecting edge using Canny()
imgCanny1 = cv2.Canny(imgBlur,50,50)
# imgCanny1 = resize(imgCanny)
imgCanny = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Canny.png",imgCanny1)
imgCanny = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Canny.png")

getContours(imgCanny1)

# Creating zeros 
imgBlank = np.zeros_like(img)

# Horizontal and vertical concatenation
con = concat_list([[img,imgGray,imgBlur],
                    [imgCanny,imgCopy,img]])

cv2.imshow("Stacked",con)

cv2.waitKey(0)
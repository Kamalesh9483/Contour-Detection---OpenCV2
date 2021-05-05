import cv2
import numpy as np

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
            objectType = "Tri"
         elif objCor == 4:
            objectType = "Sqr"
         elif objCor == 5:
            objectType = "Pent"
         elif objCor == 6:
            objectType = "Hex"
         elif objCor == 7:
            objectType = "Hept" 
         elif objCor == 8:
            objectType = "Oct"  
         elif objCor == 9:
            objectType = "Nano" 

         else: 
            objectType = "Cir"
            
          
         cv2.rectangle(imgCopy,(x, y),(x+w,y+h),(0,255,0))
         cv2.putText(imgCopy,objectType,(int(x+(w/2)-15),int(y+(h/2))+7),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
         

img = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Polygon.png")
img = cv2.resize(img,(500,300))
imgCopy = img.copy()


# Converting original image to Gray image, saving the Gray image and reading saved Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray = cv2.resize(imgGray,(500,300))
imgGray = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Gray.png",imgGray)
imgGray = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Gray.png")

# Converting original image to Gray image, saving the Gray image and reading saved Gray image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgBlur = cv2.resize(imgBlur,(500,300))
imgBlur = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Blur.png",imgBlur)
imgBlur = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Blur.png")


# Detecting edge using Canny()
imgCanny = cv2.Canny(imgBlur,50,50)
imgCanny2 = cv2.resize(imgCanny,(500,300))
imgCanny = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Canny.png",imgCanny2)
imgCanny = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Canny.png")

getContours(imgCanny2)


# Creating zeros 
imgBlank = np.zeros_like(img)

# Horizontal and vertical concatenation
con = concat_list([[img,imgGray,imgBlur],
                    [imgCanny,imgCopy,imgBlank]])

cv2.imshow("Stacked",con)

cv2.waitKey(0)
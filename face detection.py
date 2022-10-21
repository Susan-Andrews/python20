#References from google 

# OpenCV comes with a lot of pre-trained classifiers. For instance, there are classifiers for smile, eyes, face, etc. These come in the form of xml files.Download the xml files and place them in the data folder in the same working directory as the jupyter notebook.
# pip install opencv-python in cmd
# Read in the image using the imread function. 
# OpenCV reads images in the form of BGR, matplotlib, on the other hand, follows the order of RGB. Thus, when we read a file through OpenCV, we read it as if it contains channels in the order of blue, green and red. However, when we display the image using matplotlib, the red and blue channel gets swapped and hence the blue tinge. To avoid this issue, we will transform the channel to how matplotlib expects it to be using the cvtColor function.
# The cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues.
# For a rectangle, we need to specify the top left and the bottom right coordinates.
# 







import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')           # Loading the image to be tested
img=cv2.imread('anyfaceimage.jpg')                             
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                                           # Converting to grayscale
faces=face_cascade.detectMultiScale(gray,1.1,4)                                     # Applying the haar classifier to detect faces

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y) , (x+w , y+h) , (225,0,0) ,2)
# detectMultiscale module of the classifier. This function will return a rectangle with coordinates(x,y,w,h) around the detected face. This function has two important parameters which have to be tuned according to the data.


cv2.imshow('img',img)
cv2.waitKey()

cv2.imwrite("newnameforfile.jpg",img)

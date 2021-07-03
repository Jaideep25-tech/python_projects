import cv2
img=cv2.imread("jds.jpg")
# CONVERT TO GRAYSCALE
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# INVERT GRAYSCALE IMAGE
gray_image=cv2.bitwise_not(img)
# blur inverted image
blurred=cv2.GaussianBlur(gray_image,(21,21),0)
# invert blurred image
invert_blurred=cv2.bitwise_not(blurred)
# final sketch
sketch_image=cv2.divide(img,invert_blurred,scale=250.0)
cv2.imwrite("ash.png",sketch_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
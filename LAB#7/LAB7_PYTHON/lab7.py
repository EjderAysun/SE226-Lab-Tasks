# Please enter the LAB#7 folder and run!
# Install opencv2 before starting, you can use "pip install opencv-python" command.
# jpg source: https://www.pexels.com/photo/blue-green-and-red-abstract-illustration-1566909/
# task 1 #
import cv2

# task 2 #
load = cv2.imread('Mission_Documents#7/pexels-alexander-grey-1566909.jpg', 1)
load = cv2.resize(load, (int(load.shape[1]/4), int(load.shape[0]/4)))

# task 3 & 4#
(R, G, B) = cv2.split(load)

# task 5 #
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# task 6 #
red = cv2.normalize(R, None, 0, 255, cv2.NORM_MINMAX)
green = cv2.normalize(G, None, 0, 0, cv2.NORM_MINMAX)
blue = cv2.normalize(B, None, 0, 255, cv2.NORM_MINMAX)

# task 7 #
processed_image = cv2.merge([blue, green, red])

cv2.imshow("Processed Image", processed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
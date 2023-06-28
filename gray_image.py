import cv2

image_path = "origin_image/image5.png"
image = cv2.imread(image_path)
image_name = image_path.split("/")[-1]


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_image/gray_" + image_name, gray_image)

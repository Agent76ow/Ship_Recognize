from skimage.metrics import structural_similarity as ssim
import cv2

image1 = cv2.imread("origin_image/image1.png")
image2 = cv2.imread("gray_image/gray_image1.png")

similarity = ssim(image1, image2, multichannel=True)
if similarity == 1:
    print("两张图像完全相同")
else:
    print("两张图像存在差异")
print(similarity)


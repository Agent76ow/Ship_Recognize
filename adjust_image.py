import cv2
import os

# 读取图像
def image_adjust(image_path):

    image_path = image_path
    image = cv2.imread(image_path, 0)  # 以灰度模式读取图像
    image_name = image_path.split('\\')[-1]

    # 调整对比度和亮度
    alpha = 1.2  # 对比度增强因子
    beta = 20  # 亮度增强因子
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    adjusted_image2 = adjusted_image

    # 直方图均衡化
    equalized_image = cv2.equalizeHist(adjusted_image)

    # 滤波操作
    kernel_size = 3  # 滤波器大小
    blurred_image = cv2.GaussianBlur(equalized_image, (kernel_size, kernel_size), 0)
    blurred_image2 = cv2.GaussianBlur(adjusted_image2, (kernel_size, kernel_size), 0)

    # 显示结果 并 保存图像
    # cv2.imshow("adjusted_image", adjusted_image)
    # if there not existing the folder then create a new one
    if not os.path.exists("adjusted_image"):
        os.mkdir("adjusted_image")
    cv2.imwrite(f"adjusted_image/ajusted_{image_name}", adjusted_image)


    # cv2.imshow("equalized_image", equalized_image)
    if not os.path.exists("equalized_image"):
        os.mkdir("equalized_image")
    cv2.imwrite(f"equalized_image/ajusted_{image_name}", equalized_image)

    # cv2.imshow("blurred_image", blurred_image)
    if not os.path.exists("blurred_image"):
        os.mkdir("blurred_image")
    cv2.imwrite(f"blurred_image/ajusted_{image_name}", blurred_image)

    # cv2.imshow("blurred_image(no equalized)", blurred_image2)
    if not os.path.exists("blurred_image(no equalized)"):
        os.mkdir("blurred_image(no equalized)")
    cv2.imwrite(f"blurred_image(no equalized)/ajusted_{image_name}", blurred_image2)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
image_foler = "origin_image"
for image in os.listdir(image_foler):
    image_path = os.path.join(image_foler, image)
    print(image_path)
    image_adjust(image_path)
    
# image_adjust("origin_image/image1.png")
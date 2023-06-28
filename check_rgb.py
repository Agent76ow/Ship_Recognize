from PIL import Image

def check_rgb_image(image_path):
    try:
        image = Image.open(image_path)
        if image.mode == 'RGB':
            print("该图片是RGB三通道图片")
        else:
            print("该图片不是RGB三通道图片")
    except IOError:
        print("无法打开该图片")

# 调用函数来检查图片
check_rgb_image("origin_image/image5.png")
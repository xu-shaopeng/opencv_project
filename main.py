import cv2  
import numpy as np  
  
def add_gaussian_noise(image, mean=0, var=0.1):  
    """  
    给图片添加高斯噪声  
    :param image: 输入的图片，应该是灰度图或彩色图  
    :param mean: 噪声的均值  
    :param var: 噪声的方差  
    :return: 添加了高斯噪声的图片  
    """  
    if image is None:  
        raise ValueError("Image not loaded correctly")  
  
    row, col, ch = image.shape  
    gauss = np.random.normal(mean, var**0.5, (row, col, ch))  
      
    # 将噪声图像与原图相加  
    noisy = image + gauss  
      
    # 裁剪像素值，防止超出范围（0-255）  
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)  
      
    return noisy  
  
# 读取图片  
image_path = 'st.png'  # 替换为你的图片路径  
image = cv2.imread(image_path)  
  
if image is None:  
    print(f"Error: Unable to load image at {image_path}")  
else:  
    # 添加高斯噪声  
    noisy_image = add_gaussian_noise(image, mean=0, var=0.05)  # 调整var的值以改变噪声强度  
  
    # 显示原图和加噪后的图  
    cv2.imshow('Original Image', image)  
    cv2.imshow('Noisy Image', noisy_image)  
      
    # 等待按键后关闭窗口  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
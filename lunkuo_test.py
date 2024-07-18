import cv2  
import numpy as np  
  
def extract_contours(image_path):  
    # 读取图片  
    image = cv2.imread(image_path)  
    if image is None:  
        print("Error: 图片未找到或路径错误")  
        return  
  
    # 转换为灰度图  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
  
    # 应用阈值处理进行二值化  
    # 这里使用固定阈值，但你可以根据图片调整thresh和maxval的值  
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  
  
    # 查找轮廓  
    # 注意：findContours函数的返回值在不同的OpenCV版本中可能有所不同  
    # 这里使用OpenCV 4.x的返回方式  
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
  
    # 在原图上绘制轮廓  
    # 注意：绘制轮廓时，原图的拷贝是必要的，因为findContours会修改原图  
    contour_img = image.copy()  
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 3)  
  
    # 显示原图和处理后的图片  
    cv2.imshow('Original Image', image)  
    cv2.imshow('Contours', contour_img)  
  
    # 等待按键操作  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
  
# 调用函数  
extract_contours('st.png')
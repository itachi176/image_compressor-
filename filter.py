import cv2
import numpy as np 
org_img = cv2.imread("./image/lena.png")
org_img = cv2.resize(org_img, (351,331))
new_image = cv2.imread("./image_compress_15.png")
def psnr(org_image, new_image):
    mse = np.square(org_image - new_image).mean()
    mse = round(mse, 5)
    psnr = 10*(np.log10((255*255)/mse))
    psnr = round(psnr, 5)
    return psnr
psnr = psnr(org_img, new_image)
print(psnr)
new_image_filter = cv2.bilateralFilter(new_image, 9,75,75)
mse = np.square(org_img-new_image_filter).mean()
psnr = 10*(np.log10((255*255)/mse))
psnr = round(psnr, 5)
print(psnr)
# cv2.imshow('ad', new_image_filter)
# cv2.waitKey()
# import the necessary packages
from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

def convolution(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    pad = (kW - 1) // 2 
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype = "float32")
    # loop over the input image, "sliding" the kernel across
	# each (x, y)-coordinate from left-to-right and top to
	# bottom
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
			# extract the ROI of the image by extracting the
			# *center* region of the current (x, y)-coordinates
			# dimensions
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			# perform the actual convolution by taking the
			# element-wise multiplicate between the ROI and
			# the kernel, then summing the matrix
            k = (roi * kernel).sum()
			# store the convolved value in the output (x,y)-
			# coordinate of the output image
            output[y - pad, x - pad] = k
    # rescale the output image to be in the range [0, 255]
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
	# return the output image
    return output

image = cv2.imread("./emma.png")
kernel = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
a = convolution(image, kernel)
cv2.imshow("anh", a)
cv2.waitKey()
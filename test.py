from encode import *
from compress import *
import cv2
img = cv2.imread("emma.png", 0)
# cv2.imshow("origin", img)
print(img.shape)
bitstream = encode(img)
compress = compress(bitstream)
cv2.imshow("origin", img)
cv2.imshow("compress", compress)
cv2.imwrite("compress.bmp", compress)
cv2.waitKey()
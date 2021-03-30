from encode import *
from compress import *
from huffman import *
import cv2
img = cv2.imread("lena.png", 0)
# cv2.imshow("origin", img)
print(img.shape)
encode_text = encode(img)
compress = compress(encode_text)
cv2.imshow("origin", img)
cv2.imshow("compress", compress)
cv2.imwrite("compress.bmp", compress)
cv2.waitKey()
from encode import *
from compress import *
from huffman import *
import cv2
img = cv2.imread("emma.png", 0)
block_size = 8
QUANTIZATION_MAT = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56 ],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]])

[h, w] = img.shape
    #copy h, w to caculator 
height = h
width = w
h = np.float32(h)
w = np.float32(w)

nbh = math.ceil(h/block_size) #lam tron len va chia chieu cao ra thanh cac block 8
nbh = np.int32(nbh)

nbw = math.ceil(w/block_size) #lam tron len va chia chieu rong ra thanh cac block 8
nbw = np.int32(nbw)

    #pad image because sometime size not divable to block size
    #print(nbh)
H = block_size * nbh
    #print (H)
W = block_size * nbw

padd_img = np.zeros((H, W))

padd_img[0:height,0:width] = img[0:height,0:width]
    # print((padd_img).shape)
    # cv2.imshow("pad img", np.uint8(padd_img))
    #image->block 8x8 
    #dct with each block
cv2.imshow("normal", img)
for i in range (nbh):
    row1 = i * block_size
    row2 = row1 + block_size
    for j in range(nbw):
        col1 = j*block_size
        col2 = col1 + block_size
        block = padd_img[row1:row2, col1:col2]
        DCT = cv2.dct(block)
        DCT_normalized = np.divide(DCT,QUANTIZATION_MAT).astype(int)     
        reordered = zigzag(DCT_normalized)
            #reshape to 8x8
        reshaped= np.reshape(reordered, (block_size, block_size)) 
            #copy block to padd_image
        padd_img[row1:row2, col1:col2]=(reshaped/1)
        cv2.imshow("quantization", padd_img)
cv2.waitKey()
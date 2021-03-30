from zigzag import *
from huffman import *
import cv2
import math
def encode(img):
    #defind block size 
    block_size = 8
    #quantization matrix 
    QUANTIZATION_MAT = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56 ],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]])

    #img = cv2.imread('emma.png', cv2.IMREAD_GRAYSCALE)
    #cv2.imshow("pad img", img)

    #print(img.shape)
    #size of image 

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
    print((padd_img).shape)
    # cv2.imshow("pad img", np.uint8(padd_img))
    #image->block 8x8 
    #dct with each block
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
            padd_img[row1:row2, col1:col2]=reshaped

    def get_run_length_encoding(image):
        i = 0
        skip = 0
        stream = []    
        bitstream = ""
        image = image.astype(int)
        while i < image.shape[0]:
            if image[i] != 0:            
                stream.append((image[i],skip))
                bitstream = bitstream + str(image[i])+ " " +str(skip)+ " "
                skip = 0
            else:
                skip = skip + 1
            i = i + 1

        return bitstream

    array = padd_img.flatten()
    print(array)
    #cv2.imshow("padd_img", padd_img)

    bitstream = get_run_length_encoding(array)
    bitstream = str(padd_img.shape[0]) + " " + str(padd_img.shape[1]) + " " + bitstream + ";"
    #print(bitstream)
    #cv2.waitKey()
    tree = HuffmanTree()
    tree.build_tree(bitstream)
    encoded_text = tree.encode(bitstream)
    # print("Encoded text: {}\n".format(" ".join("{:02x}".format(c) for c in encoded_text)))
   
    # print(encoded_text)
    file2 = open("encode_text.txt", 'wb')
    file2.write(encoded_text)
    file2.close()

    return encoded_text

# img = cv2.imread("emma.png", 0)
# cv2.imshow("sd", img)
# cv2.waitKey()
# bitstream = encode(img)
# print(bitstream)

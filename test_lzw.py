import io

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            
            dict_size += 1
            w = c

    #Output the new Dictionary.       
    newDictionary = list(dictionary.items())
    print("****New Dictionary****")
    print(" ITEM  INDEX ")
    for d in newDictionary[256:]:
        print(d,"\n")
       
    #Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

def decompress(compressed):
    """Decompress a list of output ks to a string."""
    
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    
    result = io.StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()

import cv2 

img = cv2.imread("emma.png", 0)
img = img.flatten()
a = compress(str(img))
b = decompress(a)
bitsteam = ''
for i in range(len(a) - 1):
    bnr = bin(a[i])
    bitsteam = bitsteam + bnr[2:]
print(len(a))

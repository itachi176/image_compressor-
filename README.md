# image_compressor-
- Giao diện cơ bản mô phỏng hệ thống nén ảnh theo chuẩn JPEG sử dụng python, opencv, pyqt5: 

1) Flow Diagram

- Encode:
![](image/flow%20diagram.png)




- Decode: 



![](image/flow%20diagram1.png)


2) Mô tả hoạt động 
- Encode: 
+ Chia ảnh thành các block nhỏ 8x8 múc đích để giảm thời gian tính toán
+ Do không phải ma trận ảnh nào cũng chia hết cho 8 nên phải padd thêm các điểm ảnh 0 bên ngoài để chia đủ khối 8x8 
+ Với mỗi khối 8x8 biến đổi DCT 
+ Thu được ảnh mới sau DCT 
+ Lượng tử hóa với bẳng lượng tử và thuật toán zigzag 
+ Trải ma trận thu được thành ma trận 1-D
+ Run Length Coding hoặc Huffman 
- Decode: 
+ Giải mã để thu được ảnh phục hồi 

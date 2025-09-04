

from PIL import Image
import numpy
import time
import struct
import random

# file_path="F:\book.txt"
# imglist = []
# try:
#     with open(file_path, 'rb') as f:
#         data = bytearray(f.read())
# except FileNotFoundError:
#     print(f"Error: The file {file_path} does not exist.")
#     exit(1)
#
# # Ensure the length of data is a multiple of 3 by padding with zeros if necessary
# while len(data) % 3 != 0:
#     data.append(0)
#
# num_pixels = len(data) // 3
# width = int(num_pixels ** 0.5)
# height = (num_pixels + width - 1) // width
#
# pixel_data = []
# for i in range(height * width):
#     if i < num_pixels:
#         r = data[i * 3]
#         g = data[i * 3 + 1]
#         b = data[i * 3 + 2]
#         pixel_data.append(list((r, g, b)))
#     else:
#         pixel_data.append(list((0, 0, 0)))  # Fill remaining pixels with black if necessary
# print("dfsdfse")
# tuplelist=[]
# chongfunum = 0
# ddnum = 0
# allnum=0
# print(len(pixel_data))
# for i in pixel_data:
#     # print(type(i))
#     # break
#     allnum+=1
#     if allnum%10000==0:
#         print(allnum/10000)
#     if i in imglist:
#         chongfunum += 1
#         # print("ddd")
#     else:
#         tuplelist.append(tuple(i))
#         imglist.append(i)
#
# print(chongfunum, "重复数字")
# allnums=len(imglist)
# print(allnums, "总数")
#
# for i in range(1000):
#     for j in range(i-10,i):
#         if i*j >allnums:
#             break
#     if i * j > allnums:
#         break
# for i in range((i*j-allnums-1)):
#     tuplelist.append((0,0,0))
#
# image = Image.new('RGB', (i, j))
# image.putdata(tuplelist)
# image.save("yasuotu1.png")







listdict={}
img=Image.open("yasuotu1.png","r")
arr=numpy.array(img)
# print(arr)
alnum=0
for i in arr:
    for j in i:
        dt=tuple(j)
        listdict[dt]=alnum
        alnum+=1

print(len(listdict))


file_path="F:\book.txt"
# imglist = []

with open(file_path, 'rb') as f:
    data = bytearray(f.read())
num_pixels = len(data) // 3
width = int(num_pixels ** 0.5)
height = (num_pixels + width - 1) // width
allldatall=0
pixel_data = []
for i in range(height * width):
    if i < num_pixels:
        allldatall+=1
        if allldatall%10000==0:
            print(allldatall/10000)
            time.sleep(.2)
        r = data[i * 3]
        g = data[i * 3 + 1]
        b = data[i * 3 + 2]
        pixel_data.append(listdict[(r, g, b)])
    else:
        pixel_data.append(listdict[(0, 0, 0)])


# 生成一个包含10000到30000个数字的列表，每个数字在0到65535之间
# num_elements = random.randint(0, 65535)
# numbers = [random.randint(0, 65535) for _ in range(num_elements)]
# 使用struct.pack将数字列表打包成二进制数据
# '<H' 表示小端序的无符号短整型（2字节）
# data_list = [i % 65536 for i in range(160000)]

# 使用struct.pack将整个列表打包成字节数据
byte_data = b''.join(struct.pack('<H', num) for num in pixel_data)

# 打印结果以验证转换
# print(f"Length of byte {len(byte_data)} bytes")

# 将二进制数据写入文件
with open('book1.txt', 'wb') as file:
    file.write(byte_data)

print("Data has been written to 'numbers.bin'")








import os
from PIL import Image
import numpy
import time
def create_image_from_file(file_path,saveimg):
    # Read the file in binary mode
    with open(file_path, 'rb') as f:
        data = f.read()

    # Calculate the number of pixels
    num_pixels = len(data) // 3

    # Determine the dimensions of the image
    width = int(num_pixels ** 0.5)
    height = (num_pixels + width - 1) // width

    # Create an array of pixel data and fill it with the file's content
    pixel_data = []
    for i in range(height * width):
        if i < num_pixels:
            r = data[i * 3]
            g = data[i * 3 + 1]
            b = data[i * 3 + 2]
        else:
            r, g, b = 0, 0, 0  # Fill extra space with black pixels
        pixel_data.append((r, g, b))

    # Create and save the image
    image = Image.new('RGB', (width, height))
    image.putdata(pixel_data)
    image.save(saveimg)

def create_image_to_file(file_path,fileto):
    filename_path=open(fileto, 'wb')
    img=Image.open(file_path,"r")
    arr=numpy.array(img)
    for i in arr:
        for j in i:
            filename_path.write(bytes(j))
    filename_path.close()

# Example usage
file1="F:\xiaoshuo.txt"
file2="xiaoshuo.txt"
saveimg="opt.png"
create_image_from_file(file_path=file1,saveimg=saveimg)
time.sleep(1)
create_image_to_file(file_path=saveimg,fileto=file2)

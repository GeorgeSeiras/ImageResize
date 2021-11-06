#!/usr/bin/env python3
from PIL import Image,ImageOps
import os

path = os.getcwd()+"\\"
dirs = os.listdir( path )
final_size = 1024;

def resize_aspect_fit():
    if(os.path.exists(path+"\\resized") == False):
        os.mkdir(path+"\\resized")
    for item in dirs:
        if item == '.DS_Store':
            continue
        if os.path.isfile(path+item) &( (path+item).endswith('.jpg') | (path+item).endswith('.png')):
            original_image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)
            fixed_image = ImageOps.exif_transpose(original_image)

            #change image dimensions, keeping the aspect ratio intact
            size = fixed_image.size
            new_image_height = 1024
            new_image_width = int(size[1] / size[0] * new_image_height)

            #save image in the resized folder, as a jpg keeping 70% of the original quality
            fixed_image = fixed_image.resize((new_image_height, new_image_width), Image.ANTIALIAS)
            fixed_image.save(path+"\\resized\\"+os.path.basename(file_path) + "_resized" + extension, 'JPEG', quality=70)
resize_aspect_fit()
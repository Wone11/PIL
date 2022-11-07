from os import listdir
from PIL import Image
import os

'''firts option methods here---- '''
def Option_One():   
    # set source and target dirs:
    src_dir = "images/"
    new_dir = "opt/icons/"

    # set reprocess vars:
    rotation_90dg = -90
    resize_size = (128, 128)

    # support. PNG would be a more suitable option, but the lab calls for JPEG.
    image_format = "JPEG"

    # gather list of image files:
    img_files = [f for f in listdir(src_dir) if f.startswith("ic_")]

    # reprocess images:
    for file in img_files:
        src_img = Image.open(src_dir + file)

        # rotate & resize image:
        new_img = src_img.rotate(rotation_90dg).resize(resize_size)

        # NOTE: we need to convert to RGB here to avoid error:
        new_img = new_img.convert("RGB")

        # save new output file:
        new_img.save(new_dir + file, image_format)
        
        print(new_img)
    
def Option_Two():
    #define directory here
    directory = "images"
    save_dir  = "/opts/icons/"

    #collect the files and correct bad format
    for files in os.listdir(directory):
        if files.startswith("ic_"):
            img_data = Image.open(os.path.join(directory,files))
            img_data = img_data.rotate(-90)
            img_data = img_data.resize((128,128))
            img_data = img_data.convert("RGB")
            img_data.save(os.path.join(save_dir,files+".jpeg"))


#call methons here
# Option_One()
Option_Two()
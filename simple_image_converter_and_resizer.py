"""Hello there! Here is my very first project on GitHub. 
I made it for my working purposes. I would be grateful for your comments"""

#to jpg converter and resiser READY

import os
import datetime
import imghdr
from PIL import Image

def get_cur_date_time_yyyy_mm_dd__hh_mm_ss():
    cur_time = datetime.datetime.now()
    curtime_str = str(cur_time).split(" ")
    curdate_yyyy_mm_dd_ready = curtime_str[0].split("-")[0] + "_" + curtime_str[0].split("-")[1] + "_" + curtime_str[0].split("-")[2]
    curtime_hh_mm_ss = curtime_str[1].split(".")[0]
    curtime_hh_mm_ss_ready = curtime_hh_mm_ss.split(":")[0] + "_" + curtime_hh_mm_ss.split(":")[1] + "_" + curtime_hh_mm_ss.split(":")[2]
    cur_date_time = curdate_yyyy_mm_dd_ready + "__" + curtime_hh_mm_ss_ready
    return cur_date_time

def resize_all_images_in_folder(folder_name):
    cur_dir = os.getcwd()

    picture_list = os.listdir(folder_name)

    width = int(input("Enter width ") or "1000")


    MAX_SIZE = (width, width)

    resize_out_folder_name = folder_name + "_" + get_cur_date_time_yyyy_mm_dd__hh_mm_ss()
    os.makedirs(resize_out_folder_name)


    for index, picture_name in enumerate(picture_list):
        #image = Image.open(cur_dir + "\\" + folder_name + "\\" + picture_name)
        image = Image.open(folder_name + "\\" + picture_name)
        image.thumbnail(MAX_SIZE)
        #image.save(cur_dir + "\\" + resize_out_folder_name + "\\" + picture_name)
        image.save(resize_out_folder_name + "\\" + picture_name)

    print(f'Resize compliter. {index + 1} images resized')


cur_dir = os.getcwd()

want_convert = input("Do you want to convert images to jpg? Y/n ").lower()
if want_convert == 'y':
    
    inp_folder_name = input("Type the name of folder where your images are (don't forget to put folder with images in the same directory as script)")
    picture_list = os.listdir(inp_folder_name)


    out_folder_name = cur_dir + "\\out_pics" + get_cur_date_time_yyyy_mm_dd__hh_mm_ss()

    os.makedirs(out_folder_name)


    for index, picture_name in enumerate(picture_list):
        im = Image.open(cur_dir + "\\" + inp_folder_name + "\\" + picture_name).convert("RGB")
        im.save(out_folder_name + "\\" + picture_name.split(".")[0]+".jpg","jpeg")

    print(f"Convertion completed. I converted {index+1}  images to .jpg")  
    
want_resize = input("Do you want to resize images? Y/n ").lower()

if want_resize == 'y' and want_convert == 'y':
    print(f"Out folder name = {out_folder_name}")
    inp_folder_name = out_folder_name
    print(inp_folder_name.split('\\')[-1])
    #resize_all_images_in_folder(inp_folder_name.split('\\')[-1])
    resize_all_images_in_folder(inp_folder_name)
elif want_resize == 'y' and want_convert != 'y':
    inp_folder_name = input("Enter the name of folder with images ")
    resize_all_images_in_folder(inp_folder_name)

    
    
"""
    This script takes the text file containing YOLO format annotation which has following structure:
    label xmin ymin xmax ymax
    and converts to csv having following format:
    image, xmin, ymin, xmax, ymax, label

    based on this formula...
    x = xmin / width
    y = ymin / height
    w = (xmax - xmin) / width
    h = (ymax - ymin) / height
     so,
     xmin = x * width
     ymin = y * height
     xmax = (w * width) + xmin
     ymax = (h * height) + ymin
 """

import sys
import os
import pandas as pd
import PIL

imgFolderPath = sys.argv[1]

# Intialize the dateframe
col_names = ["image", "xmin", "ymin", "xmax", "ymax", "label"]
df_annotation_info = pd.DataFrame(columns=col_names)
label = "Fish"

# Search all yolo files in this folder
for file in os.listdir(imgFolderPath):
    if file.endswith(".txt"):
        # print(file)
        file_name = os.path.splitext(file)[0]
        image_name = file_name + ".jpg"

        file_path = os.path.join(imgFolderPath, file)
        txt_file = open(file_path)
        for each_line in txt_file:
            list_column_info = each_line.split()
            # print("List of a row info >>>>")
            # print(list_column_info)

            image = PIL.Image.open(image_name)
            width, height = image.size

            x = list_column_info[1]
            y = list_column_info[2]
            w = list_column_info[3]
            h = list_column_info[4]

            xmin = x * width
            ymin = y * height
            xmax = (w * width) + xmin
            ymax = (h * height) + ymin

            new_entry = {"image": image_name, "xmin": xmin, "ymin": ymin, "xmax":
                xmax, "ymax": ymax, "label": label}
            df_annotation_info.loc[len(df_annotation_info)] = new_entry
        txt_file.close()

print(df_annotation_info)
df_annotation_info.to_csv('Annotations-export.csv', index= False)
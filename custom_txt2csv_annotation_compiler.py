import sys
import os
import pandas as pd

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
            new_entry = {"image": image_name, "xmin": list_column_info[1], "ymin": list_column_info[2], "xmax":
                list_column_info[3], "ymax": list_column_info[4], "label": label}
            df_annotation_info.loc[len(df_annotation_info)] = new_entry
        txt_file.close()

print(df_annotation_info)
df_annotation_info.to_csv('Annotations-export.csv', index= False)
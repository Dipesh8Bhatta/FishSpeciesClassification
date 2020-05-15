import pandas as pd
from PIL import Image
import os
import glob
# import macpath

import classify as cs

def find_test_image_YOLOv3():
    # Need to write code here
    return "Data/Source_Images/Test_Images/blastie.jpeg"


def crop_detected_image_area():
    df = pd.read_csv("Data/Source_Images/Test_Image_Detection_Results/Detection_Results.csv")
    # print(df)
    # Iterate over the pandas dataframe.
    for index, row in df.iterrows():
        print(row)
        # Have to use strip to remove space in image path.
        source_image_path = row['image_path']
        print(source_image_path)
        im = Image.open(source_image_path)
        im_crop = im.crop((row['xmin'], row['ymin'], row['xmax'], row['ymax']))
        destination_image_path = os.path.join("examples", str(row['label'])+"-"+row['image'])
        im_crop.save(destination_image_path, quality=95)
        im_crop.show()

def clear_directory(directory):
    files = glob.glob(directory + '/*')
    for f in files:
        os.remove(f)

def main():
    print("Welcome to Fish Classification System...")

    # Find the Images path for the object detection using YOLOv3.
    test_image_YOLOv3 = find_test_image_YOLOv3()

    # Use YOLOv3 for object detection and return path.

    # Function to crop the detected image from the YOLOv3 prediction.
    crop_detected_image_area()

    # Function to classify images using tiny VGGNet
    for test_image in os.listdir("examples"):
        print("this is test image......" + test_image)
        test_image_path = os.path.join("examples", test_image)
        cs.classify("fishSpeciesClassification.model", "lb.pickle", test_image_path)

    # Function to clear the directories
    # clear_directory("Data/Source_Images/Test_Images")
    clear_directory("examples")


if __name__ == "__main__":
    main()

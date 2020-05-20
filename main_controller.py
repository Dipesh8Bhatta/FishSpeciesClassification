import pandas as pd
from PIL import Image
import os
import glob
# import macpath

import Detector as dt
import classify as cs


def get_parent_dir(n=0):
    """ returns the n-th parent directory of the current
    working directory """
    current_path = os.path.dirname(os.path.abspath(__file__))
    for k in range(n):
        current_path = os.path.dirname(current_path)
    return current_path


# Set up path for the essential locations.
data_folder = os.path.join(get_parent_dir(n=0), "Data")
model_weights = os.path.join(data_folder, 'Model_Weights')
source_images = os.path.join(data_folder, 'Source_Images')
image_classification_source = os.path.join(source_images, "examples")


def find_test_image_YOLOv3():
    test_images_path = os.path.join(source_images, 'Test_Images')
    return test_images_path


def crop_detected_image(detection_results_folder):
    detection_results_info_csv = os.path.join(detection_results_folder, 'Detection_Results.csv')
    df = pd.read_csv(detection_results_info_csv)
    # print(df)
    # Iterate over the pandas dataframe.
    for index, row in df.iterrows():
        print(row)
        # Have to use strip to remove space in image path.
        source_image_path = row['image_path']
        print(source_image_path)
        im = Image.open(source_image_path)
        im_crop = im.crop((row['xmin'], row['ymin'], row['xmax'], row['ymax']))
        image_classification_source_path = os.path.join(image_classification_source, str(row['label'])+"-"+row['image'])
        im_crop.save(image_classification_source_path, quality=95)
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
    detection_results_folder = dt.detect(test_image_YOLOv3)
    print(">>>>>>>>>>>>>>>>>>>")
    print(detection_results_folder)

    # Function to crop the detected image from the YOLOv3 prediction.
    crop_detected_image(detection_results_folder)

    # Function to classify images using tiny VGGNet
    for test_image in os.listdir(image_classification_source):
        print("This is test image..." + test_image + "...for VGGNET classification.")
        test_image_path = os.path.join(image_classification_source, test_image)
        vggnet_model_path = os.path.join(model_weights, "fishSpeciesClassification.model")
        pickle_path = os.path.join(model_weights, "lb.pickle")
        cs.classify(vggnet_model_path, pickle_path, test_image_path)

    # Function to clear the directories.
    # TO DO: path passed as an argument should be managed.
    clear_directory("Data/Source_Images/Test_Images")
    clear_directory("examples")


if __name__ == "__main__":
    main()

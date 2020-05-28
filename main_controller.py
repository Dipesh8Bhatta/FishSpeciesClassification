import pandas as pd
from PIL import Image
import os
import glob

import detect as dt
import classify as cs
import file_paths as fp


def find_test_image_YOLOv3():
    return fp.test_images_path


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
        image_classification_source_path = os.path.join(fp.image_classification_source, str(row['label']) + "-" +
                                                        str(index) + "-" + row['image'])
        im_crop.save(image_classification_source_path, quality=95)
        # im_crop.show()


def clear_directory(directory):
    files = glob.glob(directory + '/*')
    for f in files:
        os.remove(f)


def main():
    print("Welcome to Fish Classification System...")

    # Clear previously identified fish images result from Test_Classification, Test_Image_Detection_Results and Result folder.
    print(">>>>>>>>>>>>>>>>>>>")
    print("Cleaning previous result...")
    clear_directory(fp.detection_results_folder)
    clear_directory(fp.image_classification_source)

    # Find the Images path for the object detection using YOLOv3.
    print(">>>>>>>>>>>>>>>>>>>")
    print("Managing photos for detection...")
    test_image_YOLOv3 = find_test_image_YOLOv3()

    # Use YOLOv3 for object detection and return path.
    print(">>>>>>>>>>>>>>>>>>>")
    print("Running YOLOv3 for detection...")
    detection_results_folder = dt.detect(test_image_YOLOv3)

    # Function to crop the detected image from the YOLOv3 prediction.
    print(">>>>>>>>>>>>>>>>>>>")
    print("Cropping detected images from.." + detection_results_folder)
    crop_detected_image(detection_results_folder)

    # classify images using tiny VGGNet
    print(">>>>>>>>>>>>>>>")
    print("Running Smaller VGGNet for classification...")
    cs.classify(fp.vggnet_model_path, fp.pickle_path, fp.image_classification_source, fp.final_output)


if __name__ == "__main__":
    main()

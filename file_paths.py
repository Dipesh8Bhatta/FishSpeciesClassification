import os


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

test_images_path = os.path.join(source_images, 'Test_Images')
image_classification_source = os.path.join(source_images, "examples")
vggnet_model_path = os.path.join(model_weights, "fishSpeciesClassification.model")
pickle_path = os.path.join(model_weights, "lb.pickle")

detection_results_folder = os.path.join(source_images, "Test_Image_Detection_Results")
detection_results_file = os.path.join(detection_results_folder, "Detection_Results.csv")

YOLO_weights = os.path.join(model_weights, "trained_weights_final.h5")
anchors_path = os.path.join(model_weights, "yolo_anchors.txt")

training_images_YOLO = os.path.join(source_images, "Training_Images")
voTT_Folder = os.path.join(training_images_YOLO, "vott-csv-export")
YOLO_filename = os.path.join(voTT_Folder, "data_train.txt")
YOLO_classname = os.path.join(model_weights, "data_classes.txt")

log_dir = model_weights
weights_path = os.path.join(model_weights, "yolo.h5")

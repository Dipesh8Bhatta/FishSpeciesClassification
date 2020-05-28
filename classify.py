# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras import backend
import numpy as np
# import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-m", "--model", required=True,
# 	help="path to trained model model")
# ap.add_argument("-l", "--labelbin", required=True,
# 	help="path to label binarizer")
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())
def classify(model_path, label, image_classification_source, final_output):
	# load the trained convolutional neural network and the label
	# binarizer
	print("[INFO] loading network...")
	# model = load_model(args["model"])
	backend.clear_session()
	model = load_model(model_path, compile=False)
	# lb = pickle.loads(open(args["labelbin"], "rb").read())
	lb = pickle.loads(open(label, "rb").read())

	for test_image in os.listdir(image_classification_source):
		print("This is test image..." + test_image + "...for VGGNET classification.")
		image_path = os.path.join(image_classification_source, test_image)
		# load the image
		# image = cv2.imread(args["image"])
		image = cv2.imread(image_path)
		output = image.copy()
		# pre-process the image for classification
		image = cv2.resize(image, (96, 96))
		image = image.astype("float") / 255.0
		image = img_to_array(image)
		image = np.expand_dims(image, axis=0)

		# classify the input image
		print("[INFO] classifying image...")
		proba = model.predict(image)[0]
		idx = np.argmax(proba)
		label = lb.classes_[idx]

		# we'll mark our prediction as "correct" of the input image filename
		# contains the predicted label text (obviously this makes the
		# assumption that you have named your testing image files this way)
		# filename = args["image"][args["image"].rfind(os.path.sep) + 1:]
		filename = image_path[image_path.rfind(os.path.sep) + 1:]
		correct = "correct" if filename.rfind(label) != -1 else "incorrect"
		# build the label and draw the label on the image
		label = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, correct)
		output = imutils.resize(output, width=400)
		cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
			0.7, (0, 255, 0), 2)
		# show the output image
		print("[INFO] {}".format(label))
		cv2.imshow("Output", output)

		# final output path.
		# final_image_path = os.path.join(final_output, test_image)
		# print(">>>>>>>>>>>>>>>>>>>>")
		# print(final_image_path)
		# print(output)
		# if not cv2.imwrite(final_image_path, output):
		# 	raise Exception("Could not write image")

		cv2.waitKey(0)


def main():
	classify("Data/Model_Weights/fishSpeciesClassification.model", "Data/Model_Weights/lb.pickle",
			 "/home/bishal/PycharmProjects/FishSpeciesClassification/Data/Source_Images/Test_Classification")


if __name__ == "__main__":
	main()

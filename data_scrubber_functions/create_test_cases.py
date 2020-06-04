"""This module was created to rename the large number of images of a class of fish to that class name."""

import shutil, random, os

"""This is the location from where you are selecting test images.
Modify it before running this function."""
src_directory = 'CLEANED/Tetrapturus_georgii'

"""This is the location where you store your test cases.
Modify this location before using it."""
des_directory = 'large_test_images'
filenames = random.sample(os.listdir(src_directory), 3)


def main():
    for i, fname in enumerate(filenames):
        src_file = os.path.join(src_directory, fname)
        """Change here for file name"""
        new_fname = "Tetrapturus_georgii_" + str(i) + ".jpg"
        dst_file = os.path.join(src_directory, new_fname)
        os.rename(src_file, dst_file)
        src_path = os.path.join(src_directory, new_fname)
        shutil.move(src_path, des_directory)


if __name__ == '__main__':
    main()

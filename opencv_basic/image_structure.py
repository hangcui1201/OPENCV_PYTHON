#!/usr/bin/env python

import cv2
import numpy as np 

image_name = "tiger"

def main():

	print("Read an image ...")
	image = cv2.imread("./images/"+image_name+".jpg")

	print("Display the content of the image ...")
	print(image)

	print("\nIn Python, an image is stored in a numpy array.")
	print("The type of the image: %s" % type(image))
	print("The data type of a pixel: %s" % image.dtype)
	print("The size of the image: %d" % image.size)
	print("The shape of the image: %s" % str(image.shape))
	print("The number of rows(height): %d" % image.shape[0])
	print("The number of columns(width): %d" % image.shape[1])
	print("The number of channels: %d" % image.shape[2])

	print("\nThe values of the pixel at location (10,5): %s" % image[10][5])
	print("The value of the pixel at location (10,5) in the B(Blue) channel: %s" % image[10][5][0])
	print("The values of the pixels at location height=10:\n %s" % image[10])

	print("\nAll the pixel values in the B(Blue) channel:\n %s" % image[:,:,0])

	cv2.namedWindow("Image Show", cv2.WINDOW_NORMAL)

	print("\nDisplay image ...")
	print("Press any key inside the image to quit ...")
	cv2.imshow("Image Show", image)
	cv2.waitKey(0)


if __name__ == '__main__':
	main()
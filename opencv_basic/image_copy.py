#!/usr/bin/env python

import cv2
import numpy as np 

image_name = "tiger"

def main():

	print("Read an image ...")
	image = cv2.imread("./images/"+image_name+".jpg")

	print("Create a window to show the image ...")
	cv2.namedWindow("Image Show", cv2.WINDOW_NORMAL)

	print("Display image ...")
	cv2.imshow("Image Show", image)

	print("Press any key inside the image to make a copy ...")
	cv2.waitKey(0)

	print("Image is copied to folder images/copy/")
	cv2.imwrite("./images/copy/"+image_name+"_copy.jpg", image)


if __name__ == '__main__':
	main()
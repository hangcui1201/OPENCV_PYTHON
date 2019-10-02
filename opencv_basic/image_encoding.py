#!/usr/bin/env python

import cv2
import numpy as np 

image_name = "road"

def main():

	print("Read an image ...")
	image = cv2.imread("./images/"+image_name+".jpg", cv2.IMREAD_COLOR)
	height, width, channel = image.shape
	print("The shape of the image: %s" % str(image.shape))
	print("Split the image into three(BGR) channels.")
	blue, green, red = cv2.split(image)

	cv2.imshow("Original Image", image)
	#cv2.moveWindow("Original Image", 0, 0)

	print("Convert the image to grayscale.")
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	print("The shape of the gray image: %s" % str(gray_image.shape))
	cv2.imshow("Gray Image", gray_image)

	print("The content of a gray image.")
	print(gray_image)
	
	print("Display the image in Blue channel.")
	cv2.imshow("Blue Channel", blue)
	cv2.moveWindow("Blue Channel", 0, height)

	print("Display the image in Green channel.")
	cv2.imshow("Green Channel", green)
	cv2.moveWindow("Green Channel", 0, height)

	print("Display the image in Red channel.")
	cv2.imshow("Red Channel", red)
	cv2.moveWindow("Red Channel", 0, height)

	bgr_image_combine = np.concatenate((blue, green, red), axis=1)
	cv2.imshow("Blue, Green, Red Image", bgr_image_combine)
	cv2.moveWindow("Blue, Green, Red Image", 0, height)


	# Hue: indicate the type of color that we see in a 360 degree format
	# Saturation: indicate how saturated an individual color is
	# Value: indicate how luminous the channel is

	print("Split the image into Hue, Saturation and Value channels.")
	hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	h,s,v = cv2.split(hsv_image)
	
	# Show H, S, V channel in one window
	hsv_image_combine = np.concatenate((h,s,v), axis=1)
	cv2.imshow("Hue, Saturation, Value Image", hsv_image_combine)
	cv2.moveWindow("Hue, Saturation, Value Image", 0, height)


	print("Press any key inside the image to quit ...")
	cv2.waitKey(0)


if __name__ == '__main__':
	main()
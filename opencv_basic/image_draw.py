#!/usr/bin/env python

import cv2
import numpy as np 

# Construct an image with shape=(512,512,3) and pixel values all 0
image = np.zeros((512,512,3), np.uint8)


def main():

	# params: image, start_pixel, end_pixel, color, line_thickness
	cv2.line(image, (0,0), (511,511), (255,255,255), 5)

	# params: image, circle_center, radius, color, line_thickness
	# line_thickness=-1 will draw solid circle
	cv2.circle(image, (447,63), 63, (0,0,255), -1)

	# params: image, top_left_corner, bottom_right_corner, color, line_thickness
	cv2.rectangle(image, (384,0), (510,128), (0,255,0), 3)

	# params: image, ellipse_center, (major_axis_length/2, minor_axis_length/2), 
	#         angle(ellipse rotation angle in degrees)
	#         start_angle(starting angle of the elliptic arc in degrees)
	#         end_angle(ending angle of the elliptic arc in degrees)
	#         color(scalar), line_thickness
	cv2.ellipse(image, (image.shape[0]/2, image.shape[1]/2), (100,50), 0, 0, 180, 255, -1)


	pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
	print("Points before reshape.")
	print(pts)
	# Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices
	pts = pts.reshape((-1,1,2))
	print("\nPoints after reshape.")
	print(pts)
	cv2.polylines(image, [pts], True, (0,255,255))

	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(image, "OpenCV", (10,500), font, 2, (255,255,255), 2, cv2.LINE_AA)
	cv2.imshow("Image Panel", image)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
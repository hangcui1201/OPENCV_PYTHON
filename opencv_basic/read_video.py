#!/usr/bin/env python

import cv2
import numpy as np 

video_capture = cv2.VideoCapture(1)
#video_capture = cv2.VideoCapture('./video/video.mp4')


def main():

	while(True):

		ret, frame = video_capture.read()
		#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
		#cv2.line(frame, (0,0), (511,511), (255,0,0), 3)

		# Flip the frame upside down
		frame = cv2.flip(frame, 0)
		cv2.imshow("Frame", frame)

		if (cv2.waitKey(10) == 27):
			break # ESC to quit

	video_capture.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
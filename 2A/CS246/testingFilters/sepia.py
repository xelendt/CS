import numpy as np
import cv2
import cv2.cv as cv
import sys
import os
from matplotlib import pyplot as plt

filename  = raw_input( "Filename: " )
img = cv2.imread( filename, -1 )
#print img.shape
width, height, alpha = img.shape
out = np.zeros((width, height, 3), np.uint8)
#print out.shape



for x in range( 0, width- 1  ):
	print '''pixel row:[''', x,']'
	for y in range( 0, height - 1):
#		print img[x, y]
		out[x, y][2] = img[x, y][2]*0.393 + img[x, y][1]*0.769 + img[x, y][0]*0.189
		out[x, y][1] = img[x, y][2]*0.349 + img[x, y][1]*0.686 + img[x, y][0]*0.168
		out[x, y][0] = img[x, y][2]*0.272 + img[x, y][1]*0.534 + img[x, y][0]*0.131
		
cv2.imwrite( "sepia_"+filename, out)

os.system( 'open '+filename )
os.system( 'open sepia_'+filename )

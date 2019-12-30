import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    cv2.imwrite('frame.png', frame)

    im = cv2.imread('frame.png')
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)

    # Display the resulting frame
    cv2.imshow('Frame', output_image)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

# im = cv2.imread('utiles.png')
# bbox, label, conf = cv.detect_common_objects(im)
# output_image = draw_bbox(im, bbox, label, conf)

# cv2.imshow('frame', output_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

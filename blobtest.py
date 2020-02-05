# Standard imports
import cv2
import numpy as np
import keyboard
import time


###Connecting to IP camera

cameraIp = "192.168.1.10"
cameraUsername = "root"
cameraPass = "root"
thresholdValue = 100
showRawFlag = 1
cap = cv2.VideoCapture('rtsp://' + cameraUsername + ':' + cameraPass + '@' + cameraIp + '/axis-media/media.amp')
# cap = cv2.VideoCapture(0)
# params = cv2.SimpleBlobDetector_Params()
# params.filterByColor = 1
# params.blobColor = 255
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.2

# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500

# detector = cv2.SimpleBlobDetector_create(params)

while(True):
    if keyboard.is_pressed('h'):
        if thresholdValue > 255:
            thresholdValue = 255
        else:
            thresholdValue = thresholdValue + 5
        # print(thresholdValue)
    

    if keyboard.is_pressed('j'):
        if thresholdValue < 0:
            thresholdValue = 0
        else:
            thresholdValue = thresholdValue - 5
        # print(thresholdValue)

    ret, frame = cap.read()
    frame = cv2.resize(frame , (1280 , 720) ,  interpolation = cv2.INTER_AREA)
    grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(grayimg, thresholdValue, 255, cv2.THRESH_BINARY)
    # Set up the detector with default parameters.
    # Detect blobs.
    # keypoints = detector.detect(grayimg)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    # im_with_keypoints = cv2.drawKeypoints(grayimg, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Show keypoints
    # cv2.imshow("Keypoints", im_with_keypoints)

    if keyboard.is_pressed('o'):
        showRawFlag = not showRawFlag
        time.sleep(0.3);




    if showRawFlag == 1:
        cv2.imshow('frame' , grayimg)
    else:
        cv2.imshow('frame' , im_bw)

    if keyboard.is_pressed('r'):
        cv2.imshow('frame' , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
# cv2.destroyAllWindows()


##### Reading image and find circles etc


# Read image
# print("Reading Image")
# im = cv2.imread("BlobTest.jpg", cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
# params = cv2.SimpleBlobDetector_Params()
 
# # Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200
 
# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500
 
# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1
 
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87
 
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01
 
# # Create a detector with the parameters
# ver = (cv2.__version__).split('.')
# if int(ver[0]) < 3 :
#     detector = cv2.SimpleBlobDetector(params)
# else : 
#     detector = cv2.SimpleBlobDetector_create(params)

# print("Setting Detector")
# # detector = cv2.SimpleBlobDetector_create()
 
# # Detect blobs.
# print("Detect")
# keypoints = detector.detect(im)
# print(keypoints)

# for i in range(0 , len(keypoints)):
#     print(int(keypoints[i].pt[0]));
# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# print("Settings keypoints")
# im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # Show keypoints
# print("Came here")
# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(5000)
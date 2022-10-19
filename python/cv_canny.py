# import dependencies
import cv2
  
# create the video capture object (USB capture)
capture = cv2.VideoCapture(0)

# begin polling loop
while(True):

    # capture the video frame
    success, frame = capture.read()
    
    # check to see if we received a valid frame
    if success:
        # may want to do some grayscale or filters

        # apply the canny edge detector
        # old but fast, parallelizable and tunable
        # canny edge detector algo needs 2 tuning values
        # threshold to see whats light and dark(?)
        # <100 = dark
        # >200 = very light
        # how canny works - takes a sliding kernel (sample space) and move it
        # when it finds a big difference, it marks the center of that kernel as an edge
        # very common preprocessing step
        edges = cv2.Canny(frame, 100, 200)

        # any lines detected aren't actually defined as "lines" theyre just pixels
        # huff line detection - model lines - clusters of pixels that fit a y=mx+b type of line

        # Display the resulting frames
        cv2.imshow('frame', frame)
        cv2.imshow('edges', edges)

        # check for 'q' key press
        key = cv2.waitKey(1)
        print(key)
        if key == ord('q'):
            print("terminating program")
            break
    else:
        print("WARNING: unable to retrieve frame")
  
# shutdown the capture stream and display windows
capture.release()
cv2.destroyAllWindows()

# can load in trained models to opencv w their dnn module and use it in opencv

# cv boils down to:
# 1st half - performance, but some apps we dont care abt performance
# 2nd half - knowing whats in our library and the api-know how to search for them in docs
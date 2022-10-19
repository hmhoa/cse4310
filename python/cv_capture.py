# 10/19/2022

# 2 way to install - package, src code (can manually adjust optimizations)

# opencv up to version 5.x but all in opencv2

# OpenCV
#     - Supported in C++ and python
#     - De facto standard
#         ○ Usually learning opencv when learning cv

# Opencv python
#     - Opencv python pip install

# Github cse4310>python>cv_capture.py
#     - Line 5 does most of the nitty gritty work for us
#         ○ Can set brightness, etc.
#         ○ Grab data from usb camera, 
# - Can also support data from webstreams (rtsp) 

# import dependencies
import cv2
  
# create the video capture object (USB capture)
# connects to video device - can pull video, individual frame, from any usb as long as it supports os image acquuisition standard/driver level interface to talk to usb cam (linux - bf4l2)
# pass in 0 to videocapture object - enum at that addy
#   - integrated camera (unless disabled)
capture = cv2.VideoCapture(0)

# create the video capture object (RTSP stream)
# video clip ppl often use to test video stuff
# could easily be a security clip from your home and such
# can even go to websites for traffic cameras - alot of them have rtsp streams and can use them
# since traffic is a common cv use case, can just connect to the rtsp stream from somewhere
#capture = cv2.VideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4")

# begin polling loop
while(True):

    # capture the video frame
    # fill up frame buffer
    # up to 30 ms to come in - proc time, latency to grab frame, acquisition
    success, frame = capture.read()
    
    # frame will come through as a matrix - cv mat

    # check to see if we received a valid frame since we may not have any data left
    if success:

        # Display the resulting frame
        # can overwrite windows by giving same window name, but if you change names it'll make unique windows
        # tells opencv to add a particular window to render to its window drawing queue, but wont wont send to gpu to display until call cv waitkey
        cv2.imshow('frame', frame)

        # check for 'q' key press - check for n number of ms
        # in this case, wait 1 ms for key press detected
        # ascii code for that key will be in the key variable
        key = cv2.waitKey(1) # tells engine to draw the stuff
        print(key)
        if key == ord('q'):
            print("terminating program")
            break
    else:
        print("WARNING: unable to retrieve frame")
  
# shutdown the capture stream and display windows
# dont have to do this if program exits naturally-closes normally since destructors will call it
# but if it crashes while in use, but os may still mark camera in use-wait a bit til os lets it go or force close it
capture.release()
cv2.destroyAllWindows()
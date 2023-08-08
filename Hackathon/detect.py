import cv2
import numpy as np

def display_color_window(boolean_value):
    # Create a black window with a size of 200x200 pixels
    window = np.zeros((400, 400, 3), np.uint8)

    while True:
        if boolean_value:
            # Set the color of the window to green
            window[:] = (0, 255, 0)
        else:
            # Set the color of the window to red
            window[:] = (0, 0, 255)

        # Display the window and wait for 10 milliseconds
        cv2.imshow("Color Window", window)
        break




def detect_yellow(frame):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for yellow color detection in HSV
    lower_yellow = np.array([5, 100, 100])
    upper_yellow = np.array([25, 255, 255])

    # Threshold the HSV frame to get only yellow colors
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Count the number of non-zero pixels in the yellow mask
    yellow_pixel_count = cv2.countNonZero(yellow_mask)

    # If there are yellow pixels, return True; otherwise, return False
    if yellow_pixel_count > 0:
        return True
    else:
        return False

# Create a VideoCapture object to read from the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Flip the frame horizontally (optional)
    frame = cv2.flip(frame, 1)

    # Detect yellow objects in the frame
    yellow_detected = detect_yellow(frame)

    # Display the frame
    cv2.imshow('Yellow Detection', frame)

    display_color_window(yellow_detected)

    # Exit the loop if 'esc' is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()

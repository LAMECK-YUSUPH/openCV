import cv2
import numpy as np

# Open the video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or provide a video file path

# Create a background subtractor object
background_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Apply background subtraction
    mask = background_subtractor.apply(frame)

    # Find contours of the moving objects
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours and draw bounding boxes
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Adjust the minimum area threshold as needed
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with bounding boxes
    cv2.imshow("Moving Object Detection", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
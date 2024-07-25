import cv2
import numpy as np

# Open the video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or provide a video file path

# Create a flag to track if the user is drawing the perimeter
drawing_perimeter = False

# Create a list to store the coordinates of the perimeter points
perimeter_points = []

# Function to handle mouse events
def draw_perimeter(event, x, y, flags, param):
    global drawing_perimeter, perimeter_points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_perimeter = True
        perimeter_points.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing_perimeter = False

    elif event == cv2.EVENT_MOUSEMOVE and drawing_perimeter:
        perimeter_points.append((x, y))

# Create a window and set the mouse callback function
cv2.namedWindow('Draw Perimeter on Video')
cv2.setMouseCallback('Draw Perimeter on Video', draw_perimeter)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Draw the perimeter on the frame
    drawing = frame.copy()
    for i in range(len(perimeter_points) - 1):
        cv2.line(drawing, perimeter_points[i], perimeter_points[i + 1], (0, 255, 0), 2)

    # Display the frame with the perimeter
    cv2.imshow('Draw Perimeter on Video', drawing)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
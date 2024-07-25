import cv2
import numpy as np
import pygame

# Initialize Pygame mixer for sound effects
pygame.mixer.init()
##sound_effect = pygame.mixer.Sound('path\\to\\your\\sound_effect.wav')
sound_effect = pygame.mixer.Sound('C:\\Users\\yusup\\OneDrive\\Documents\\openCV\\ww.mp3')

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

# Function to detect objects within the perimeter
def detect_objects_in_perimeter(frame, perimeter_points):
    # Create a mask based on the perimeter
    mask = np.zeros_like(frame)
    cv2.fillPoly(mask, [np.array(perimeter_points, dtype=np.int32)], (255, 255, 255))

    # Apply the mask to the frame
    masked_frame = cv2.bitwise_and(frame, mask)

    # Perform object detection on the masked frame
    # You can use a pre-trained object detection model here, such as YOLO or Faster R-CNN
    # For this example, let's just detect any movement within the perimeter
    gray_frame = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_frame, 25, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Play the sound effect
        sound_effect.play()

    return masked_frame, len(contours) > 0

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

    # Detect objects within the perimeter
    masked_frame, object_detected = detect_objects_in_perimeter(frame, perimeter_points)

    # Display the frame with the perimeter and object detection
    cv2.imshow('Draw Perimeter on Video', drawing)
    cv2.imshow('Object Detection', masked_frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
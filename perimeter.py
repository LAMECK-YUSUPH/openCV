import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Create a copy of the original image
drawing = image.copy()

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
        cv2.line(drawing, perimeter_points[-2], perimeter_points[-1], (0, 255, 0), 2)
        cv2.imshow('Draw Perimeter', drawing)

# Create a window and set the mouse callback function
cv2.namedWindow('Draw Perimeter')
cv2.setMouseCallback('Draw Perimeter', draw_perimeter)

# Display the image and wait for user input
while True:
    cv2.imshow('Draw Perimeter', drawing)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if key == ord('s'):
        # Save the image with the perimeter
        cv2.imwrite('perimeter_image.jpg', drawing)
        print('Image saved as "perimeter_image.jpg"')

# Close all windows and release resources
cv2.destroyAllWindows()
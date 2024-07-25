import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the default camera
video_path = 'Awesome Animals.mp4'
cap = cv2.VideoCapture(video_path)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Create a window to display the video
cv2.namedWindow("Face Detection", cv2.WINDOW_NORMAL)

# Play the video and detect faces
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 1000, 0), 2)

        # Display the frame
        cv2.imshow("Face Detection", frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()


import cv2

# Replace 'IP_ADDRESS' with the IP address of your ESP32-CAM module
camera_url = 'http://192.168.0.104:81/stream'

# Create a VideoCapture object
cap = cv2.VideoCapture(camera_url)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Read and display the video frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Failed to receive frame from the camera")
        break

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()

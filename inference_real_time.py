from ultralytics import YOLO
import cv2

# Path to your YOLOv8 model
model_path = 'detect-s.pt'
model = YOLO(model_path)

# Virtual camera index (2)
camera_index = 2

# Open the virtual camera
cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

if not cap.isOpened():
    print(f"Could not connect to the virtual camera at index: {camera_index}")
    exit()

# Set model to use GPU if available
if model.device.type != 'cuda':
    model.to('cuda')

# Create fullscreen window
window_name = "Real-Time Detection (Virtual Camera)"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Get screen dimensions
screen_width = cv2.getWindowImageRect(window_name)[2]
screen_height = cv2.getWindowImageRect(window_name)[3]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Could not read frame (end of stream).")
        break

    # Perform detection with YOLOv8
    results = model(frame, conf=0.5, iou=0.4)

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Resize frame to fullscreen dimensions
    annotated_frame = cv2.resize(annotated_frame, (screen_width, screen_height))

    # Display the processed frame in fullscreen
    cv2.imshow(window_name, annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

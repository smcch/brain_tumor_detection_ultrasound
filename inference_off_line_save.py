from ultralytics import YOLO
import cv2

# Path to your YOLOv8 model
model_path = 'detect_s.pt'
model = YOLO(model_path)

# Path to the saved video
video_path = #your_ultrasound_video_file_here

# Path to save the processed video
output_video_path = #your_output_file_name_here

# Open the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Could not open the video at: {video_path}")
    exit()

# Get properties from the original video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Set up the VideoWriter object to save the processed video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Model configuration for GPU (if available)
if model.device.type != 'cuda':
    model.to('cuda')

# Process the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video.")
        break

    # Perform detection with YOLOv8
    results = model(frame, conf=0.5, iou=0.4)

    # Draw the detections on the frame
    annotated_frame = results[0].plot()

    # Write the processed frame to the output video
    out.write(annotated_frame)

    # Display the processed frame (optional, you can comment this part if you only want to save the video)
    cv2.imshow("Processing", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved at: {output_video_path}")

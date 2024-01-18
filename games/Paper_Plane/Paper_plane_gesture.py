import cv2
import numpy as np
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Set up Video Capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Plane coordinates
plane_x, plane_y = 320, 240
plane_speed = 10

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        # Get the landmarks of the first hand
        landmarks = results.multi_hand_landmarks[0].landmark

        # Get the coordinates of the tip of the index finger (Landmark 8)
        tip_x, tip_y = int(landmarks[8].x * frame.shape[1]), int(landmarks[8].y * frame.shape[0])

        # Move the plane based on hand gesture
        if tip_x > plane_x + plane_speed:
            plane_x += plane_speed
        elif tip_x < plane_x - plane_speed:
            plane_x -= plane_speed

        if tip_y > plane_y + plane_speed:
            plane_y += plane_speed
        elif tip_y < plane_y - plane_speed:
            plane_y -= plane_speed

        # Draw the paper plane on the frame
        cv2.putText(frame, "🛫", (plane_x, plane_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Paper Plane Game", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()

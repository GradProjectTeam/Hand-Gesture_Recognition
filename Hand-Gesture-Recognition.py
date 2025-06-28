import cv2
import time
import mediapipe as mp
from Draw_Hand_Landmarks import draw_hand_landmarks
from mediapipe.tasks.python.vision import GestureRecognizer, GestureRecognizerOptions, RunningMode
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode
from mediapipe.tasks.python.vision.gesture_recognizer import GestureRecognizerResult
from mediapipe.tasks.python.core.base_options import BaseOptions

# Global variables to store latest results
latest_hand_landmarks = None
latest_gesture_label = ""


def on_result(result: GestureRecognizerResult, output_image: any, timestamp_ms: int):
    """
    Callback function for processing gesture recognition results.
    """
    global latest_hand_landmarks, latest_gesture_label

    if result.gestures:
        gesture = result.gestures[0][0].category_name
        latest_gesture_label = gesture
        print(f"Detected gesture: {gesture}")

        # Map gestures to custom actions
        if gesture == "Open_Palm":
            print("📞 Simulating: Answer Call")
        elif gesture == "Thumb_Up":
            print("🔇 Simulating: Hang Up / Mute")
        elif gesture == "Victory":
            print("🎵 Simulating: Play Music")
        elif gesture == "Closed_Fist":
            print("✊ Simulating: Closed Fist Action")
        elif gesture == "Pointing_Up":
            print("☝️ Simulating: Pointing Up Action")
        elif gesture == "Thumb_Down":
            print("👎 Simulating: Thumbs Down Action")
        elif gesture == "ILoveYou":
            print("❤️ Simulating: Love Action")
        else:
            print("❓ Unrecognized gesture, label: Unknown")
    else:
        latest_gesture_label = ""  # No gesture detected

    # Store landmarks
    latest_hand_landmarks = result.hand_landmarks if result else None


# Set up gesture recognizer
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path="gesture_recognizer.task"),
    running_mode=VisionTaskRunningMode.LIVE_STREAM,
    result_callback=on_result,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
)

recognizer = GestureRecognizer.create_from_options(options)

# Start capturing from webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("❌ Cannot open webcam")

while True:
    success, frame = cap.read()
    if not success:
        continue

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    timestamp_ms = int(time.time() * 1000)

    # Convert to MediaPipe Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Perform gesture recognition
    recognizer.recognize_async(mp_image, timestamp_ms)

    # Draw landmarks if available
    if latest_hand_landmarks:
        frame = draw_hand_landmarks(frame, latest_hand_landmarks)

    # Draw gesture label
    if latest_gesture_label:
        cv2.putText(
            frame,
            f"Gesture: {latest_gesture_label}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

    # Display the frame
    cv2.imshow("Driver Gesture Recognition", frame)

    if cv2.waitKey(5) & 0xFF == 27:  # Escape key to exit
        break

cap.release()
cv2.destroyAllWindows()

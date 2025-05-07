import cv2
import time
import mediapipe as mp
from Draw_Hand_Landmarks import draw_hand_landmarks
from mediapipe.tasks.python.vision import GestureRecognizer, GestureRecognizerOptions, RunningMode
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode
from mediapipe.tasks.python.vision.gesture_recognizer import GestureRecognizerResult
from mediapipe.tasks.python.core.base_options import BaseOptions

# Global variable to store the latest hand landmarks
latest_hand_landmarks = None


def on_result(result: GestureRecognizerResult, output_image: any, timestamp_ms: int):
    """
    Callback function for processing gesture recognition results.
    """
    global latest_hand_landmarks

    if result.gestures:
        gesture = result.gestures[0][0].category_name
        print(f"Detected gesture: {gesture}")

        # Map gestures to custom actions
        if gesture == "Open_Palm":                     # 👋
            print("📞 Simulating: Answer Call")
        elif gesture == "Thumb_Up":                    # 👍
            print("🔇 Simulating: Hang Up / Mute")
        elif gesture == "Victory":                     # ✌️
            print("🎵 Simulating: Play Music")
        elif gesture == "Closed_Fist":                 # ✊
            print("✊ Simulating: Closed Fist Action")
        elif gesture == "Pointing_Up":                 # ☝️
            print("☝️ Simulating: Pointing Up Action")
        elif gesture == "Thumb_Down":                  # 👎
            print("👎 Simulating: Thumbs Down Action")
        elif gesture == "ILoveYou":                    # 🤟
            print("❤️ Simulating: Love Action")
        else:
            # Handle unrecognized gesture
            print("❓ Unrecognized gesture, label: Unknown")

    # Store the latest hand landmarks
    latest_hand_landmarks = result.hand_landmarks if result else None


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
# the Gesture Recognizer will invoke its result listener with the recognition result every time it has finished processing an input frame. 
# If the recognition function is called when the Gesture Recognizer task is busy processing another frame, the task will ignore the new input frame.


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("❌ Cannot open webcam")

while True:
    success, frame = cap.read()
    if not success:
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    timestamp_ms = int(time.time() * 1000)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    recognizer.recognize_async(mp_image, timestamp_ms)

    # Draw hand landmarks on the frame
    if latest_hand_landmarks:    
        frame = draw_hand_landmarks(frame, latest_hand_landmarks)

    cv2.imshow("Driver Gesture Recognition", frame)

    if cv2.waitKey(5) & 0xFF == 27:  # Escape key to break
        break

cap.release()
cv2.destroyAllWindows()
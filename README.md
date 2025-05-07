# 🚗 Driver Gesture Recognition with Hand Landmarks Visualization

This project is a real-time driver gesture recognition system built with [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer), OpenCV, and Python. It recognizes hand gestures through a webcam and visually overlays hand landmarks (skeleton) on the video feed, simulating specific driver actions.

## ✨ Features

- 🔍 Real-time hand gesture recognition using MediaPipe's Gesture Recognizer
- 🖐️ Hand landmark (skeleton) visualization for better feedback
- 🤖 Action simulation based on gestures (e.g., Answer Call, Play Music)
- 🖥️ Compatible with local PC 
- 🧪 Modular and extendable for more gestures or actions


## 📷 Recognized Gestures & Actions

| Gesture       | Simulated Action             |
|---------------|------------------------------|
| Open_Palm     | 📞 Answer Call               |
| Thumb_Up      | 🔇 Hang Up / Mute            |
| Victory       | 🎵 Play Music                |
                .
                .
                .
                
## Project Structure

    ├── Hand-Gesture-Recognition.py # Main gesture recognition script
    ├── Draw_Hand_Landmarks.py # Helper module for hand landmark drawing
    ├── gesture_recognizer.task # MediaPipe gesture model
    └── requirements.txt # Python dependencies


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abdoghazala7/Hand-Gesture-Recognition.git
   cd Hand-Gesture-Recognition
   
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Unix/macOS
   venv\Scripts\activate           # On Windows

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Download the model**
   Download the gesture_recognizer.task model from [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer) and place it in the root 
   folder.


## 📸 Sample Output

    The webcam feed displays live hand landmarks.
    logs gesture names and their corresponding simulated actions on the terminal.
    

## 📌 Notes

    Ensure good lighting and clear hand visibility for best results.
    Adjust gesture detection confidence thresholds if needed.
    Extend on_result() to integrate with real devices or APIs for automation.

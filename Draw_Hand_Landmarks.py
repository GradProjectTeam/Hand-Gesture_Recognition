import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2


# Initialize MediaPipe Hands and Drawing Utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles



def draw_hand_landmarks(frame, hand_landmarks):
    """
    Draws hand landmarks and connections on the input frame.
    
    Args:
        frame (numpy.ndarray): The input image/frame on which landmarks will be drawn.
        hand_landmarks (list): A list of hand landmarks detected by MediaPipe.
    """
    annotated_image = frame.copy()

    # Draw landmarks and connections for each hand
    for hand_landmark in hand_landmarks:
        # Convert hand_landmark to NormalizedLandmarkList format
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) 
            for landmark in hand_landmark
        ])

        # Draw landmarks and connections
        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmarks_proto,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        )

    return annotated_image
import cv2
import numpy as np
import mediapipe as mp
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import hypot
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import time


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


driver = webdriver.Chrome()  
driver.get("https://www.youtube.com/")
driver.maximize_window()

print("Log in and start a video. Waiting for 15 seconds...")
time.sleep(15)  


paused = False  
muted = False   


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    left_hand_detected = False
    right_hand_detected = False
    left_fist = False
    right_fist = False

    if result.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            handedness = hand_handedness.classification[0].label
            h, w, _ = frame.shape

            
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)

            finger_tips = [
                mp_hands.HandLandmark.INDEX_FINGER_TIP,
                mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                mp_hands.HandLandmark.RING_FINGER_TIP,
                mp_hands.HandLandmark.PINKY_TIP,
            ]
            finger_bases = [
                mp_hands.HandLandmark.INDEX_FINGER_MCP,
                mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                mp_hands.HandLandmark.RING_FINGER_MCP,
                mp_hands.HandLandmark.PINKY_MCP,
            ]

            closed_fist = all(
                hand_landmarks.landmark[tip].y > hand_landmarks.landmark[base].y
                for tip, base in zip(finger_tips, finger_bases)
            )

          
            if handedness == "Left":
                left_hand_detected = True
                left_fist = closed_fist

            
            if handedness == "Right":
                right_hand_detected = True
                right_fist = closed_fist

        
        if left_hand_detected and right_hand_detected:
            if left_fist and right_fist:
                if not muted:
                    driver.execute_script("document.querySelector('video').muted = true")
                    muted = True
                    cv2.putText(frame, "Muted", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            elif not left_fist and not right_fist:
                if muted:
                    driver.execute_script("document.querySelector('video').muted = false")
                    muted = False
                    cv2.putText(frame, "Unmuted", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        
        elif left_hand_detected or right_hand_detected:
            if left_hand_detected:
                
                if not left_fist:
                    distance = hypot(index_x - thumb_x, index_y - thumb_y)
                    volume_level = np.clip(distance / 200, 0.0, 1.0)
                    volume.SetMasterVolumeLevelScalar(volume_level, None)
                    cv2.putText(frame, f"Volume: {int(volume_level * 100)}%", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if right_hand_detected:
                
                if right_fist:
                    driver.execute_script("document.querySelector('video').pause()")
                    paused = True
                    cv2.putText(frame, "Paused", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    driver.execute_script("document.querySelector('video').play()")
                    paused = False
                    cv2.putText(frame, "Playing", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

   
    cv2.imshow("YouTube Gesture Control", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
driver.quit() 
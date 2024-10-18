import cv2
import mediapipe as mp
from math import hypot
import numpy as np
import os

cap = cv2.VideoCapture(0)  # Checks the camera

mpHands = mp.solutions.hands  # Detects hand/fingers
hands = mpHands.Hands()  # Initializes the complete configuration for hands
mpDraw = mp.solutions.drawing_utils

# Function to set the system volume on macOS
def set_volume_mac(volume_percent):
    # Volume percentage is expected between 0 and 100
    volume_level = volume_percent / 100  # Converts to a value between 0 and 1
    os.system(f"osascript -e 'set volume output volume {int(volume_level * 100)}'")

while True:
    success, img = cap.read()  # If the camera works, captures an image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converts to RGB

    # Collects gesture information
    results = hands.process(imgRGB)  # Processes the image

    lmList = []  # Empty list
    if results.multi_hand_landmarks:  # List of all detected hands
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):  # Adds a counter
                # Get finger joint points
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])  # Adds to the 'lmList'
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

    if lmList != []:
        # Gets the value at a point
        x1, y1 = lmList[4][1], lmList[4][2]  # Thumb
        x2, y2 = lmList[8][1], lmList[8][2]  # Index finger
        # Creates a circle at the tips of the thumb and index finger
        cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)  # Image, fingers, radius, RGB
        cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)  # Image, fingers, radius, RGB
        # Creates a line between the tips of the thumb and index finger
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)  # Creates a line between finger tips

        length = hypot(x2 - x1, y2 - y1)  # Distance between tips using hypotenuse
        # Hand range 30 - 350; volume range 0 - 100 (percentage)
        volper = np.interp(length, [30, 350], [0, 100])

        print(f"Volume percent: {int(volper)}")
        set_volume_mac(volper)  # Sets system volume based on finger distance
            
        # Creates a volume bar for the volume level 
        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 4)  # Video, start position, end position, RGB, thickness
        volbar = np.interp(length, [30, 350], [400, 150])
        cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 0, 255), cv2.FILLED)  # Filled rectangle
        cv2.putText(img, f"{int(volper)}%", (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
        # Displays volume percentage, location, font, size, RGB color, thickness

    cv2.imshow('Image', img)  # Displays the video
    if cv2.waitKey(1) & 0xff == ord(' '):  # Using the spacebar, the delay will stop
        break

cap.release()  # Stops the camera
cv2.destroyAllWindows()  # Closes the window

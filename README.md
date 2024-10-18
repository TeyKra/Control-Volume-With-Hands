# Control-Volume-With-Hands

## Overview

This project allows you to control your macOS system volume using hand gestures detected through your webcam. By measuring the distance between your thumb and index finger, the program adjusts the system volume in real-time. It provides visual feedback by displaying the webcam feed with annotations indicating finger positions, the distance between them, and a volume bar.

## Features

- **Real-time Hand Detection**: Utilizes Mediapipe to detect and track hand landmarks.
- **Gesture-based Volume Control**: Adjusts system volume based on the distance between thumb and index finger.
- **Visual Interface**: Displays finger joints, a line indicating distance, and a volume bar.
- **Platform Support**: Currently supports macOS for volume control.

## Prerequisites

- **Python 3.x**
- **Operating System**: macOS
- **Webcam**: Built-in or external

## Dependencies

Install the following Python packages:

- `opencv-python`
- `mediapipe`
- `numpy`

You can install them using pip:

```bash
pip install opencv-python mediapipe numpy
```

## How It Works

1. **Hand Detection**: The program uses Mediapipe's hand detection module to identify hand landmarks from the webcam feed.
2. **Distance Calculation**: Calculates the Euclidean distance between the tips of the thumb and index finger.
3. **Volume Mapping**: Maps the calculated distance to a volume percentage (0% to 100%).
4. **System Volume Adjustment**: Uses AppleScript commands executed via `os.system` to set the macOS system volume.
5. **Visual Feedback**: Displays the webcam feed with annotations:
   - **Red Circles**: Mark the tips of the thumb and index finger.
   - **Green Line**: Shows the distance between the two fingertips.
   - **Blue Volume Bar**: Indicates the current volume level on the side of the window.

## Usage

1. **Run the Script**:

   ```bash
   python your_script_name.py
   ```

2. **Control Volume**:

   - Move your thumb and index finger closer to decrease the volume.
   - Move them apart to increase the volume.

3. **Exit**:

   - Press the **spacebar** to stop the program and close the window.

## Code Explanation

- **Imports**: The script imports necessary libraries for computer vision (`cv2`), hand tracking (`mediapipe`), mathematical calculations (`math`, `numpy`), and system operations (`os`).
- **Camera Initialization**: Captures video from the default webcam.
- **Hand Tracking Setup**: Initializes Mediapipe's hand detection module.
- **Volume Control Function**: Defines `set_volume_mac()` to adjust system volume using AppleScript commands.
- **Main Loop**:
  - Reads frames from the webcam.
  - Converts frames to RGB for Mediapipe processing.
  - Detects hand landmarks and stores them.
  - Calculates the distance between thumb and index fingertips.
  - Maps this distance to a volume percentage.
  - Adjusts the system volume accordingly.
  - Displays annotations on the video feed.
- **Exit Condition**: The loop breaks when the spacebar is pressed.

## Customization

- **Adjust Sensitivity**: Modify the range `[30, 350]` in the `np.interp()` functions to calibrate the sensitivity of the gesture recognition.
- **Change Colors**:
  - **Volume Bar**: Change the BGR color `(255, 0, 0)` in `cv2.rectangle()` for the volume bar.
  - **Finger Circles**: Adjust the BGR color `(0, 0, 255)` in `cv2.circle()` for fingertip markers.
  - **Distance Line**: Modify the BGR color `(0, 255, 0)` in `cv2.line()` for the line between fingertips.
- **Platform Support**: Replace the `set_volume_mac()` function with an equivalent function for Windows or Linux if needed.

## Acknowledgements

- **Mediapipe**: For providing efficient hand detection and tracking.
- **OpenCV**: For powerful real-time computer vision capabilities.
- **Community**: Inspired by various open-source projects combining gesture recognition and system control.

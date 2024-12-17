# GestureTube: Gesture-Controlled YouTube Player

## Project Overview
GestureTube is an innovative project that enables users to control YouTube playback using hand gestures detected through their webcam. By leveraging advanced computer vision technologies, the project provides a seamless, hands-free experience for pausing, playing, muting, and adjusting the volume of YouTube videos. The implementation is built with OpenCV, MediaPipe, Selenium, and Pycaw.

---

## Project Details

### Features
- **Mute/Unmute**: Close both fists to mute or unmute the video.
- **Pause/Play**: Close your right fist to pause and open it to play.
- **Volume Control**: Adjust the distance between your thumb and index finger on your left hand to control the volume.

### Technologies Used
- **OpenCV**: For capturing and processing video input.
- **MediaPipe**: For hand landmark detection and gesture recognition.
- **Selenium**: For controlling YouTube playback through browser automation.
- **Pycaw**: For system-level volume control.

---

## Project Structure
The project is organized as follows:

```
GestureTube/
├── src/                # Source code
│   └── main.py         # Main script for gesture detection and playback control
│
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── LICENSE             # License file
└── .gitignore          # Ignore unnecessary files
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/username/GestureTube.git
cd GestureTube
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure ChromeDriver
- Download and install [ChromeDriver](https://chromedriver.chromium.org/).
- Ensure ChromeDriver is added to your PATH.

---

## Usage Guide

### Running the Program
1. Start the script:
   ```bash
   python src/main.py
   ```

2. Log in to YouTube and start a video. The program waits for 15 seconds to allow for setup.

3. Use the following gestures to control playback:
   - **Mute/Unmute**: Close both fists.
   - **Pause/Play**: Close your right fist to pause and open it to play.
   - **Volume Control**: Adjust the distance between your thumb and index finger on your left hand.

4. Press `q` to exit the program.

---

## Example Usage

### Mute/Unmute
- Close both fists to toggle the mute state of the video.

### Volume Adjustment
- Move your left thumb and index finger closer or farther apart to lower or raise the volume.

### Pause/Play
- Close your right fist to pause the video. Open your fist to resume playback.

---

## Contributing
Contributions are welcome! To contribute:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Submit a pull request for review.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
If you have any questions, suggestions, or feedback, feel free to contact me at [sauravsamal9@gmail.com].


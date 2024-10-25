# Real-time Posture Corrector

A computer vision-based application that helps maintain good posture by monitoring shoulder and neck alignment in real-time using your webcam.

## Features

- Real-time posture detection and monitoring
- Visual feedback with angle measurements
- Calibration system for personalized posture thresholds
- Audio alerts for poor posture
- Color-coded status indicators
- Detailed angle measurements and visualization

## Demo

### Calibration Process
![Image Alt](https://github.com/MeghanshGovil/Posture-Detection-Tool/blob/1973443b1c2780f0b989e0573614b9376f40c8a7/Calibration.png)
The system calibrates to your natural posture in the first 30 frames.

### Good Posture Detection
![Image Alt](https://github.com/MeghanshGovil/Posture-Detection-Tool/blob/1973443b1c2780f0b989e0573614b9376f40c8a7/Good%20Posture.png)
Green indicators show when posture is maintained within acceptable ranges.

### Poor Posture Detection
![Image Alt](https://github.com/MeghanshGovil/Posture-Detection-Tool/blob/1973443b1c2780f0b989e0573614b9376f40c8a7/Bad%20Posture.png)
Red indicators and specific feedback when posture correction is needed.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/posture-corrector.git
cd posture-corrector
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Required Dependencies

```plaintext
opencv-python>=4.7.0
mediapipe>=0.9.0
numpy>=1.22.0
playsound>=1.3.0
```

## Usage

1. Run the main application:
```bash
python main.py
```

2. Position yourself in front of the camera with good posture.

3. Stay still during the 30-frame calibration period.

4. The system will start monitoring your posture and provide real-time feedback.

### Controls
- Press 'q' to quit the application
- The system will automatically alert you when poor posture is detected
- Visual indicators show current posture status and measurements

## How It Works

1. **Pose Detection**
   - Uses MediaPipe Pose to detect body landmarks
   - Tracks key points including shoulders and ears

2. **Angle Calculation**
   - Measures angles between ears, shoulders, and vertical reference
   - Compares measurements against calibrated thresholds

3. **Feedback System**
   - Visual feedback with color-coded indicators
   - Audio alerts for sustained poor posture
   - Real-time angle measurements display

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MediaPipe for the pose detection system
- OpenCV for image processing capabilities
- Contributors and maintainers of all dependencies

## Future Improvements

-  Add data logging capabilities
-  Implement posture history tracking
-  Add customizable alert sounds
-  Create a GUI for settings adjustment
-  Add support for multiple camera inputs
-  Implement profile saving/loading

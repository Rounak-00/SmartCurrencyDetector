# Currency Recognition System

## Overview
This project is a currency recognition system built using Django for the backend and a combination of HTML, CSS, and JavaScript for the frontend. The system utilizes deep learning models trained using transfer learning and fine-tuning on VGG16, VGG19, ResNet50, and EfficientNet. The trained models are used to classify Indian currency notes and provide audio feedback for visually impaired users.

## Features
- **Live Camera Capture**: Users can capture an image using their webcam.
- **Image Upload**: Users can upload an image for currency recognition.
- **Currency Detection**: The system processes the image and identifies the currency.
- **Audio Feedback**: A detected currency note's value is converted to audio output.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Transfer Learning & Fine-tuning (VGG16, VGG19, ResNet50, EfficientNet)
- **API Communication**: JavaScript (POST request to Django backend)

## Directory Structure
```
CurrencyRecognizer/
│── currency_app/
│   ├── models/
│   ├── ModelTraining.ipynb
│   ├── CheckCurrency.py
│   ├── TextToAudio.py
│
│── static/
│   ├── css/
│   │   ├── style.css
│   ├── js/
│   │   ├── script.js
│
│── templates/
│   ├── camera.html
```

## Model Training
The dataset used for training was downloaded from Kaggle:
```
kaggle datasets download -d vishalmane109/indian-currency-note-images-dataset-2020
```
The models were trained on Kaggle using transfer learning and fine-tuning techniques. The final trained models were saved in `.keras` format under the `models/` directory.

## How It Works
1. **Frontend Interaction**: The user either captures an image using their webcam or uploads an image.
2. **API Request**: The image is sent to the Django backend via a POST request.
3. **Currency Detection**: The backend processes the image using `CheckCurrency.py`.
4. **Audio Feedback**: `TextToAudio.py` converts the detected currency note's value into an audio response.
5. **Response to Frontend**: The result is displayed, and the corresponding audio is played.

## API Details
- **Endpoint**: `POST /upload_image/`
- **Handled in**: `urls.py -> upload_image in views.py`
- **Request Body**: FormData containing the uploaded image
- **Response**: JSON with detected currency and an audio response

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/Rounak-00/SmartCurrencyDetector.git
   cd SmartCurrencyDetector
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Django server:
   ```sh
   python manage.py runserver
   ```
4. Open the application in your browser: `http://127.0.0.1:8000/`

## Future Enhancements
- Improve accuracy with additional training data.
- Deploy the system for real-time mobile application use.
- Implement support for multiple currencies.

## Author
**Rounak** 🚀


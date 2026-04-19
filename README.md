# 🚗 Driver Drowsiness Detection

## 📌 Project Overview

Driver drowsiness is one of the major causes of road accidents. This project implements a computer vision–based solution to detect driver drowsiness in real-time using a webcam feed. The model is trained on a Kaggle dataset of open and closed eyes, and then deployed to continuously monitor eye states to raise alerts when drowsiness is detected.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** OpenCV, scikit-learn, NumPy, Joblib
* **Environment:** VS Code
* **Dataset:** Kaggle (Open/Closed eyes dataset) - download from Kaggle

---

## 📂 Project Structure

Driver-Drowsiness-Detection/
│
├── src/                     # Source code
│   ├── model_training.py    # Script for training the ML model
│   └── model_work.py        # Script for running webcam & prediction
├── venv/                    # Virtual environment (ignored in GitHub)
├── ddd.pkl                  # Saved trained model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

---

## ⚙️ Setup Instructions

1. Clone the repository:

   (bash)
   git clone https://github.com/USERNAME/Driver-Drowsiness-Detection.git
   cd Driver-Drowsiness-Detection

2. Create and activate a virtual environment:

   (bash)
   python -m venv venv
   venv\Scripts\activate   # For Windows
   source venv/bin/activate   # For Linux/Mac

3. Install dependencies:

   (bash)
   pip install -r requirements.txt

4. Train the model (optional if model is already saved):

   (bash)
   python src/model_training.py

5. Run the webcam detection:

   (bash)
   python src/model_work.py

---

## 🎯 Features

* Detects driver drowsiness in real-time via webcam.
* Machine Learning model trained on eye states (open/closed).
* Alerts when driver shows signs of sleepiness.
* Modular code: separate training and prediction scripts.

---

## 📊 Results

* Model used: **KNN Classifier**
* Accuracy on test data: **99.97%**

---

## 🚀 Future Improvements

* Add sound/vibration alerts.
* Deploy on Raspberry Pi for real car testing.
* Improve model accuracy with CNNs.

---

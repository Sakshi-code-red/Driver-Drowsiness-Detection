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
├── model_train.py    # Script for training the ML model  
├── trained.py        # Script for running webcam & prediction    
├── ddd.pkl           # Saved trained model  
└── README.md         # Project documentation  

---

## ⚙️ Setup Instructions

1. Clone the repository:

   (bash)
   git clone https://github.com/Sakshi-code-red/Driver-Drowsiness-Detection.git
   cd Driver-Drowsiness-Detection

2. Install dependencies:

   (bash)
   pip install -r requirements.txt

3. Train the model (optional if model is already saved):

   (bash)
   python model_train.py

4. Run the webcam detection:

   (bash)
   python trainde.py

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

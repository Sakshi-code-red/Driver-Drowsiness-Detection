import joblib as jb
import cv2
import signal
import sys

# Load model
model = jb.load('ddd.pkl')
print('model loaded')

# Load Haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Start webcam (faster init)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

closed_eyes_frame_count = 0
drowsy_threshold = 5


# 🔥 HANDLE FORCE STOP PROPERLY
def signal_handler(sig, frame):
    print("Stopping camera...")
    cap.release()
    cv2.destroyAllWindows()
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes_detected = False

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 1:
            eyes_detected = True
            break

    if eyes_detected:
        closed_eyes_frame_count = 0
        text = "Eyes Open"
        color = (0, 255, 0)
    else:
        closed_eyes_frame_count += 1
        text = "Eyes Closed"
        color = (0, 0, 255)

    if closed_eyes_frame_count > drowsy_threshold:
        text = "DROWSINESS ALERT!"

    cv2.putText(frame, text, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands  # Formality
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0  # Previous time
cTime = 0  # Current time

while True:
    success, img = cap.read()
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    print(results.multi_hand_landmarks)

    # if results.multi_hand_landmarks:
    #     for handLms in results.multi_hand_landmark:
    #         mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3,
                (255, 0, 255), 3)

    cv2.imshow("Mediapipe Hands", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()

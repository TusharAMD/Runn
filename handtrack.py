import cv2
import mediapipe as mp
import math
import pynput

from pynput.keyboard import Key, Controller
keyboard = Controller()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
drawingspec=mp.solutions.drawing_utils.DrawingSpec

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        for ids,lm in enumerate(hand_landmarks.landmark):

            if ids==0:
                point_o_x=lm.x
                point_o_y=lm.y
                #print(lm.x,lm.y,0)
                
            if ids==8:
                #print(lm.x,lm.y,8)
                point_8_x=lm.x
                point_8_y=lm.y
                leftside=math.sqrt(abs((point_o_x-point_8_x)*(point_o_x-point_8_x)+(point_o_y-point_8_y)*(point_o_y-point_8_y)))
                print(leftside,"leftside")
                #print(point_o_x-point_8_x,point_o_y-point_8_y)
            if ids==12:
                #print(lm.x,lm.y,8)
                point_12_x=lm.x
                point_12_y=lm.y
                middleside=math.sqrt(abs((point_o_x-point_12_x)*(point_o_x-point_12_x)+(point_o_y-point_12_y)*(point_o_y-point_12_y)))
                print(middleside,"middleside")
                #print(point_o_x-point_8_x,point_o_y-point_8_y)
            if ids==20:
                #print(lm.x,lm.y,8)
                point_20_x=lm.x
                point_20_y=lm.y
                rightside=math.sqrt(abs((point_o_x-point_20_x)*(point_o_x-point_20_x)+(point_o_y-point_20_y)*(point_o_y-point_20_y)))
                print(rightside,"rightside")
                #print(point_o_x-point_8_x,point_o_y-point_8_y)
            try:
                if middleside>0.40:
                    print("MIDDLE")
                    for i in range(0,10):
                        pass
                        keyboard.press(Key.up)
                        keyboard.release(Key.up)
                elif leftside>0.40:
                    print("LEFT")
                    for i in range(0,10):
                        keyboard.press(Key.left)
                        keyboard.release(Key.left)
                
                elif rightside>0.40:
                    print("RIGHT")
                    for i in range(0,10):
                        keyboard.press(Key.right)
                        keyboard.release(Key.right)
                    
            except Exception as e:
                print(e)
             
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS,drawingspec(color=(0,215,255),circle_radius=5),drawingspec(color=(0,215,255),thickness=6))
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

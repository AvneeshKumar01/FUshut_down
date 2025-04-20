import cv2
import os
import mediapipe as mp
import numpy  as np

def shut_down_computer():
	if os.name == 'nt':
		os.system('shutdown /s /t 0')
	elif os.name == 'posix':
		os.system('poweroff')
	else :
		print("os not supported")

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1 , min_detection_confidence=0.5 , min_tracking_confidence=0.7) as hands:
	while True:
		suc , img = cap.read()
		img = cv2.flip(img , 1)
		img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
		results = hands.process(img)

		img = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
		if results.multi_hand_landmarks:
			for hand_position in results.multi_hand_landmarks:
				mp_drawing.draw_landmarks(img , hand_position , mp_hands.HAND_CONNECTIONS)

				landmarks = np.array([(lm.x , lm.y , lm.z) for lm in hand_position.landmark])

				middle_tip = landmarks[12]
				middle_pip =  landmarks[10]

				index_tip = landmarks[8]
				index_pip = landmarks[6]

				ring_tip = landmarks[16]
				ring_pip = landmarks[14]

				pinky_tip = landmarks[20]
				pinky_pip = landmarks[18]

				middle_extended = middle_pip[1] >  middle_tip[1]
				index_folded = index_pip[1] <  index_tip[1]
				ring_folded = ring_pip[1] <  ring_tip[1]
				pinky_folded = pinky_pip[1] <  pinky_tip[1]

				if middle_extended and index_folded and ring_folded and pinky_folded:
					shut_down_computer()
				#	print("shutdown") wrote it here for testing , wont remove cuz im cool like that 
		cv2.imshow("webcam" , img)

		if  cv2.waitKey(1) & 0XFF == ord('q'):
			break

cap.release()

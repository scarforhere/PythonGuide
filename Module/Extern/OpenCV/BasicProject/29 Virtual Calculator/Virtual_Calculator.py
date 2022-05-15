# coding: utf-8
"""
-------------------------------------------------
   File Name:      code
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    Virtual Calculator

"""
import cv2
from cvzone.HandTrackingModule import HandDetector
 
 
class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value
 
    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 15, self.pos[1] + 35), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)
 
    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 5, self.pos[1] + 45), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 3)
            return True

        else:
            return False
 
 
# Buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 50 + 100
        ypos = y * 50 + 120
 
        buttonList.append(Button((xpos, ypos), 50, 50, buttonListValues[y][x]))
 
# Variables
myEquation = ''
delayCounter = 0
# Webcam
cap = cv2.VideoCapture('http://192.168.178.48:4747/video')
detector = HandDetector(detectionCon=0.8, maxHands=1)
 
while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

    hands, img = detector.findHands(img)
 
    # Draw All
    cv2.rectangle(img, (100, 70), (100 + 200, 70 + 50), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (100, 70), (100 + 200, 70 + 50), (50, 50, 50), 3)

    for button in buttonList:
        button.draw(img)

    # Check for Hand
    if hands:
        # Find distance between fingers
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8], lmList[12], img)
        # print(length)
        x, y = lmList[8]

        # If clicked check which button and perform action
        if length < 50 and delayCounter == 0:
            for i, button in enumerate(buttonList):
                if button.checkClick(x, y):
                    myValue = buttonListValues[int(i % 4)][int(i / 4)]  # get correct number
                    if myValue == '=':
                        try:
                            myEquation = str(eval(myEquation))
                        except SyntaxError:
                            myEquation = "SyntaxError"
                    else:
                        myEquation += myValue
                    delayCounter = 1

    # to avoid multiple clicks
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Write the Final answer
    cv2.putText(img, myEquation, (110, 105), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)

    # Display
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    cv2.imshow("Image", img)
    if key == ord('c'):
        myEquation = ''

cap.release()
cv2.destroyAllWindows()

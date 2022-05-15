from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject()

while True:
    # In Arduino always receive a list
    arduino.sendData([1])
    sleep(3)
    arduino.sendData([0])
    sleep(1)

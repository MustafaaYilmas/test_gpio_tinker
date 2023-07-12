#Testing for software PWM
import RPi.GPIO as GPIO
import unittest   
import time   

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
redPwm = GPIO.PWM(8, 50)
greenPwm = GPIO.PWM(10, 50)
bluePwm = GPIO.PWM(12, 50)
pwm.start(100)
redPwm.ChangeDutyCycle(100)
greenPwm.ChangeDutyCycle(100)
bluePwm.ChangeDutyCycle(100)

while True:
    
	for i in range(0,3):
        redPwm.ChangeDutyCycle(0)
        time.sleep(5)
        redPwm.ChangeDutyCycle(100)
        time.sleep(5)
        greenPwm.ChangeDutyCycle(0)
        time.sleep(5)
        greenPwm.ChangeDutyCycle(100)
        time.sleep(5)
        bluePwm.ChangeDutyCycle(0)
        time.sleep(5)
        bluePwm.ChangeDutyCycle(100)
        time.sleep(5)
        

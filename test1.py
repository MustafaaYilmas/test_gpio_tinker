import RPi.GPIO as GPIO
import time

RED_LED_PIN = 8
GREEN_LED_PIN = 10
BLUE_LED_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

leds = [RED_LED_PIN, GREEN_LED_PIN, BLUE_LED_PIN]

try:
    for led in leds:
        pwm = GPIO.PWM(led, 50)
        pwm.start(0)
        for i in range(3):
            for brightness in range(0, 101, 5):
                pwm.ChangeDutyCycle(brightness)
                time.sleep(0.1)
            for brightness in range(100, -1, -5):
                pwm.ChangeDutyCycle(brightness)
                time.sleep(0.1)
        pwm.stop()

finally:
    GPIO.cleanup()

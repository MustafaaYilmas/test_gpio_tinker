import RPi.GPIO as GPIO
import time

BLUE_LED_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

try:
    pwm_blue = GPIO.PWM(BLUE_LED_PIN, 50)
    pwm_blue.start(0)
    for i in range(3):
        for brightness in range(0, 101, 5):
            pwm_blue.ChangeDutyCycle(brightness)
            time.sleep(0.1)
        for brightness in range(100, -1, -5):
            pwm_blue.ChangeDutyCycle(brightness)
            time.sleep(0.1)
    pwm_blue.stop()

finally:
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

RED_LED_PIN = 8
GREEN_LED_PIN = 10
BLUE_LED_PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

pwm_red = GPIO.PWM(RED_LED_PIN, 50)
pwm_green = GPIO.PWM(GREEN_LED_PIN, 50)
pwm_blue = GPIO.PWM(BLUE_LED_PIN, 50)

try:
    for pwm in [pwm_red, pwm_green, pwm_blue]:
        pwm.start(0)
        for i in range(3):
            for brightness in range(0, 101, 5):
                pwm.ChangeDutyCycle(brightness)
                time.sleep(0.1)
            for brightness in range(100, -1, -5):
                pwm.ChangeDutyCycle(brightness)
                time.sleep(0.1)
        pwm.ChangeDutyCycle(0)  # Make sure the LED is turned off before moving to the next one
finally:
    pwm_red.stop()
    pwm_green.stop()
    pwm_blue.stop()
    GPIO.cleanup()

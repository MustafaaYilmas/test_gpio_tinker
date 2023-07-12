import RPi.GPIO as GPIO
import time

# Pin numaralarını tanımlayın
RED_LED_PIN = 8
GREEN_LED_PIN = 10
BLUE_LED_PIN = 12

# BOARD pin numaralandırma düzenini kullanın
GPIO.setmode(GPIO.BOARD)

# Pinleri çıkış olarak ayarlayın
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

# Her pin için bir PWM nesnesi oluşturun
pwm_red = GPIO.PWM(RED_LED_PIN, 50)
pwm_green = GPIO.PWM(GREEN_LED_PIN, 50)
pwm_blue = GPIO.PWM(BLUE_LED_PIN, 50)

try:
    # Her LED için bir döngü başlatın
    for pwm in [pwm_red, pwm_green, pwm_blue]:
        pwm.start(0)  # LED'i kapatın
        for i in range(3):  # 3 kez parlaklaştırma/sönme döngüsü yapın
            # LED'i kademeli olarak parlaklaştırın
            for brightness in range(0, 101, 5):
                pwm.ChangeDutyCycle(brightness)
                time.sleep(0.1)
            # LED'i kademeli olarak karartın
            for brightness in range(100, -1, -5):
                pwm.ChangeDutyCycle(brightness)
                time.sleep(0.1)
        pwm.stop()  # PWM'i durdurun
finally:
    GPIO.cleanup()  # GPIO pinlerini temizleyin

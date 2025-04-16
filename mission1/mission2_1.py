from gpiozero import LED
from time import sleep

# LED 핀 설정
led = LED(8)

# LED 깜박이기
while True:
    led.on()  # LED 켜기
    sleep(1)  # 1초 대기
    led.off()  # LED 끄기
    sleep(1)  # 1초 대기
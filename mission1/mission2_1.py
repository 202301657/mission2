from gpiozero import LED, Button
from time import sleep

# 스위치와 LED 핀 설정
SWPIN = 25
GPIO_PINS = [8, 7, 16, 20]

# LED 객체 생성
leds = [LED(pin) for pin in GPIO_PINS]

# 스위치 객체 생성 (풀업 설정)
switch = Button(SWPIN, pull_up=True)

# 스위치 상태에 따라 LED 제어
while True:
    print(switch.is_pressed)
    if switch.is_pressed:  # 스위치가 눌렸을 때
        for led in leds:
            led.on()  # LED 켜기
    else:
        for led in leds:
            led.off()  # LED 끄기

    sleep(0.1)  # 100ms 대기
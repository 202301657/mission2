from gpiozero import LED, Button
from time import sleep

# 스위치와 LED 핀 설정
SWPIN = 25
GPIO_PINS = [8, 7, 16, 20]

# LED 객체 생성
leds = [LED(pin) for pin in GPIO_PINS]

# 스위치 객체 생성 (풀업 설정)
switch = Button(SWPIN, pull_up=True)

# 카운터 초기화
cnt = 0

while True:
    # 모든 LED 끄기
    for led in leds:
        led.off()

    if switch.is_pressed:  # 스위치가 눌렸을 때 카운터 증가
        cnt += 1
        sleep(0.2)  # 디바운싱을 위한 짧은 대기

    # 카운터 값을 이진수로 해석하여 각 LED를 순차적으로 켜기
    if (cnt // 1) % 2:
        leds[0].on()
    if (cnt // 2) % 2:
        leds[1].on()
    if (cnt // 4) % 2:
        leds[2].on()
    if (cnt // 8) % 2:
        leds[3].on()

    sleep(0.1)  # 반복 대기

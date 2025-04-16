from gpiozero import LED, Button
from time import sleep

# 스위치와 LED 핀 설정
SWPIN = 25
GPIO_PINS = [8, 7, 16, 20]

# LED 객체 생성
leds = [LED(pin) for pin in GPIO_PINS]

# 스위치 객체 생성 (풀업 설정)
switch = Button(SWPIN, pull_up=True)

# 변수 초기화
n = 0

while True:
    if switch.is_pressed:  # 스위치가 눌렸을 때
        print("Button pressed, executing domino sequence...")

        # 도미노 시퀀스
        for i in range(len(GPIO_PINS)):
            leds[n].on()  # LED 켬
            sleep(1)
            leds[n].off()  # LED 끄기

            # 다음 LED로 이동 (n은 0, 1, 2, 3 순으로 순환)
            n = (n + 1) % len(GPIO_PINS)

    sleep(0.1)  # 100ms 대기

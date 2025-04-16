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
prev_state = True  # 스위치 상태 (True = 'hi', False = 'lo')
led_on = False

while True:
    if switch.is_pressed and prev_state:  # 스위치가 눌렸을 때 상태 변화 감지
        # LED 토글
        if not led_on:
            # LED 켬
            for led in leds:
                led.on()
            led_on = True
        else:
            # LED 끔
            for led in leds:
                led.off()
            led_on = False

    prev_state = switch.is_pressed  # 이전 스위치 상태 갱신
    sleep(0.2)  # 디바운싱 처리

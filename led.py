import serial
import time

RED = [1, 0, 0]
BLACK = [0,0,0]
WHITE = [64,64,64]


def draw_calibration_pixel(ser, led_number, retries=3):
    for _ in range(retries):
        # ser.write(bytearray(BLACK * led_number + RED + BLACK * (299 - led_number)))
        ser.write(WHITE*300)
        time.sleep(0.3)

with serial.Serial("COM3", baudrate=2152000, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE) as ser:
    # for _ in range(5):
    #     for i in range(300):
    draw_calibration_pixel(ser, 50)
    time.sleep(1)

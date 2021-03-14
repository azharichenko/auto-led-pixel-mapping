import serial
import time

RED = [255, 0, 0]
BLACK = [0,0,0]


def draw_calibration_pixel(ser, led_number, retries=3):
    for _ in range(retries):
        ser.write(bytearray(BLACK * led_number + RED + BLACK * (299 - led_number)))
        time.sleep(0.25)

with serial.Serial("COM3", baudrate=2152000, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE) as ser:
    draw_calibration_pixel(ser, 0)
    time.sleep(1)

from machine import Pin 
from utime import sleep

print("Hello teacher!")

ledGreen = Pin(4, Pin.OUT)
ledYellow = Pin(16, Pin.OUT)
ledRed = Pin(21, Pin.OUT)

while True:
    ledRed.on()
    sleep(7)
    print("LedRed ON!")
    ledRed.off()
    print("LedRed OFF!")
    sleep(0.5)

    ledYellow.on()
    sleep(10)
    print("LedYellow ON!")
    ledYellow.off()
    print("LedYellow OFF!")
    sleep(0.5)

    ledGreen.on()
    sleep(20)
    print("LedGreen ON!")
    ledGreen.off()
    print("LedGreen OFF!")
    sleep(0.5)


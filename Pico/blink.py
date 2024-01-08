# blink.py - blink a pin and print the frequency
# Builtin LED on Pico W is referenced using "LED"
# delay time will determine frequency
from machine import Pin
from time import sleep_ms

delay = 25
freq = (1 / (delay * 2)) * 1000
led = Pin("LED", Pin.OUT)

print("blink: ", "LED", "will blink with a delay of",
      delay, "ms at a frequency of", freq, "kHz.")

# with a delay of 100, the pin will have a 5Hz frequency
while True:
    led.off()
    sleep_ms(delay)
    led.on()
    sleep_ms(delay)

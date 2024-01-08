# toggle.py - a more simple blink
# Builtin LED on Pico W is referenced using "LED"
from machine import Pin
from time import sleep_ms

delay = 250
freq = (1 / (delay * 2)) * 1000
led = Pin("LED", Pin.OUT)

print("toggle: ", "LED", "will blink with a delay of",
      delay, "ms at a frequency of", freq, "kHz.")

# with a delay of 100, the pin will have a 5Hz frequency
while True:
    led.toggle()
    sleep_ms(delay)

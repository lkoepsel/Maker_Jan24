# analogSave.py - read an analog to digital pin and save to a file

import machine
from machine import Pin
import sys
import time

samples = 5
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
led = Pin("LED", Pin.OUT)


def temp_convert(t):
    conversion_factor = 3.3 / (65535)
    reading = t * conversion_factor
    celsius = 27 - (reading - 0.706) / 0.001721
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


def read():
    file = open("temps.txt", "w")
    for i in range(samples):
        led.on()
        temp = temp_convert(sensor_temp.read_u16())
        data = str(i) + "\t" + str(time.localtime()) + "\t" + str(temp) + "\n"
        file.write(str(data))
        file.flush()
        time.sleep_ms(1000)
        led.off()
        time.sleep_ms(1000)

    file.close


def print_data():
    file = open("temps.txt", "r")
    print("Sample No \t Local Date/Time \t Temperature")

    for i in range(samples):
        data = file.read()
        print(data, end='')
    print("End of data")
    file.close


if __name__ == '__main__':
    print("Start Logging")
    read()
    print_data()
    print("Logging Complete")
    sys.exit(0)

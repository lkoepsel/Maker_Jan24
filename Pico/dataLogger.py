# dataLogger.py - read an analog to digital pin and save to a file
# self-running if saved as main.py
# delays reading pins for (wait_count * wait_time), if key pressed
# during delay, if key, pressed skip reading pins and print data
# if key not pressed, read pins then print data

from machine import Pin, ADC
import sys
import time
import uselect


# setup for reading keyboard presses
spoll = uselect.poll()
spoll.register(sys.stdin, uselect.POLLIN)

# number of data samples, sensor pin and led pin
samples = 5
sensor = ADC(0)
led = Pin("LED", Pin.OUT)

# number of seconds to wait based on wait_time of 1000
# delay times on reading data and printing data
wait_count = 5
wait_time = 1000
read_time = 500
print_time = 100


# returns key pressed when called, if no key, then None returned
def read_keyboard():
    return(sys.stdin.read(1) if spoll.poll(0) else None)


# waits for a key press within (wait_count * wait_time) delay
# returns key if pressed, otherwise None
def wait_keys():
    print(f"Press a key, to print data or board will read sensor.")
    for i in range(wait_count):
        k = read_keyboard()
        if k is not None:
            return(k)
        led.toggle()
        time.sleep_ms(wait_time)
    return(None)


# read sensor and write to a file
def read_sensor():
    file = open("temps.txt", "w")
    for i in range(samples):
        led.on()
        temp = sensor.read_u16()
        data = str(i) + "\t" + str(time.localtime()) + "\t" + str(temp) + "\n"
        file.write(str(data))
        file.flush()
        time.sleep_ms(read_time)
        led.off()
        time.sleep_ms(read_time)

    file.close


# read the data file and print to serial port
def print_data():
    file = open("temps.txt", "r")
    print("Sample No \t Local Date/Time \t Temperature")

    for i in range(samples):
        led.on()
        data = file.read()
        print(data, end='')
        time.sleep_ms(print_time)
        led.off()
        time.sleep_ms(print_time)
    print("End of data")
    file.close


if __name__ == '__main__':
    time.sleep(1)
    key = wait_keys()
    if key is None:
        print("Start Logging")
        read_sensor()
    print_data()
    print("Print Complete")
    sys.exit(0)

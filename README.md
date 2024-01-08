# ReadMe
This repository provides the files used to better understand embedded microcontrollers in our Makerspace Workshop.

## Introduction
There are two microcontroller boards used in the examples, the *Raspberry Pi Pico* and the *Arduino Uno R3*. The former has sufficient power and memory to be able to run [*MicroPython*](www.micropython.org), hence all of the examples are *MicroPython*. The development environment will use the *Thonny IDE* as it works well for learning *MicroPython*. 

The latter board (*Uno R3*) with its much more simple microcontroller (*ATmega328P*), allows someone with a limited software background to optimize the program for speed. Even though the *Pico* clock speed is 8-times faster and a the 32-bit instruction set provides greater performance, *MicroPython* isn't as [fast as compiled *C++* running on the Uno](https://wellys.com/posts/board-language_speed/). This means the code for the *Uno*, will use the *Arduino IDE* and the *Arduino C++* language.

## Programs
* **blink** - standard "*Hello World*" program for microcontrollers, run this first to understand the programming process
* **toggle** - an enhanced version which assumes a symmetrical *on/off* cycle. The *Uno* version adds an considerable speed enhancement. This program is designed to help you understand how to make changes to enhance performance.
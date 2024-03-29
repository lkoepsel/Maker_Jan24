// Blink_BV
// Blinks a pin as fast as possible using the _BV macro and writing to PIN register
// This function is specific to the AVR family (ATmega328P)
// With no delay, runs at 1.32MHz

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  PINB |= (_BV(PORTB5)); // toggle the bit using C bit set code
  // delay(100); // wait for a 10 milliseconds
}

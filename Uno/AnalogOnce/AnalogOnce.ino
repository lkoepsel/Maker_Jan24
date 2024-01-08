// AnalogOnce -  Reads an analog pin and prints value to serial port.


// the current address in the EEPROM (i.e. which byte we're going to write to next) **/
int sensorPin = A0;    // select the input pin for the potentiometer
unsigned int sensorValue = 0;  // variable to store the value coming from the sensor

// function to "stop" processor, stays in infinite loop
void stop()
{
    while(1) {};
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  unsigned int now = millis();

  Serial.print("Sensor Value: \t");
  Serial.println(sensorValue);

  stop();

}

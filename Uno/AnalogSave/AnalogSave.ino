//  AnalogSave - Reads an analog pin and saves the value to EEPROM.
// Values will stay in the EEPROM once board is
// turned off and may be retrieved later by another sketch.
// If a value has not changed in the EEPROM, it is not overwritten
// which would reduce the life span of the EEPROM unnecessarily.
// Once all values have been read, the values are printed back to the serial port

#include <EEPROM.h>

/** the current address in the EEPROM (i.e. which byte we're going to write to next) **/
int sensorPin = A0;    // select the input pin for the potentiometer
unsigned int sensorValue = 0;  // variable to store the value coming from the sensor
unsigned int now;  // time stamp for data
unsigned int address = 0;
unsigned int memorySize = EEPROM.length()/(sizeof(sensorValue) + sizeof(now));
// int memorySize = 10;

void stop()
{
    while(1) {};
}

void read() {
    Serial.print(memorySize);
    Serial.print(" Readings to be attempted, starting at ");
    Serial.println(address);


    while(address <= memorySize) 
    {
        // read the value from the sensor:
        sensorValue = analogRead(sensorPin);
        unsigned int now = millis();
    
        EEPROM.put(address, now);
        address += sizeof(now);
    
        EEPROM.put(address, sensorValue);
        address += sizeof(sensorValue);

        delay(50);
    }
    Serial.println("End of readings");
}

void print() 
{
    Serial.println("Address\tTime\tData");

    while(address <= memorySize) 
    {
        // print the value from the EEPROM:
        Serial.print(address);
        Serial.print("\t");
        EEPROM.get(address, now);
        Serial.print(now);
        Serial.print("\t");
        address += sizeof(now);
        EEPROM.get(address, sensorValue);
        Serial.println(sensorValue);
        address += sizeof(sensorValue);
    }
    Serial.println("End of memory");
}

void setup() 
{
    Serial.begin(115200);
    Serial.println("");
}

void loop() 
{
    read();
    address = 0;
    print();
    Serial.println("End of Program");
    stop();
  }

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {
  Serial.begin(9600);     // Initialize serial communication for debugging
  mySwitch.enableTransmit(10);  // Set the RF transmitter pin
}

void loop() {
  char data[] = "Hello, Arduino!";  // Data to be sent
  mySwitch.send((uint8_t *)data, strlen(data));  // Send the data
  delay(1000);  // Wait for 1 second before sending again
}
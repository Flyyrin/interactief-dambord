#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {
  Serial.begin(9600);     // Initialize serial communication for debugging
  mySwitch.enableReceive(2);  // Set the RF receiver pin
}

void loop() {
  if (mySwitch.available()) {
    uint32_t receivedValue = mySwitch.getReceivedValue();  // Get the received value
    if (receivedValue != 0) {
      Serial.print("Received: ");
      Serial.println((char *)&receivedValue);  // Print the received data
    }
    mySwitch.resetAvailable();
  }
}
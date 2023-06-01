#include <RH_ASK.h>
#include <SPI.h>

RH_ASK driver;

void setup() {
  Serial.begin(9600);     // Initialize serial communication for debugging
  if (!driver.init()) {
    Serial.println("RadioHead initialization failed");
  }
}

void loop() {
  char data[] = "Hello, Arduino!";  // Data to be sent
  driver.send((uint8_t *)data, strlen(data));  // Send the data
  driver.waitPacketSent();  // Wait for the transmission to complete
  delay(1000);  // Wait for 1 second before sending again
}
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
  uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];  // Buffer to hold received data
  uint8_t buflen = sizeof(buf);  // Length of received data buffer

  if (driver.recv(buf, &buflen)) {  // Check if data is received
    Serial.print("Received: ");
    Serial.println((char *)buf);  // Print the received data
    driver.resetAvailable();
  }
}


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
  uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];  // Buffer to hold received data
  uint8_t buflen = sizeof(buf);  // Length of received data buffer

  if (driver.recv(buf, &buflen)) {  // Check if data is received
    Serial.print("Received: ");
    Serial.println((char *)buf);  // Print the received data
    memset(buf, 0, buflen);  // Clear the buffer
    buflen = sizeof(buf);  // Reset the buffer length
  }
}
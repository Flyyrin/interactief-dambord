#include <RH_ASK.h>
#include <SPI.h>

RH_ASK driver;

void setup() {
  Serial.begin(9600);
  if (!driver.init()) {
    Serial.println("initialization failed");
  }
}

void loop() {
  uint8_t buf[RH_ASK_MAX_MESSAGE_LEN] = {0};
  uint8_t buflen = sizeof(buf);

  if (driver.recv(buf, &buflen)) {  
    Serial.print("Received: ");
    Serial.println((char *)buf);
    driver.resetAvailable();
  }
}
#include <RH_ASK.h>
#include <SPI.h>

RH_ASK driver;

const int up = 3;
const int down = 4;
const int left = 5;
const int right = 6;
const int button = 7;

bool up_pressed = false;
bool down_pressed = false;
bool left_pressed = false;
bool right_pressed = false;
bool button_pressed = false;

void setup() {
  Serial.begin(9600);
  pinMode(up, INPUT);
  pinMode(down, INPUT);
  pinMode(left, INPUT);
  pinMode(right, INPUT);
  pinMode(button, INPUT);
  if (!driver.init()) {
    Serial.println("initialization failed");
  }
}

void loop() {

  if (digitalRead(up) == HIGH) {
    if (up_pressed == false) {
      up_pressed = true;
      char data[] = "up";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    up_pressed = false;
  }

  if (digitalRead(down) == HIGH) {
    if (down_pressed == false) {
      down_pressed = true;
      char data[] = "down";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    down_pressed = false;
  }

  if (digitalRead(left) == HIGH) {
    if (left_pressed == false) {
      left_pressed = true;
      char data[] = "left";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    left_pressed = false;
  }

  if (digitalRead(right) == HIGH) {
    if (right_pressed == false) {
      right_pressed = true;
      char data[] = "right";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    right_pressed = false;
  }

  if (digitalRead(left) == HIGH) {
    if (button_pressed == false) {
      button_pressed = true;
      char data[] = "button";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    button_pressed = false;
  }

}
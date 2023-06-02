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
  pinMode(up, INPUT_PULLUP);
  pinMode(down, INPUT_PULLUP);
  pinMode(left, INPUT_PULLUP);
  pinMode(right, INPUT_PULLUP);
  pinMode(button, INPUT_PULLUP);
  if (!driver.init()) {
    Serial.println("initialization failed");
  }
}

void loop() {
  if (digitalRead(up) == LOW) {
    if (up_pressed == false) {
      up_pressed = true;
      char data[] = "1_up";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    up_pressed = false;
  }

  if (digitalRead(down) == LOW) {
    if (down_pressed == false) {
      down_pressed = true;
      char data[] = "1_down";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    down_pressed = false;
  }

  if (digitalRead(left) == LOW) {
    if (left_pressed == false) {
      left_pressed = true;
      char data[] = "1_left";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    left_pressed = false;
  }

  if (digitalRead(right) == LOW) {
    if (right_pressed == false) {
      right_pressed = true;
      char data[] = "1_right";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    right_pressed = false;
  }

  if (digitalRead(button) == LOW) {
    if (button_pressed == false) {
      button_pressed = true;
      char data[] = "1_press";
      driver.send((uint8_t *)data, strlen(data));
      driver.waitPacketSent();
    }
  } else {
    button_pressed = false;
  }
}
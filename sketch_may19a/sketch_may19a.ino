#include <Servo.h>

Servo cancelaServo;

const int led_verde = 2;
const int led_red = 4;

void setup() {
  cancelaServo.attach(9);
  Serial.begin(9600);

  pinMode(led_verde, OUTPUT);
  pinMode(led_red, OUTPUT);

  cancelaServo.write(90);
  digitalWrite(led_verde, LOW);
  digitalWrite(led_red, HIGH);
}

void loop() {
  if (Serial.available()) {
    char comando = Serial.read();

    if (comando == '1') {
      cancelaServo.write(0);
      digitalWrite(led_verde, HIGH);
      digitalWrite(led_red, LOW);
      delay(5000);
      cancelaServo.write(90);
      digitalWrite(led_verde, LOW);
      digitalWrite(led_red, HIGH);
    }
  }
}

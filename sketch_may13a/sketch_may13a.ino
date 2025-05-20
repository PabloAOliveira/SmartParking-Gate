const int trigPin = 11;
const int echoPin = 12;
long duration;
int distance;

void setup() {
Serial.begin(9600);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
}

void loop() {

digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);


duration = pulseIn(echoPin, HIGH);


distance = duration * 0.034 / 2;


if (distance > 0 && distance < 20) {
Serial.println("1");
} else {
Serial.println("0");
}

delay(500);
}

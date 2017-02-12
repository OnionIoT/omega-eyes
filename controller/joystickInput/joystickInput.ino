int xInputPin = A0;
int yInputPin = A1;

int tolerance;

int xValue;
int yValue;

int xValuePrev;
int yValuePrev;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // set initial values
  xValuePrev = 0;
  yValuePrev = 0;

  tolerance = 5;
}

void loop() {
  // save the previous value
  xValuePrev = xValue;
  yValuePrev = yValue;
  
  // read the new value
  xValue = analogRead(xInputPin);
  yValue = analogRead(yInputPin);

  // output only if there has been a change
  if (valueChanged(xValue, xValuePrev, tolerance) || valueChanged(yValue, yValuePrev, tolerance) ) {
    printJoystickValue();
  }

  delay(100);
}

int valueChanged(int current, int prev, int tolerance) {
  if (prev > (current + tolerance) || prev < (current - tolerance)) {
    return 1;
  }
  return 0;
}

void printJoystickValue () {
  Serial.print(xValue);
  Serial.print(" ");
  Serial.println(yValue);
}



#include <AFMotor.h>
#include <Servo.h> 

AF_DCMotor camera_trigger(1);
AF_Stepper focus_stepper(200, 2);
String input_string;
char command_letter;
int value;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  focus_stepper.setSpeed(5);
}

void trigger_camera(int duration){
  camera_trigger.setSpeed(255);
  camera_trigger.run(BACKWARD);
  delay(duration);
  camera_trigger.run(RELEASE);
  Serial.print("executed trigger with duration: ");
  Serial.println(duration);  
}

void move_forward(int distance, int step_size){
  focus_stepper.step(distance, FORWARD, step_size);
  focus_stepper.release();
  Serial.print("moved focus forward number of steps: ");
  Serial.println(distance);
}

void move_backward(int distance, int step_size){
  focus_stepper.step(distance, BACKWARD, step_size);
  focus_stepper.release();
  Serial.print("moved focus forward number of steps: ");
  Serial.println(distance);
}


void loop() {
  command_letter = ' ';
  value = 0;
  
  input_string = Serial.readStringUntil('\n');
  if (input_string.length() > 0){
    command_letter = input_string.charAt(0);
    value = input_string.substring(1, input_string.length()).toInt();
    if (command_letter == 't' and value > 0){
      trigger_camera(value);
    } else if (command_letter == 'f' and value > 0){
      move_forward(value, INTERLEAVE);
    } else if (command_letter == 'F' and value > 0){
      move_forward(value, DOUBLE);
    } else if (command_letter == 'b' and value > 0){
      move_backward(value, INTERLEAVE);
    } else if (command_letter == 'B' and value > 0){
      move_backward(value, DOUBLE);
    } else if (command_letter == 's' and value >= 0){
      
    }
  }
}

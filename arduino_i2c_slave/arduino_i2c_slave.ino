////////////////////////////////
// GPS Module - GP-20U7 - Arduino UNO Example
//
// Author: Gustavo Bertoli
//
// References:
// https://cdn.sparkfun.com/datasheets/GPS/GP-20U7.pdf
// https://www.arduino.cc/en/Reference/SoftwareSerial
// http://forum.arduino.cc/index.php?topic=288234.0
// 

// red = 5v, black = GND, white = pin 1 (RX)
#include <SoftwareSerial.h> 
#include <Wire.h>

#define SLAVE_ADDRESS 0x04

SoftwareSerial GPS_Serial(0, 1); // RX, TX

int number = 0;
int state = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  GPS_Serial.begin(9600);  //start listening to GPS
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  
  Serial.println("Ready!");

}

void loop() {
  delay(100);
}

// callback for received data
void receiveData(int byteCount){

  while(Wire.available()) {
    number = Wire.read();
    Serial.print("data received: ");
    Serial.println(number);
  
    if (number == 1){
  
      if (state == 0){
        digitalWrite(13, HIGH); // set the LED on
        state = 1;
      }
      else{
        digitalWrite(13, LOW); // set the LED off
        state = 0;
      }
    }
  }
}

// callback for sending data
void sendData(){
   char rc;

   if (GPS_Serial.available()){
      rc = GPS_Serial.read();
//        Serial.write(rc);
      Wire.write(rc);
   }
//  Wire.write(number);
}

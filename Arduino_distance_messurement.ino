#include <LiquidCrystal.h>
// Setup

int trig = 13;
int echo = 11; 
int rs = 7; 
int e = 8; 
int d4 = 2; 
int d5 = 3;
int d6 = 4; 
int d7 = 5; 
String msg = "Distance: "; 
String si = "in"; 

// variables for the mathematics 

float t; 
int dt = 500;  
float r = 0.0135473; 
float x; 

//Creation of the lcd object 

LiquidCrystal lcd(rs, e, d4, d5, d6, d7); 

void setup() {
lcd.begin(16, 2); 
//lcd.clear(); 
pinMode(trig, OUTPUT); 
pinMode(echo, INPUT); 
Serial.begin(9600); 




}

void loop() {

//retrieving the time neeeded to recieve a sound wave
 

digitalWrite(trig, LOW); 
delayMicroseconds(2); 
digitalWrite(trig, HIGH); 
delayMicroseconds(2); 
digitalWrite(trig, LOW); 
t = pulseIn(echo, HIGH); 
t = t/2.; //the t is the time taken to recieve starting from transmission, thus we must divide by 2 as it takes time for the wave to bounce 
x = r * t; // x as the position in inches, must be the product of the speed of sound in inches per microseconds, times the microseconds it takes.
Serial.println(x); //for the purpose of a test

// The position must be written on the lcd

lcd.setCursor(0,0); 
lcd.print(msg);
lcd.print(x);
lcd.print(si); 
delay(dt); 
lcd.clear(); 
 

}

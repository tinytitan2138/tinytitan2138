
int LED1 = 13;
int LED2 = 12; 
int LED3 = 11;
int SHORT = 175;
int LONG = 500; 


int dot()
{
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED3, HIGH);
  delay(SHORT); 
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  delay(SHORT); 
}

int dash() 
{
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED3, HIGH);
  delay(LONG); 
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  delay(LONG); 
}

int morse_code(String text) 
{
  for (char x: text) {
    switch(x) {
    case 'a':
    case 'A':
      dot();
      dash();
      break; 
    case 'b':
    case'B':
      dash();
      dot();
      dot();
      dot();
      break; 
    case 'c':
    case 'C':
      dash();
      dot();
      dash();
      dot(); 
      break;
    case 'd':
    case 'D':
      dash();
      dot();
      dot(); 
      break; 
    case 'e':
    case 'E':
      dot(); 
      break; 
    case 'f':
    case 'F':
      dot();
      dot();
      dash();
      dot(); 
      break;
    case 'g':
    case 'G':
      dash();
      dash();
      dot();
      break;
    case 'h':
    case 'H':
      dot();
      dot();
      dot();
      dot();
      break; 
    case 'i':
    case 'I':
      dot();
      dot();
      break; 
    case 'j':
    case 'J':
      dot();
      dash();
      dash();
      dash();
      break; 
    case 'k':
    case 'K':
      dash();
      dot();
      dash();
      break;
    case 'l':
    case 'L':
      dot();
      dash();
      dot();
      dot();
      break; 
    case 'm':
    case 'M':
      dash();
      dash();
      break;
    case 'n':
    case 'N':
      dash();
      dot();
      break;
    case 'o':
    case 'O':
      dash(); 
      dash();
      dash();
      break;
    case 'p':
    case 'P':
      dot();
      dash();
      dash();
      dot();
      break;
    case 'q':
    case 'Q':
      dash();
      dash();
      dot();
      dash();
      break; 
    case 'r':
    case 'R':
      dot();
      dash();
      dot();
      break;
    case 's':
    case 'S':
      dot();
      dot();
      dot();
      break;
    case 't':
    case 'T':
      dash();
      break;
    case 'u':
    case 'U':
      dot();
      dot();
      dash();
      break; 
    case 'v':
    case 'V':
      dot();
      dot();
      dot();
      dash();
      break; 
    case 'w':
    case 'W':
      dot();
      dot();
      dash();
      break; 
    case 'x':
    case 'X':
      dash();
      dot();
      dot();
      dash();
      break; 
    case 'y':
    case 'Y':
      dash();
      dot();
      dash();
      dash();
      break;
    case 'z':
    case 'Z':
      dash();
      dash();
      dot();
      dot();
      break; 
  case ' ': 
  case ',':
  case '.':
  case '?':
  case '!': 
  
    break; 
  case '1':
    dot();
    dash();
    dash();
    dash();
    dash(); 
    break; 
  case '2':
    dot();
    dot();
    dash();
    dash();
    dash();
    break; 
  case '3': 
    dot();
    dot();
    dot();
    dash();
    dash();
    break; 
  case '4':
    dash();
    dash();
    dash();
    dash();
    dot();
    break;
  case '5':
    dot();
    dot();
    dot();
    dot();
    dot(); 
    break; 
  case '6':
    dash();
    dot();
    dot();
    dot();
    dot();
    break;
  case '7':
    dash();
    dash();
    dot();
    dot();
    dot();
    break; 
  case '8': 
    dash();
    dash();
    dash();
    dot();
    dot();
    break; 
  case '9':
    dash();
    dash();
    dash();
    dash();
    dot();
    break; 
  case '0':
    dash();
    dash();
    dash();
    dash(); 
    dash(); 
    break; 
   
   default: 
    digitalWrite(LED1, LOW); 
    digitalWrite(LED2, LOW);
    digitalWrite(LED3, LOW);
    delay(10000); 
    break; 
    };
  };  

  
}

void setup() 
{
   pinMode(LED1, OUTPUT);
   pinMode(LED2, OUTPUT);
   pinMode(LED3, OUTPUT); 
}

void loop() 
{
  morse_code("Hello, World!");
  delay(5000); 
}

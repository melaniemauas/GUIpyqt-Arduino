void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  // Inicializo el puerto serie a 9600 baudios
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(A0);  // Leo el pin A0 (0-1023)
  
  // Escala a volts
  float voltage = sensorValue * (5.0 / 1023.0);  // Convierte a volts (0-5 V)
  
  Serial.println(voltage);  // Envía el valor al PC
  
  delay(100);  // Espera 100 ms → ~10 lecturas por segundo
}

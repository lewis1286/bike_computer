#!/usr/bin/python
# coding = utf-8
#
import time
import serial
ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=2)
print ser      # Despliega datos del puerto serial
print ser.isOpen()
# define tipo de display
# ser.write(chr(0x7C))  # Comando
# ser.write(chr(3)) # 3:20 caracteres  4:16 caracteres
# ser.write(chr(0x7C))  # Comando
# ser.write(chr(5)) # 5:4 lineas  6:2 lineas
# ser.write(chr(0x7C))  # Comando
# ser.write(chr(0x0C)) # display on
# # ajusta brillo leds
# ser.write(chr(0x7C))  # Comando
# ser.write(chr(144)) # 128 a 157 128:nada 143:medio 157:full
# # limpiar display
# ser.write(chr(0xFE))  # Comando
# ser.write(chr(1)) #
# # linea 1:128 2:192
# # 3:148 4:212
# ser.write(chr(0xFE))  # Comando
# ser.write(chr(128)) # linea+chr
# # escribir
# # cadena de
# caracteres
# normales
ser.write("proyectoelectronico.com")
time.sleep(10)
ser.close()     # cierra puerto serial

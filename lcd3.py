from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD("PCF8574", 0x27)

lcd.write_string('Raspberry Pi')


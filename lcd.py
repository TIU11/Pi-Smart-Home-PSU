from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD("PCF8574", 0x27)
lcd.write_string('Raspberry Pi HD44780')
lcd.cursor_pos = (2, 0)
lcd.write_string('https://github.com/\n\rdbrgn/RPLCD')


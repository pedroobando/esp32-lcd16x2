
from machine import Pin, SoftI2C, sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time
# import datetime 

# Parametros del LCD 16x2
I2C_ADDR = 0X27
TOTAL_ROWS = 2
TOTAL_COLS = 16

SCL_GPIO_22 = Pin(22)
SDA_GPIO_21 = Pin(21)
FREQ = 10000

i2c = SoftI2C(scl=SCL_GPIO_22, sda=SDA_GPIO_21, freq=FREQ)
lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLS)
# lcd.backlight_off()
lcd.backlight_on()
lcd.clear()
# lcd.move_to(0, 1)
# lcd.putstr("ESP32 y LCD")

lcd.putstr("Romana: ")

contador_romana = 0
while True:
  lcd.move_to(8, 0)
  lcd.putstr(str(contador_romana))
  time.sleep(.6)
  contador_romana = contador_romana + 24
  print(str(contador_romana))




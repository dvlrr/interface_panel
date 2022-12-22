# Imports
from machine import Pin, I2C, PWM, 
from ssd1306 import SSD1306_I2C
import time
import framebuf

# Define buttons
button1 = Pin(18, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(19, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(20, Pin.IN, Pin.PULL_DOWN)

# Define LEDs

led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(5, Pin.OUT)
led5 = Pin(6, Pin.OUT)
led6 = Pin(7, Pin.OUT)
ledgreen = Pin(8, Pin.OUT)
ledred = Pin(9, Pin.OUT)

# Define buzzer pin

# Define buzzer duty

# Define buzzer tones

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

# Define display dimensions

WIDTH = 128
HEIGHT = 32

# Define current time in hours

gmt = time.localtime()[3]

# Define messages

awake = "Mummy and Daddy are awake! Go find them..."
asleep = "Mummy and Daddy are asleep..."
default = "Mummy & Daddy Bot is waiting for your instruction"
cuddle = "You have selected cuddle"
bad_dream = "You have selected bad dream"
playtime = "You have selected playtime"
snack = "You have selected snack"
wee = "You have selected wee-wee"
poo = "You have selected poo"
lights_on = "Turning lights on"
lights_off = "Turning lights off"

# Scripting - When button is pressed: light LED, play confirmation message, check time & either play positive/negative noise and display positive/negative message after delay

while True:
    
    time.sleep(1)
    
    display.fill(0)
    
    display.text(default,0,0)
    
    display.show()
    
    
    if button1.value() == 1: # If button 1 is pressed
        
        led1.value(1)
        display.fill(0)
        display.text(cuddle,0,0)
        display.show()
        time.sleep(5)
        led1.value(0)
        display.fill(0)
        print(cuddle)
            
        if 06 < gmt < 21: # If between 6am & 9pm
                
                ledgreen.value(1)
                display.text(awake,0,0)
                display.show()
                
                
        elif 21 < gmt < 00: # If between 9pm & 12am
                
                ledred.value(1)
                display.text(asleep,0,0)
                display.show()
            
        elif 01 < gmt < 05: # If between 1am & 5am
                
                ledred.value(1)
                display.text(asleep,0,0)
                display.show()
    
    
    
    
    
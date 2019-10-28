from gfxhat import lcd, backlight
import random
import time


backlight.set_all(255, 255, 200)
backlight.show()
lcd.clear()
lcd.show()

#function to erase object
def eraseObject(obj,x=0,y=0):
    for i in range(0, len(obj)):
        for j in range(0, len(obj[i])):
            lcd.set_pixel(x+j,y+i,0)
            lcd.show()
            
#Function that displays an object
def displayObject(obj,x,y):
    for i in range(0, len(obj)):
        for j in range(0, len(obj[i])):
            lcd.set_pixel(x+j,y+i,obj[i][j])
            lcd.show()
            x = x + vx
            lcd.show()

ball =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]


#function moves an object from position x,y to new position x+vx,y+vy. It returns the new coordinates x and y.
vx = 10
vy = 10
def moveObject(obj,x=0,y=0,vx=0,vy=0):
    while x < 127 or y < 63:
        for i in range(0, len(obj)):
            for j in range(0, len(obj[i])):
                lcd.set_pixel(x+j,y+i,obj[i][j])
                lcd.show()
        lcd.clear()
        x+=vx
        lcd.show()

    
                    
                
#Function to check collision and ensure object moves within screen size
def checkCollision(obj,x=0,y=0,vx=0,vy=0,sx=127,sy=63):
    sx = False
    while not sx:
        if x == sx:
            y = y + vy
            x = x - vx
        if x == 0:
            y = y - vy
            x = x + vx
        if y == 0:
            y = y + vy
            x = x - vx
        if y == sy:
            y = y - vy
            x = x + vx




#Program that bounces ball
def bouncingBall():
    while True:
        x = input("Input x starting point ")
        y = input("Input y starting point ")
        eraseObject(ball)
        moveObject(ball,x,y,10,0)
        checkCollision(ball, x, y, 10, 10, 127, 63)
        time.sleep(.1)

bouncingBall()
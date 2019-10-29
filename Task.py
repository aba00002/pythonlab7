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
x = 0
y = 0
vx = 2
vy = 2
def moveObject(obj,x,y,vx,vy):
    while x < 127 or y < 63:
        for i in range(0, len(obj)):
            for j in range(0, len(obj[i])):
                lcd.set_pixel(x+j,y+i,obj[i][j])
                lcd.show()
        lcd.clear()
        x+=vx
        y+=vy
        lcd.show()

    
                    
                
#Function to check collision and ensure object moves within screen size
def checkCollision(obj,x,y,vx,vy,sx=127,sy=63):
    h = len(obj)
    w = len(obj[0])
    if y < 0 or y+h>63 or x + w>127 or x < 0:
        if y<0:
            y=0
            vy +=vy
        if y+h>63:
            y=63-h
            vy = -vy
        if x<0:
            x=0
            vx +=vx
        if x+w>127:
            x=127-w
            vx = -vx
    return x,y,vx,vy 



#Program that bounces ball
sx = 127
sy = 63
def bouncingBall(obj,x,y,vx,vy,sx=127,sy=63):
    while (True):
        for i in range(0, len(obj)):
            for j in range(0, len(obj[i])):
                lcd.set_pixel(x+j,y+i,obj[i][j])
                lcd.show()
                time.sleep(.1)
                lcd.clear()
                x+=vx
                y+=vy
                lcd.show()
                x,y,vx,vy=checkCollision(obj, x, y, vx, vy, sx, sy)
        

bouncingBall(ball,x,y,vx,vy,sx,sy)
# Because fuck you that's why.

# I figured out what was wrong, but not why. I rewrote the suspected code, and now it works! ¯\_(?)_/¯

"""
........................./´¯/) 
......................,/¯..// 
...................../..../ / 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´(..´......,~/'...') 
.........\.................\/..../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\ 
"""

import TouchCircle
import CircleButton
import Colors
import AssetCache

myTouchCircle = None
circleButton = None

def initialize():
    global myTouchCircle, circleButton
    myTouchCircle = TouchCircle.TouchCircle()
    circleButton = CircleButton.CircleButton(250, 250, 150, Colors.SteelBlue, Colors.White, AssetCache.buttonFont)
    circleButton.setClickEvent(buttonPress)
    circleButton.setButtonCaption("wow such circle")

def update(deltaTime):
    global myTouchCircle, circleButton
    myTouchCircle.update(deltaTime)
    circleButton.update(deltaTime)

def handleInput(event):
    global myTouchCircle, circleButton
    myTouchCircle.handleInput(event)
    circleButton.handleInput(event)

def buttonPress():
    global circleButton
    circleButton.active = False

def draw(deltaTime):
    global myTouchCircle, circleButton
    myTouchCircle.draw()
    circleButton.draw(Colors.DarkOrange, Colors.White)

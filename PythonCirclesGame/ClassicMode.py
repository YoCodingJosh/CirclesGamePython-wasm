# ClassicMode.py - 
# Created by Josh Kennedy on 24 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import TouchCircle

class ClassicMode(object):
    def __init__(self):
        self.testCircle = TouchCircle.TouchCircle()
        testCircle.onTouch = testPrint

    def testPrint(self):
        print("test print, please ignore")

    def update(self, deltaTime):
        self.testCircle.update(deltaTime)

    def handleInput(self, event):
        self.testCircle.handleInput(event)

    def draw(self, deltaTime):
        self.testCircle.draw()

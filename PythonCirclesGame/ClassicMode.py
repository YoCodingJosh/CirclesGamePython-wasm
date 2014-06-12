# ClassicMode.py - 
# Created by Josh Kennedy on 24 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import TouchCircle

class ClassicMode(object):
    def __init__(self):
        self.testCircle = TouchCircle.TouchCircle()
        self.testCircle.onTouch = self.testPrint
        self.active = False
        self.started = False

    def startGame(self):
        self.active = True
        self.started = True

    def stopGame(self):
        self.active = False

    def testPrint(self):
        print("test print, please ignore")

    def update(self, deltaTime):
        if not self.active: return

        self.testCircle.update(deltaTime)

    def handleInput(self, event):
        if not self.active: return

        self.testCircle.handleInput(event)

    def draw(self, deltaTime):
        if not self.active: return

        self.testCircle.draw()

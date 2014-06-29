# ClassicMode.py - Classic Gameplay Mode
# Created by Josh Kennedy on 24 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import TouchCircle
import BadCircle

import random

class ClassicMode():
    def __init__(self):
        self.active = False
        self.started = False
        self.circlesList = list();
        self.level = -1
        self.numBad = 0

    def startGame(self):
        # We're rollin!
        self.active = True
        self.started = True

        # Start with level 1.
        self.startLevel(1)

    def startLevel(self, classicLevel):
        self.level = classicLevel

        # Clear out the circles (because bad circles don't clear out)
        self.circlesList.clear()

        # Determine the number of bad circles.
        if (self.level == 1):
            self.numBad = 0
        elif (self.level <= 4):
            self.numBad = 1
        else:
           self.numBad = int((self.level / 5) + 1)

        # Add the bad circles
        for x in range(self.numBad):
            myBad = BadCircle.BadCircle()
            myBad.onTouch = self.badTouch

            self.circlesList.append(myBad)

        # Add the current level amount of circles.
        for i in range(self.level):
            # Create circle.
            myCircle = TouchCircle.TouchCircle()
            myCircle.onTouch = self.goodTouch

            self.circlesList.append(myCircle)

    def stopGame(self):
        self.active = False

    def badTouch(self, circle):
        self.active = False
        print("GAME OVER MAN, GAME OVER!!")

    def goodTouch(self, circle):
        # I could use __repr__()
        # But that returns the type and the address, and I only want the address.
        print("wow such circle at " + hex(id(circle)))
        self.circlesList.remove(circle)

    def update(self, deltaTime):
        if not self.active: return

        if len(self.circlesList) - self.numBad <= 0:
            self.level += 1
            self.startLevel(self.level)

        for circle in self.circlesList:
            circle.update(deltaTime)

    def handleInput(self, event):
        if not self.active: return

        for circle in self.circlesList:
            circle.handleInput(event)

    def draw(self, deltaTime):
        if not self.active: return

        for circle in self.circlesList:
            circle.draw()

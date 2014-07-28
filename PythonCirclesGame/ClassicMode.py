# ClassicMode.py - Classic Gameplay Mode
# Created by Josh Kennedy on 24 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import TouchCircle
import BadCircle
import AssetCache
import Colors
import HighScore
import Rectangle
import HelperAPI

import pygame

import random

class ClassicMode():
    def __init__(self):
        self.active = False
        self.started = False
        self.circlesList = list();
        self.boundary = HelperAPI.getWindowRectangleAsRectangle()
        self.boundary.y = 30
        #self.boundary.height -= 30
        self.level = -1
        self.numBad = 0
        self.score = -1

    def startGame(self):
        # We're rollin!
        self.active = True
        self.started = True
        self.score = 0

        # Initialize High Score
        self.highScoreObject = HighScore.HighScore()
        self.highScore = self.highScoreObject.getScore("Classic")
        print("High Score is " + str(self.highScore))

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
            myBad = BadCircle.BadCircle(self.boundary)
            myBad.onTouch = self.badTouch

            self.circlesList.append(myBad)

        # Add the current level amount of circles.
        for i in range(self.level):
            # Create circle.
            myCircle = TouchCircle.TouchCircle(self.boundary)
            myCircle.onTouch = self.goodTouch

            self.circlesList.append(myCircle)

    def stopGame(self):
        self.active = False

    def badTouch(self, circle):
        AssetCache.badPopSound.play()
        self.active = False
        self.gameOver()

    def gameOver(self):
        print("GAME OVER MAN, GAME OVER!!")
        print("Final Score: " + str(self.score) + " ", end = '')
        print("points" if self.score > 1 else "point")

        if (self.score > self.highScore):
            print("You have a new high score! Sweet! :D")
            self.highScoreObject.setScore("Classic", self.score)
        else:
            print("Awww shucks, you don't have a new high score. :(")

    def goodTouch(self, circle):
        # I could use __repr__()
        # But that returns the type and the address, and I only want the address.
        print("wow such circle at " + hex(id(circle)))
        self.circlesList.remove(circle)

        AssetCache.lowPopSound.play()
        
        self.score += 1

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

        pygame.display.get_surface().fill(Colors.DarkMediumGray.getTuple())

        self.boundary.draw(Colors.White)

        for circle in self.circlesList:
            circle.draw()

        scoreSurface = AssetCache.scoreFont.render("Score: " + str(self.score), True, Colors.Red.getTuple())

        pygame.display.get_surface().blit(scoreSurface, (0, 0))

# ClassicMode.py - Classic Gameplay Mode
# Created by Josh Kennedy on 24 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import TouchCircle
import BadCircle
import AssetCache
import Colors
import HighScore
import HelperAPI
import GameOverScreen

import pygame

import random

class ClassicMode():
    def __init__(self):
        self.active = False
        self.started = False
        self.circlesList = list();
        self.boundary = HelperAPI.getWindowRectangleAsRectangle()
        self.level = -1
        self.numBad = 0
        self.score = -1
        self.gameOverScreen = None
        self.isGameOver = False

    def startGame(self):
        # We're rollin!
        self.active = True
        self.started = True
        self.introFinished = False
        self.score = 0
        self.gameOverScreen = None
        self.isGameOver = False

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

        # Add the current level amount of circles.
        for i in range(self.level):
            if (i == (int)(self.level / 2)):
                # Add bad circles.
                for i in range(self.numBad):
                    myBad = BadCircle.BadCircle(self.boundary)
                    myBad.onTouch = self.badTouch
                    self.circlesList.append(myBad)

            # Create circle.
            myCircle = TouchCircle.TouchCircle(self.boundary)
            myCircle.onTouch = self.goodTouch

            # and put it in the list (last in line).
            self.circlesList.append(myCircle)

    def stopGame(self):
        self.active = False
        self.started = False

    def badTouch(self, circle):
        AssetCache.badPopSound.play()
        self.gameOver()

    def gameOver(self):
        self.isGameOver = True
        self.active = False

        print("GAME OVER MAN, GAME OVER!!")
        print("Final Score: " + str(self.score) + " points")

        if (self.score > self.highScore):
            print("You have a new high score! Sweet! :D")
            self.highScoreObject.setScore("Classic", self.score)
        else:
            print("Awww shucks, you don't have a new high score. :(")

        # Let's create the Game Over Screen
        self.gameOverScreen = GameOverScreen.GameOverScreen(1, self.score, self.highScore, self)

    def goodTouch(self, circle):
        # I could use __repr__()
        # But that returns the type and the address, and I only want the address.
        print("wow such circle at " + hex(id(circle)))
        #self.circlesList.remove(circle)
        circle.active = False

        HelperAPI.playRandomPopSound()
        
        self.score += 1

    def update(self, deltaTime):
        if not self.introFinished:
            if (self.boundary.y < 30):
                self.boundary.y += (0.6 * deltaTime) * 100
                return
            else:
                self.boundary.y = int(self.boundary.y)
                self.introFinished = True

        if (self.isGameOver):
            self.gameOverScreen.update(deltaTime)
        
        if (not self.active): return

        if len(self.circlesList) - self.numBad <= 0:
            self.level += 1
            self.startLevel(self.level)

        for circle in self.circlesList:
            circle.update(deltaTime)

    def handleInput(self, event):
        if (not self.active and self.isGameOver):
            self.gameOverScreen.handleInput(event)

        if not self.active: return

        i = 0
        while i < len(self.circlesList):
            self.circlesList[i].handleInput(event)

            if (self.circlesList[i].active is False):
                self.circlesList.remove(self.circlesList[i])
                break
            
            i += 1

    def draw(self, deltaTime):
        pygame.display.get_surface().fill(Colors.DarkMediumGray.getTuple())

        self.boundary.draw(Colors.White)

        if not self.introFinished: return

        for circle in reversed(self.circlesList):
            circle.draw()

        scoreSurface = AssetCache.scoreFont.render("Score: " + str(self.score), True, Colors.Red.getTuple())

        if not self.isGameOver:
            pygame.display.get_surface().blit(scoreSurface, (0, 0))
        
        if (not self.active and self.isGameOver):
            self.gameOverScreen.draw()

    def restartGame(self):
        print("Restarting Classic Mode...")
        self.startGame()

    def mainMenu(self):
        pass

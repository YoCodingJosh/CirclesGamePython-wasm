# MainMenu.py - The game's main menu.
# Created by Josh Kennedy on 22 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import AssetCache

import Colors
import TouchCircle
import Circle
import CircleButton
import GameInit

class MainMenu():
    def __init__(self):
        self.playGameCircleButton = CircleButton.CircleButton(200, 150, 100, Colors.Cyan, Colors.White, AssetCache.buttonFont)
        self.playGameCircleButton.setButtonCaption("Play Game!")
        self.playGameCircleButton.setClickEvent(self.playGame)
        
        self.playMenuBackgroundCircle = Circle.Circle(200, 150, 100)

        self.optionsCircleButton = CircleButton.CircleButton(450, 150, 100, Colors.DeepPink, Colors.Black, AssetCache.buttonFont)
        self.optionsCircleButton.setButtonCaption("Options")
        self.optionsCircleButton.setClickEvent(self.showOptions)
        
        self.optionsMenuBackgroundCircle = Circle.Circle(450, 150, 100)

        self.creditsCircleButton = CircleButton.CircleButton(200, 400, 100, Colors.ForestGreen, Colors.Gold, AssetCache.buttonFont)
        self.creditsCircleButton.setButtonCaption("Credits")
        self.creditsCircleButton.setClickEvent(self.showCredits)

        self.creditsBackgroundCircle = Circle.Circle(200, 400, 100)

        self.exitCircleButton = CircleButton.CircleButton(450, 400, 100, Colors.MediumPurple, Colors.Black, AssetCache.buttonFont)
        self.exitCircleButton.setButtonCaption("Exit Game")
        self.exitCircleButton.setClickEvent(self.exitGame)

        self.exitBackgroundCircle = Circle.Circle(450, 400, 100)

        self.transitionToMenu = False

        # 0 is main menu, 1 is play game, 2 is options, 3 is credits
        self.selectedMenu = 0
        self.currentMenu = 0

    def update(self, deltaTime):
        self.playGameCircleButton.update(deltaTime)
        self.optionsCircleButton.update(deltaTime)
        self.creditsCircleButton.update(deltaTime)
        self.exitCircleButton.update(deltaTime)

        if (self.transitionToMenu and self.selectedMenu == 1 and self.playMenuBackgroundCircle.radius <= 1220):
            self.playMenuBackgroundCircle.radius += int((5 * deltaTime) * 100)
        elif (self.playMenuBackgroundCircle.radius >= 1220):
            self.exitCircleButton.active = False
            self.creditsCircleButton.active = False
            self.optionsCircleButton.active = False
            self.transitionToMenu = False
            self.currentMenu = 1

    def handleInput(self, event):
        self.playGameCircleButton.handleInput(event)
        self.optionsCircleButton.handleInput(event)
        self.creditsCircleButton.handleInput(event)
        self.exitCircleButton.handleInput(event)

    def draw(self, deltaTime):
        self.playGameCircleButton.draw(Colors.SpringGreen, Colors.Black)
        self.optionsCircleButton.draw(Colors.Khaki, Colors.White)
        self.creditsCircleButton.draw(Colors.Purple, Colors.White)
        self.exitCircleButton.draw(Colors.Tomato, Colors.Black)

        if (self.currentMenu == 1 or self.selectedMenu == 1):
            self.playMenuBackgroundCircle.draw(Colors.SpringGreen)

    def playGame(self):
        AssetCache.highPopSound.play()
        print("test print, please ignore")
        self.transitionToMenu = True
        self.exitCircleButton.clickable = False
        self.creditsCircleButton.clickable = False
        self.optionsCircleButton.clickable = False
        self.playGameCircleButton.active = False
        self.selectedMenu = 1

    def showOptions(self):
        AssetCache.lowPopSound.play()
        print("options not implemented yet")
    
    def showCredits(self):
        AssetCache.highPop2Sound.play()
        print("credits not yet implemented")

    def exitGame(self):
        AssetCache.badPopSound.play()
        pygame.time.delay(666)
        GameInit.exitGame()

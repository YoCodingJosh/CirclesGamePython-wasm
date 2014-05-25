# MainMenu.py - The game's main menu.
# Created by Josh Kennedy on 22 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import AssetCache

import Colors
import TouchCircle
import CircleButton
import GameInit

class MainMenu():
    def __init__(self):
        self.playGameCircleButton = CircleButton.CircleButton(200, 150, 100, Colors.Cyan, Colors.White, AssetCache.buttonFont)
        self.playGameCircleButton.setButtonCaption("Play Game!")
        self.playGameCircleButton.setClickEvent(self.playGame)

        self.optionsCircleButton = CircleButton.CircleButton(450, 150, 100, Colors.DeepPink, Colors.Black, AssetCache.buttonFont)
        self.optionsCircleButton.setButtonCaption("Options")
        self.optionsCircleButton.setClickEvent(self.showOptions)

        self.creditsCircleButton = CircleButton.CircleButton(200, 400, 100, Colors.ForestGreen, Colors.Gold, AssetCache.buttonFont)
        self.creditsCircleButton.setButtonCaption("Credits")
        self.creditsCircleButton.setClickEvent(self.showCredits)

        self.exitCircleButton = CircleButton.CircleButton(450, 400, 100, Colors.MediumPurple, Colors.Black, AssetCache.buttonFont)
        self.exitCircleButton.setButtonCaption("Exit Game")
        self.exitCircleButton.setClickEvent(self.exitGame)

    def update(self, deltaTime):
        return

    def handleInput(self, event):
        self.playGameCircleButton.handleInput(event)
        self.optionsCircleButton.handleInput(event)
        self.creditsCircleButton.handleInput(event)
        self.exitCircleButton.handleInput(event)

    def draw(self, deltaTime):
        self.playGameCircleButton.draw(Colors.SpringGreen, Colors.Black)
        self.optionsCircleButton.draw(Colors.Gold, Colors.White)
        self.creditsCircleButton.draw(Colors.Purple, Colors.White)
        self.exitCircleButton.draw(Colors.Tomato, Colors.Black)

    def playGame(self):
        print("test print, please ignore")

    def showOptions(self):
        print("options not implemented yet")
    
    def showCredits(self):
        print("credits not yet implemented")

    def exitGame(self):
        GameInit.exitGame()

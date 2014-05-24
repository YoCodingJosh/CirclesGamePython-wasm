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

class MainMenu():
    def __init__(self):
        self.playGameCircleButton = CircleButton.CircleButton(200, 150, 100, Colors.Cyan, Colors.White, AssetCache.buttonFont)
        self.playGameCircleButton.setButtonCaption("Play Game!")
        self.playGameCircleButton.setClickEvent(self.playGame)

        self.optionsCircleButton = CircleButton.CircleButton(450, 150, 100, Colors.DeepPink, Colors.Black, AssetCache.buttonFont)
        self.optionsCircleButton.setButtonCaption("Options")
        self.optionsCircleButton.setClickEvent(self.showOptions)

    def update(self, deltaTime):
        return

    def handleInput(self, event):
        self.playGameCircleButton.handleInput(event)
        self.optionsCircleButton.handleInput(event)

    def draw(self, deltaTime):
        self.playGameCircleButton.draw(Colors.SpringGreen, Colors.Black)
        self.optionsCircleButton.draw(Colors.Gold, Colors.White)

    def playGame(self):
        print("test print, please ignore")

    def showOptions(self):
        print("options not implemented yet")

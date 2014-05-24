# CirclesGame.py - Updates and draws the game and the menu.
# Created by Josh Kennedy on 18 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import TouchCircle
import MainMenu

class CirclesGame():
    def __init__(self):
        self.showMainMenu = True
        self.mainMenu = MainMenu.MainMenu()

    def update(self, deltaTime):
        if self.showMainMenu:
            self.mainMenu.update(deltaTime)

    def handleInput(self, event):
        if self.showMainMenu:
            self.mainMenu.handleInput(event)

    def draw(self, deltaTime):
        if self.showMainMenu:
            self.mainMenu.draw(deltaTime)

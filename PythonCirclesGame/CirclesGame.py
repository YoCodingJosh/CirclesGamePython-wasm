# CirclesGame.py - Updates and draws the game and the menu.
# Created by Josh Kennedy on 18 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import TouchCircle

import MainMenu

import ClassicMode
import LightningMode

class CirclesGame():
    def __init__(self):
        self.showMainMenu = True
        self.mainMenu = MainMenu.MainMenu()
        self.classicMode = ClassicMode.ClassicMode()
        self.gameplayMode = 0
        self.lightningMode = LightningMode.LightningMode()

    def update(self, deltaTime):
        if (not self.classicMode.started and not self.classicMode.active and self.gameplayMode is 1):
            self.classicMode.startGame()

        # insert code to start lightning mode here
        if (self.gameplayMode is 2):
            pass

        if self.showMainMenu:
            self.mainMenu.update(deltaTime)

            self.showMainMenu = self.mainMenu.active
            self.gameplayMode = self.mainMenu.selectedGameMode
        else:
            if (self.gameplayMode is 1):
                # Classic mode.
                self.classicMode.update(deltaTime)
            if (self.gameplayMode is 2):
                # Lightning mode.
                self.lightningMode.update(deltaTime)

    def handleInput(self, event):
        if self.showMainMenu:
            self.mainMenu.handleInput(event)
        else:
            if (self.gameplayMode is 1):
                # Classic mode.
                self.classicMode.handleInput(event)
            if (self.gameplayMode is 2):
                # Lightning mode.
                self.lightningMode.handleInput(event)

    def draw(self, deltaTime):
        if self.showMainMenu:
            self.mainMenu.draw(deltaTime)
        else:
            if (self.gameplayMode is 1):
                # Classic mode.
                self.classicMode.draw(deltaTime)
            if (self.gameplayMode is 2):
                # Lightning mode.
                self.lightningMode.draw(deltaTime)

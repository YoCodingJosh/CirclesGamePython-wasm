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
        self.playGameCircleButton = CircleButton.CircleButton(100, 100, 100, Colors.Cyan, Colors.White, AssetCache.buttonFont)

    def update(self, deltaTime):
        return

    def handleInput(self, event):
        return

    def draw(self, deltaTime):
        return

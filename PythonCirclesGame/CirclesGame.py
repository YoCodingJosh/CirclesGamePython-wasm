# CirclesGame.py - Updates and draws the game and the menu.
# Created by Josh Kennedy on 18 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import TouchCircle
import Colors

class CirclesGame():
    def __init__(self):
        self.testCircle = TouchCircle.TouchCircle() # test circle, please ignore
        return

    def update(self, deltaTime):
        self.testCircle.update(deltaTime)
        return

    def handleInput(self, event):
        return

    def draw(self, deltaTime):
        self.testCircle.draw()

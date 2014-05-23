# CirclesGame.py - Updates and draws the game and the menu.
# Created by Josh Kennedy on 18 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import TouchCircle

class CirclesGame():
    def __init__(self):
        self.testCircle = TouchCircle.TouchCircle() # test circle, please ignore

    def update(self, deltaTime):
        self.testCircle.update(deltaTime)

    def handleInput(self, event):
        self.testCircle.handleInput(event)

    def draw(self, deltaTime):
        self.testCircle.draw()

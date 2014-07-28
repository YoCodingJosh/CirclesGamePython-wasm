# HelperAPI.py - Some helpful utilities so I won't have to type as much. :)
# Created by Josh Kennedy on 27 July 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import Rectangle

# Gets the window rectangle as a PyGame rect.
def getWindowRectangle():
    return pygame.display.get_surface().get_rect()

# Gets the window rectangle as our custom Rectangle.
def getWindowRectangleAsRectangle():
    return Rectangle.Rectangle(getWindowRectangle().x, getWindowRectangle().y, getWindowRectangle().width, getWindowRectangle().height)

# Gets the window surface from PyGame.
def getWindowSurface():
    return pygame.display.get_surface()

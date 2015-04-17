# HelperAPI.py - Some helpful utilities so I won't have to type as much. :)
# Created by Josh Kennedy on 27 July 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

import pygame
import datetime
import os

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

# Takes a screenshot as a BMP
def takeScreenshot():
    directory = os.path.dirname(os.path.realpath(__file__)) + "/Screenshots/"

    if not os.path.exists(directory):
        os.makedirs(directory)

    now = datetime.datetime.now()

    # PNG changes some of the colors, like the score text from red to green. wtf?!
    # BMP doesn't change anything, except the filesize will be bigger. :\

    filename = directory + ("Screenshot_%s%s%s%s%s%s.bmp" % (now.year, now.month, now.day, now.hour, now.minute, now.second))

    pygame.image.save(pygame.display.get_surface(), filename)

# Get the center of the screen.
def getCenterOfScreen():
    return (pygame.display.get_surface().get_rect().centerx, pygame.display.get_surface().get_rect().centery)

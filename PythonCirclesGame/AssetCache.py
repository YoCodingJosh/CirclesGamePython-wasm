# AssetCache.py - Loads assets into memory and keeps it there.
# Created by Josh Kennedy on 22 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

fpsFont = None
buttonFont = None

def startCache(resourceDirectory):
    global fpsFont, buttonFont

    fpsFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 20)
    buttonFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 30)

    return

def unloadCache():
    global fpsFont, buttonFont

    del fpsFont
    del buttonFont

    return

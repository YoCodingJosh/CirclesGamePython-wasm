# AssetCache.py - Loads assets into memory and keeps it there.
# Created by Josh Kennedy on 22 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

fpsFont = None
buttonFont = None
highPopSound = None
highPop2Sound = None
lowPopSound = None
badPopSound = None
jaguarSound = None
handCursor = None

def startCache(resourceDirectory):
    global fpsFont, buttonFont, highPopSound, highPop2Sound, lowPopSound, badPopSound, jaguarSound, handCursor

    fpsFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 20)
    buttonFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 30)

    highPopSound = pygame.mixer.Sound(resourceDirectory + "highpop.wav")
    highPop2Sound = pygame.mixer.Sound(resourceDirectory + "highpop2.wav")
    lowPopSound = pygame.mixer.Sound(resourceDirectory + "lowpop.wav")
    badPopSound = pygame.mixer.Sound(resourceDirectory + "badpop.wav")
    jaguarSound = pygame.mixer.Sound(resourceDirectory + "jaguar.wav")

    handCursorString = (
    "     XX         ",
    "    X..X        ",
    "    X..X        ",
    "    X..X        ",
    "    X..XXXXX    ",
    "    X..X..X.XX  ",
    " XX X..X..X.X.X ",
    "X..XX.........X ",
    "X...X.........X ",
    " X.....X.X.X..X ",
    "  X....X.X.X..X ",
    "  X....X.X.X.X  ",
    "   X...X.X.X.X  ",
    "    X.......X   ",
    "     X......X   ",
    "     XXXXXXXX   "
    )

    cursor, mask, = pygame.cursors.compile(handCursorString)
    handCursor = ((16, 16), (5, 1), cursor, mask)

    return

def unloadCache():
    global fpsFont, buttonFont, highPopSound, highPop2Sound, lowPopSound, badPopSound, jaguarSound, handCursor

    del fpsFont
    del buttonFont

    del highPopSound
    del highPop2Sound
    del lowPopSound
    del badPopSound
    del jaguarSound
    del handCursor

    return

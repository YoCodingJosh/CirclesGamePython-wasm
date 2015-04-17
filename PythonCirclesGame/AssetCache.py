# AssetCache.py - Loads assets into memory and keeps it there.
# Created by Josh Kennedy on 22 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

import pygame

fpsFont = None
buttonFont = None
scoreFont = None
highPopSound = None
highPop2Sound = None
lowPopSound = None
badPopSound = None
jaguarSound = None
handCursor = None
gameOverFont = None

screenResolution = (1280, 720)

def startCache(resourceDirectory):
    global fpsFont, buttonFont, scoreFont, highPopSound, highPop2Sound, lowPopSound, badPopSound, jaguarSound, handCursor, gameOverFont

    fpsFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 20)
    buttonFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 30)
    scoreFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 26)
    gameOverFont = pygame.font.Font(resourceDirectory + "Orbitron Medium.ttf", 42)

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

    # We need new music.
    #pygame.mixer.music.load(resourceDirectory + "BLEO_-_05_-_Sultry_Space_Showers.ogg")
    #pygame.mixer.music.play()

    return

def unloadCache():
    global fpsFont, buttonFont, scoreFont, highPopSound, highPop2Sound, lowPopSound, badPopSound, jaguarSound, handCursor, gameOverFont

    #pygame.mixer_music.stop()

    del fpsFont
    del buttonFont
    del scoreFont
    del gameOverFont

    del highPopSound
    del highPop2Sound
    del lowPopSound
    del badPopSound
    del jaguarSound
    del handCursor

    return

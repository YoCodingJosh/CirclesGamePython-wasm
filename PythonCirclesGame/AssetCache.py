# AssetCache.py - Loads assets into memory and keeps it there.
# Created by Josh Kennedy on 22 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

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
titleFont = None
sirklesLogo = None

screenResolution = (1280, 720)


def start_cache(resource_directory):
    global fpsFont, buttonFont, scoreFont, highPopSound, highPop2Sound, lowPopSound, badPopSound, jaguarSound, \
        handCursor, gameOverFont, titleFont, sirklesLogo

    fpsFont = pygame.font.Font(resource_directory + "Orbitron Medium.ttf", 20)
    buttonFont = pygame.font.Font(resource_directory + "Orbitron Medium.ttf", 30)
    scoreFont = pygame.font.Font(resource_directory + "Orbitron Medium.ttf", 26)
    gameOverFont = pygame.font.Font(resource_directory + "Orbitron Medium.ttf", 42)
    titleFont = pygame.font.Font(resource_directory + "freesansbold.ttf", 72)

    highPopSound = pygame.mixer.Sound(resource_directory + "highpop.wav")
    highPop2Sound = pygame.mixer.Sound(resource_directory + "highpop2.wav")
    lowPopSound = pygame.mixer.Sound(resource_directory + "lowpop.wav")
    badPopSound = pygame.mixer.Sound(resource_directory + "badpop.wav")
    jaguarSound = pygame.mixer.Sound(resource_directory + "jaguar.wav")

    hand_cursor_string = (
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

    cursor, mask, = pygame.cursors.compile(hand_cursor_string)
    handCursor = ((16, 16), (5, 1), cursor, mask)

    sirklesLogo = pygame.image.load(resource_directory + "SirklesLogo.png")
    sirklesLogo.convert_alpha()

    # We need new music!
    # pygame.mixer.music.load(resourceDirectory + "BLEO_-_05_-_Sultry_Space_Showers.ogg")
    # pygame.mixer.music.play()

    return


def unload_cache():
    global fpsFont, buttonFont, scoreFont, highPopSound, highPop2Sound, lowPopSound, badPopSound, jaguarSound, \
        handCursor, gameOverFont, titleFont, sirklesLogo

    # pygame.mixer_music.stop()

    del fpsFont
    del buttonFont
    del scoreFont
    del gameOverFont
    del titleFont

    del highPopSound
    del highPop2Sound
    del lowPopSound
    del badPopSound
    del jaguarSound
    del handCursor

    del sirklesLogo

    return

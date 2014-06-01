# PlayGameMenu.py - Where the player can select a game mode.
# Created by Josh Kennedy on 31 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import AssetCache

import Colors
import CircleButton

class PlayGameMenu():
    def __init__(self):
        self.classicModeCircleButton = CircleButton.CircleButton(700, 150, 100, Colors.Khaki, Colors.SteelBlue, AssetCache.buttonFont)

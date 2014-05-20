# TouchCircle.py - The circle that moves and supports being clicked on.
# Created by Josh Kennedy on 19 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame
import random

import Circle

# We're inheriting from Circle, to save some code and logic.
class TouchCircle(Circle.Circle):
    def __init__(self):
        self.radius = random.randint(50, 175)
        return super().__init__(random.randint(self.radius / 2, pygame.display.get_surface().get_rect().width - (self.radius / 2)), random.randint(self.radius / 2, pygame.display.get_surface().get_rect().height - (self.radius / 2)), self.radius)

    # TODO: Implement, lol.

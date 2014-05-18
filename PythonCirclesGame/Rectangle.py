# Rectangle.py - Rectangle stuff.
# Created by Josh Kennedy on 18 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

class Rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def left(self):
        return self.x

    def right(self):
        return self.width

    def top(self):
        return self.y
    
    def bottom(self):
        return self.height

    def isInside(self, vector):
        return (vector.x > self.left() and vector.x < self.right() and vector.y > self.top and vector.y < self.bottom)

    def draw(self, vector, color):
        pygame.draw.rect(pygame.display.get_surface(), color.getTuple(), (vector.x, vector.y))
        pygame.display.flip()

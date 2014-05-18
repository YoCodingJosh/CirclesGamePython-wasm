# Circle.py - Circle stuff.
# Created by Josh Kennedy on 17 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

class Circle:
    def __init__(x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, color):
        pygame.draw.circle(pygame.display.get_surface(), color.getTuple(), (self.x, self.y), self.radius)
        pygame.display.flip()
    
    def intersects(self, otherCircle):
        diff = ((self.x - otherCircle.x) * (self.x - otherCircle.x)) + ((self.y - otherCircle.y) * (self.y - otherCircle.y))
        return ((self.radius - otherCircle.radius) * (self.radius - otherCircle.radius) <= diff and diff <= (self.radius + otherCircle.radius) * (self.radius + otherCircle.radius))

    def isInside(self, vector):
        return (((vector.x - self.x) * (vector.x - self.x)) + ((vector.y - self.y) * (vector.y - self.y)) < (self.radius * self.radius))

# Circle.py - Circle stuff.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import HelperAPI

class Circle:
    """noun: a round plane figure whose boundary (the circumference) consists of points equidistant from a fixed point (the center)."""

    def __init__(self, x, y, radius = 0.0):
        self.x = x
        self.y = y
        self.radius = radius if radius != 0.0 else HelperAPI.scaleRadius()

    def draw(self, color, surface = None):
        if (surface == None):
            pygame.draw.circle(pygame.display.get_surface(), color.getTuple(), ((int)(self.x), (int)(self.y)), (int)(self.radius))
        else:
            pygame.draw.circle(surface, color.getTuple(), ((int)(self.x), (int)(self.y)), (int)(self.radius))
    
    def intersects(self, otherCircle):
        diff = ((self.x - otherCircle.x) * (self.x - otherCircle.x)) + ((self.y - otherCircle.y) * (self.y - otherCircle.y))
        return ((self.radius - otherCircle.radius) * (self.radius - otherCircle.radius) <= diff and diff <= (self.radius + otherCircle.radius) * (self.radius + otherCircle.radius))

    def isInside(self, vector):
        return (((vector.x - self.x) * (vector.x - self.x)) + ((vector.y - self.y) * (vector.y - self.y)) < (self.radius * self.radius))

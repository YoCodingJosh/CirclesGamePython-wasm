# Circle.py - Circle stuff.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import HelperAPI


class Circle:
    """
    noun: a round plane figure whose boundary (the circumference) consists of points
        equidistant from a fixed point (the center).
    """

    def __init__(self, x, y, radius = 0.0):
        self.x = x
        self.y = y
        self.radius = radius if radius != 0.0 else HelperAPI.scaleRadius()

    def draw(self, color, surface=None):
        if surface is None:
            pygame.draw.circle(pygame.display.get_surface(), color.getTuple(), (int(self.x), int(self.y)), int(self.radius))
        else:
            pygame.draw.circle(surface, color.getTuple(), (int(self.x), int(self.y)), int(self.radius))
    
    def intersects(self, other_circle):
        diff = ((self.x - other_circle.x) * (self.x - other_circle.x)) \
               + ((self.y - other_circle.y) * (self.y - other_circle.y))
        return (self.radius - other_circle.radius) * (self.radius - other_circle.radius)\
            <= diff <= (self.radius + other_circle.radius) * (self.radius + other_circle.radius)

    def isInside(self, vector):
        return ((vector.x - self.x) * (vector.x - self.x)) + ((vector.y - self.y) * (vector.y - self.y)) < (self.radius * self.radius)

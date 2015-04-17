# Vector2.py - 2D vector utilities.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

import math

class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitudeSquared(self):
        return dot(self, self)
    
    def magnitude(self):
        return math.sqrt(magnitudeSquared())

    def lengthSquared(self):
        return magnitudeSquared()

    def length(self):
        return magnitude()

    def dot(self, otherVector):
        return (self.x * other.x) + (self.y * other.y)

    def angle(self, other):
        return math.acos(dot(other) / (magnitude() * other.magnitude()))

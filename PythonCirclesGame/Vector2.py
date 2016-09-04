# Vector2.py - 2D vector utilities.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import math


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude_squared(self):
        return self.dot(self)

    def magnitude(self):
        return math.sqrt(self.magnitude_squared())

    def length_squared(self):
        return self.magnitude_squared()

    def length(self):
        return self.magnitude()

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def angle(self, other):
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

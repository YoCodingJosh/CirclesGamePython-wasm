# Color.py - Color utilities.
# Created by Josh Kennedy on 17 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import MathHelper

class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getTuple(self):
        return (self.r, self.g, self.b)

    def lerp(color1, color2, amount):
        return (MathHelper.lerp(color1.r, color2.r, amount), MathHelper.lerp(color1.g, color2.g, amount), MathHelper.lerp(color1.b, color2.b, amount))

# Color.py - Color utilities.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import MathHelper

class Color():
    """Basic RGBA Color object."""

    def __init__(self, r, g, b, a = None):
        self.r = r
        self.g = g
        self.b = b
        if a is not None:
            self.a = a
        else:
            self.a = 0

    def getTuple(self):
        if self.a is 0:
            return (self.r, self.g, self.b)
        else:
            return (self.r, self.g, self.b, self.a)

    def lerp(color1, color2, amount):
        if (color.a is not 0 and color2.a is not 0):
            return Color(MathHelper.lerp(color1.r, color2.r, amount), MathHelper.lerp(color1.g, color2.g, amount), MathHelper.lerp(color1.b, color2.b, amount), MathHelper.lerp(color1.a, color2.a, amount))
        else:
            return Color(MathHelper.lerp(color1.r, color2.r, amount), MathHelper.lerp(color1.g, color2.g, amount), MathHelper.lerp(color1.b, color2.b, amount))

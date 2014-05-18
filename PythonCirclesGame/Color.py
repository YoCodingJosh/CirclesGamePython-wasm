# Color.py - Color utilities.
# Created by Josh Kennedy on 17 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getTuple(self):
        return (self.r, self.g, self.b)

# MathHelper.py - Some helpful math utilities.
# Created by Josh Kennedy on 18 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import math

def lerp(value1, value2, amount):
    return value1 + ((value2 - value1) * amount)

def isPowerOfTwo(value):
    return (value > 0) and ((value & (value - 1)) == 0)

def toDegrees(radians):
    return radians * 57.295779513082320876798154814105

def toRadians(degrees):
    return degrees * 0.017453292519943295769236907684886

def clamp(value, min, max):
    if (value < low):
        return low
    else:
        if (value > high):
            return high
        else:
            return value

def nextPowerOfTwo(value):
    returnValue = 1

    while (returnValue < value):
        returnValue <<= 1

    return returnValue

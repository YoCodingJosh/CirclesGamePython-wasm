# HelperAPI.py - Some helpful utilities so I won't have to type as much. :)
# Created by Josh Kennedy on 27 July 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame
import pygame.gfxdraw

import datetime
import os
import math
import random

import Rectangle
import AssetCache
import Vector2


# Gets the window rectangle as a PyGame rect.
def getWindowRectangle():
    return pygame.display.get_surface().get_rect()


# Gets the window rectangle as our custom Rectangle.
def getWindowRectangleAsRectangle():
    return Rectangle.Rectangle(getWindowRectangle().x, getWindowRectangle().y, getWindowRectangle().width,
                               getWindowRectangle().height)


# Gets the window surface from PyGame.
def getWindowSurface():
    return pygame.display.get_surface()


# Takes a screenshot as a BMP
def takeScreenshot():
    directory = os.path.dirname(os.path.realpath(__file__)) + "/Screenshots/"

    if not os.path.exists(directory):
        os.makedirs(directory)

    now = datetime.datetime.now()

    # PNG changes some of the colors, like the score text from red to green. wtf?!
    # BMP doesn't change anything, except the file size will be bigger. :\

    filename = directory + ("Screenshot_%s-%s-%s_%s.%s.%s.%s.png" % (now.year, now.month, now.day, now.hour, now.minute,
                                                                     now.second, math.floor(now.microsecond / 1000)))

    temp_surface = pygame.display.get_surface()
    temp_surface.convert_alpha()

    pygame.image.save(temp_surface, filename)

    del temp_surface


# Get the center of the screen.
def getCenterOfScreen():
    return pygame.display.get_surface().get_rect().centerx, pygame.display.get_surface().get_rect().centery


# Plays a random pop sound.
def playRandomPopSound():
    num = random.randint(0, 2)
    if num is 0:
        AssetCache.highPopSound.play()
    elif num is 1:
        AssetCache.lowPopSound.play()
    elif num is 2:
        AssetCache.highPop2Sound.play()


def getAspectRatio():
    return AssetCache.screenResolution[0] / AssetCache.screenResolution[1]


def getTempScalar():
    return AssetCache.screenResolution[0] / 1280


def getScreenScalar():
    return getAspectRatio() * getTempScalar()


def scaleRadius(custom_size=0.0):
    if custom_size == 0.0:
        temp_radius = math.floor(random.uniform(0, 1) * 90) + 70
    else:
        temp_radius = custom_size

    temp_number = temp_radius / getAspectRatio()

    return temp_number * getScreenScalar()


def scaleVelocity(is_black=False):  # -> (x, y)
    signed_x_vel = -1 if random.randint(0, 1) == 1 else 1
    signed_y_vel = 1 if random.randint(0, 1) == 0 else -1

    if not is_black:
        temp_x_vel = int(math.floor(random.uniform(0, 1) * 16) + 1) * signed_x_vel
        temp_y_vel = int(math.floor(random.uniform(0, 1) * 16) + 1) * signed_y_vel
    else:
        temp_y_vel = 16 * signed_y_vel
        temp_x_vel = 16 * signed_x_vel

    temp_number_x = temp_x_vel / getAspectRatio()
    temp_number_y = temp_y_vel / getAspectRatio()

    return temp_number_x * getScreenScalar(), temp_number_y * getScreenScalar()


def scaleVelocityAsVector(is_black=False):  # -> Vector2
    vel = scaleVelocity(is_black)
    return Vector2.Vector2(vel[0], vel[1]) 


def scaleXPos(custom_value=0):
    return math.floor(random.uniform(0, 1) * AssetCache.screenResolution[0] + 1) if custom_value == 0 else custom_value


def scaleYPos(custom_value=0):
    return math.floor(random.uniform(0, 1) * AssetCache.screenResolution[1] + 1) if custom_value == 0 else custom_value


# make general function (color as parameter)
# from https://bitbucket.org/schlangen/pexdra
def supersampled_aacircle(surf, pos, r, i):
    temp_surf = pygame.Surface((r * 2 * i, r * 2 * i))
    temp_surf.fill((255, 255, 255))
    rect = pygame.draw.circle(temp_surf, (200, 0, 0), (r * i, r * i), r * i)
    rect.center = pos
    img = pygame.transform.smoothscale(temp_surf, (r * 2, r * 2))
    surf.blit(img, img.get_rect(center=rect.center).topleft)


# from https://bitbucket.org/schlangen/pexdra
def draw_aacircle(surf, color, pos, rad):
    pygame.gfxdraw.aacircle(surf, pos[0], pos[1], rad, color)
    pygame.gfxdraw.filled_circle(surf, pos[0], pos[1], rad, color)

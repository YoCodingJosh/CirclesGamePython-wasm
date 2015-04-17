# TextEffects.py - Some pretty cool text effects. (Warning: May decrease performance!)
# Created by Josh Kennedy on 2 August 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

import math
import random
import pygame

# I found these text effects here: http://pygame.org/fontcontest.shtml

# Cool electric strobe effect found on http://www.pygame.org/pcr/linefill_text/index.php
# Credit goes to David Clark
# Slightly modified to include a optional parameter to the init method.
class Linefill_Text():
    def __init__(self, text, font_obj, background_color, line_color, line_bg_color, numLines = 10):
        self.text = text
        self.font_obj = font_obj
        self.background_color = background_color
        self.numLines = numLines
        # find an appropriate colorkey for the text blit.
        if self.background_color != (0, 0, 0):
            colorkey = (0, 0, 0)
        else:
            colorkey = (255, 255, 255)
        self.line_color = line_color
        self.line_bg_color = line_bg_color
        self.text_mask_surface = font_obj.render(self.text, 0, colorkey, self.background_color)
        self.text_mask_surface.set_colorkey(colorkey)
        self.render_surface = pygame.Surface(self.text_mask_surface.get_size())
        # For speed, precache these values for use in __random_edge_pixel()
        self.width = self.text_mask_surface.get_width()
        self.height = self.text_mask_surface.get_height()

    def render(self):
        self.render_surface.fill(self.line_bg_color)
        for linenum in range(self.numLines):
            origin = self.__random_edge_pixel()
            dest = self.__random_edge_pixel()
            pygame.draw.line(self.render_surface, self.line_color, origin, dest)
        self.render_surface.blit(self.text_mask_surface, (0,0))
        return self.render_surface

    def __random_edge_pixel(self):
        # We bias in favour of vertical lines (75%), since text surfaces are
        # always wider than they are tall.
        if random.randrange(4) != 0:
            x = random.randrange(self.width)
            y = random.choice((0, self.height))
        else:
            x = random.choice((0, self.width))
            y = random.randrange(self.height)
        return (x, y)

# Really cool text wave effect found on http://www.pygame.org/pcr/wavey_text/index.php
# Credit goes to Pete Shinners
# Slightly modified to attempt to the fix clipping issues and an error.
class textWavey:
    def __init__(self, font, message, fontcolor, amount = 10):
        self.base = font.render(message, 0, fontcolor)
        self.steps = range(0, self.base.get_width(), 2)
        self.amount = amount
        self.size = self.base.get_rect().inflate(0, amount).size
        self.offset = 0.0
        
    def animate(self):
        s = pygame.Surface(self.size)
        height = self.size[1]
        self.offset += 0.5
        for step in self.steps:
            src = pygame.Rect(step, 0, 2, height)
            dst = src.move(0, math.cos(self.offset + step * 0.02) * self.amount)
            s.blit(self.base, dst, src)
        return s

# A simple drop shadow for text. Found on http://www.pygame.org/pcr/drop_shadow/index.php
# Credit belongs to Pete Shinners
def textDropShadow(font, message, offset, fontcolor, shadowcolor):
    base = font.render(message, 0, fontcolor)
    size = base.get_width() + offset, base.get_height() + offset
    img = pygame.Surface(size, pygame.SRCALPHA)
    base.set_palette_at(1, shadowcolor)
    img.blit(base, (offset, offset))
    base.set_palette_at(1, fontcolor)
    img.blit(base, (0, 0))
    return img

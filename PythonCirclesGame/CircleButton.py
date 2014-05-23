# CircleButton.py - A button that is a circle.
# Created by Josh Kennedy on 23 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import Circle
import Vector2

class CircleButton(Circle.Circle):
    def __init__(self, x, y, radius, hoverColor, textHoverColor, font):
        self.hoverColor = hoverColor
        self.active = True
        self.clickable = True
        self.hovering = False
        self.font = font
        self.textHoverColor = textHoverColor
        return super().__init__(x, y, radius)

    def setClickEvent(self, function):
        self.clickEvent = function

    def setButtonCaption(self, text, color):
        self.text = text

    def handleInput(self, event):
        if event == pygame.MOUSEMOTION:
            x, y = event.pos
            if (self.isInside(Vector2.Vector2(x, y)) and self.active):
                self.hovering = True
        elif event == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if (self.isInside(Vector2.Vector2(x, y)) and self.active and self.clickable):
                self.clickEvent()

    def draw(self, color, textColor):
        if (self.active):
            if (self.hovering):
                super().draw(self.hoverColor)
                self.font.render(self.text, textHoverColor.getTuple())
            else:
                super().draw(color)
                self.font.render(self.text, textColor.getTuple())

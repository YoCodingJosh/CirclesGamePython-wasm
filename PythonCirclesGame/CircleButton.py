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
        self.active = True
        self.hoverColor = hoverColor
        self.clickable = True
        self.hovering = False
        self.font = font
        self.textHoverColor = textHoverColor
        return super().__init__(x, y, radius)

    def update(self, deltaTime):
        return

    def handleInput(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if (self.clickable and self.active and self.isInside(Vector2.Vector2(x, y))):
                self.clickEvent()
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if (self.active and self.isInside(Vector2.Vector2(x, y))):
                self.hovering = True
            else:
                self.hovering = False

    def draw(self, color, textColor):
        if not self.active: return

        textSurface = None

        if self.hovering:
            super().draw(self.hoverColor)
            textSurface = self.font.render(self.text, True, self.textHoverColor.getTuple())
        else:
            super().draw(color)
            textSurface = self.font.render(self.text, True, textColor.getTuple())

        pygame.display.get_surface().blit(textSurface, (self.x - (textSurface.get_rect().width / 2), self.y - (textSurface.get_rect().height / 2)))

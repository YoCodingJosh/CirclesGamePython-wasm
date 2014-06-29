# BadCircle.py - Go sit in the corner! Shame on you. :(
# Created by Josh Kennedy on 28 June 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame
import random

import Circle
import Vector2
import Colors

class BadCircle(Circle.Circle):
    def __init__(self):
        # Set the radius and velocity.
        self.radius = random.randint(50, 125)
        self.velocity = Vector2.Vector2(random.randint(10, 12), random.randint(10, 12))

        # The bad circle is supposed to be black, so....
        self.color = Colors.Black

        # Randomly invert the velocity.
        if random.randint(0, 1) == 0: self.velocity.x *= -1
        if random.randint(0, 1) == 1: self.velocity.y *= -1

        # Set the center of the circle to be somewhere within the confines of the screen.
        self.x = random.randint(0, pygame.display.get_surface().get_rect().right)
        self.y = random.randint(0, pygame.display.get_surface().get_rect().bottom)

        # Set the entity to be active.
        self.active = True

        # Set the entity to be touchable.
        self.touchable = True

        # Set the on touch event to None as default.
        self.onTouch = None

        # Return a freshly initialized instance of the base class.
        return super().__init__(self.x, self.y, self.radius)

    def handleInput(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (self.touchable and self.active and self.isInside(Vector2.Vector2(x, y))):
                if self.onTouch is None:
                    self.active = False
                else:
                    self.onTouch(self)

    def update(self, deltaTime):
        if self.active:
            # Deal with the X component.
            if self.x + self.radius >= pygame.display.get_surface().get_rect().right:
                self.x = pygame.display.get_surface().get_rect().right - self.radius
                self.velocity.x *= -1
            elif self.x - self.radius <= pygame.display.get_surface().get_rect().left:
                self.x = pygame.display.get_surface().get_rect().left + self.radius
                self.velocity.x *= -1

            # Deal with the Y component.
            if self.y + self.radius >= pygame.display.get_surface().get_rect().bottom:
                self.y = pygame.display.get_surface().get_rect().bottom - self.radius
                self.velocity.y *= -1
            elif self.y - self.radius <= pygame.display.get_surface().get_rect().top:
                self.y = pygame.display.get_surface().get_rect().top + self.radius
                self.velocity.y *= -1

            # Translate across the screen.
            # PyGame doesn't like floats as a position.
            self.x += int((self.velocity.x * deltaTime) * 100)
            self.y += int((self.velocity.y * deltaTime) * 100)

    def draw(self):
        if not self.active: return
        return super().draw(self.color)

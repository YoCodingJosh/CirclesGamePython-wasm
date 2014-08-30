# TouchCircle.py - The circle that moves and supports being clicked on.
# Created by Josh Kennedy on 19 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame
import random

import Circle
import Vector2
import Colors
import Rectangle

# We're inheriting from Circle, to save some code and logic.
class TouchCircle(Circle.Circle):
    def __init__(self, boundary):
        # Set the boundary rectangle.
        self.boundary = boundary

        # Get the radius and velocity.
        self.radius = int((random.randint(0, int(self.boundary.width / 4 - (self.boundary.width / 7))) + int(self.boundary.width / 7)) / 2)
        self.velocity = Vector2.Vector2(random.randint(2, 8), random.randint(2, 8))

        # Randomly invert the velocity.
        if random.randint(0, 1) == 0: self.velocity.x *= -1
        if random.randint(0, 1) == 1: self.velocity.y *= -1

        # Set the center of the circle to be somewhere within the confines of the boundary.
        self.x = random.randint(0, boundary.right())
        self.y = random.randint(0, boundary.bottom())

        # Set the entity to be active.
        self.active = True

        # Set the entity to be touchable.
        self.touchable = True

        # Get the color.
        self.color = self.getColor()

        # Set the on touch event to None as default.
        self.onTouch = None

        # Return a freshly initialized instance of the base class.
        return super().__init__(self.x, self.y, self.radius)

    # Picks out a random color.
    def getColor(self):
        return {
            0 : Colors.Cyan,
            1 : Colors.ForestGreen,
            2 : Colors.Purple,
            3 : Colors.DarkOrange,
            4 : Colors.DeepPink,
            5 : Colors.SpringGreen,
            6 : Colors.Gold,
            7 : Colors.Khaki,
            8 : Colors.Tomato,
            9 : Colors.LightSalmon,
            10 : Colors.SlateGray,
            11 : Colors.Olive,
            12 : Colors.Maroon,
            13 : Colors.SteelBlue,
            14 : Colors.Red,
            15 : Colors.MediumPurple,
            16 : Colors.LawnGreen
        }[random.randint(0, 16)]

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
            if self.x + self.radius >= self.boundary.right():
                self.x = self.boundary.right() - self.radius
                self.velocity.x *= -1
            elif self.x - self.radius <= self.boundary.left():
                self.x = self.boundary.left() + self.radius
                self.velocity.x *= -1

            # Deal with the Y component.
            if self.y + self.radius >= self.boundary.bottom():
                self.y = self.boundary.bottom() - self.radius
                self.velocity.y *= -1
            elif self.y - self.radius <= self.boundary.top():
                self.y = self.boundary.top() + self.radius
                self.velocity.y *= -1

            # Translate across the screen.
            # PyGame doesn't like floats as a position.
            self.x += int((self.velocity.x * deltaTime) * 100)
            self.y += int((self.velocity.y * deltaTime) * 100)

    def draw(self, surface = None):
        if not self.active: return
        if (surface == None):
            return super().draw(self.color)
        else:
            return super().draw(self.color, surface)

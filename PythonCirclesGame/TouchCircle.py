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

# We're inheriting from Circle, to save some code and logic.
class TouchCircle(Circle.Circle):
    def __init__(self):
        # Get the radius and velocity.
        self.radius = random.randint(50, 125)
        self.velocity = Vector2.Vector2(random.randint(1, 5), random.randint(1, 5))

        # Randomly invert the velocity.
        if random.randint(0, 1) == 0: self.velocity.x *= -1
        if random.randint(0, 1) == 1: self.velocity.y *= -1

        # Set the center of the circle to be somewhere within the confines of the screen.
        self.x = random.randint(0, pygame.display.get_surface().get_rect().right)
        self.y = random.randint(0, pygame.display.get_surface().get_rect().bottom)

        # Set the entity to be active.
        self.active = True

        # TODO: Implement random color.

        # Return a freshly initialized instance of the base class.
        return super().__init__(self.x, self.y, self.radius)

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
            self.x += int((self.velocity.x * deltaTime) * 100)
            self.y += int((self.velocity.y * deltaTime) * 100)

    def draw(self):
        return super().draw(Colors.ForestGreen)

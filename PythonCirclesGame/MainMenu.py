# MainMenu.py - The game's main menu.
# Created by Josh Kennedy on 22 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache

import PlayGameMenu

import Colors
import Circle
import CircleButton
import GameInit
import TouchCircle
import BadCircle
import Vector2
import Rectangle
import HelperAPI

import random

class MainMenu():
    """Portal to different menus: "Play Game", "Options", or "Credits". This class also manages the switching between menus."""

    def __init__(self):
        # Create list of background circles.
        self.backgroundCircles = list()
        self.numberOfCircles = random.randint(1, 6)
        self.circleRenderSurface = pygame.Surface(AssetCache.screenResolution, pygame.SRCALPHA)
        self.circleRenderSurface.fill(Colors.TransparentWhite.getTuple())

        for i in range(self.numberOfCircles):
            circleObject = None
            if (random.randint(0, 5) == 3):
                circleObject = BadCircle.BadCircle(HelperAPI.getWindowRectangleAsRectangle())
            else:
                circleObject = TouchCircle.TouchCircle(HelperAPI.getWindowRectangleAsRectangle())

            circleObject.touchable = False
            circleObject.velocity = Vector2.Vector2(random.randint(3, 7), random.randint(3, 7))
            
            if random.randint(0, 1) == 0: circleObject.velocity.x *= -1
            if random.randint(0, 1) == 1: circleObject.velocity.y *= -1

            self.backgroundCircles.append(circleObject)

        self.playGameCircleButton = CircleButton.CircleButton(200, 150, 100, Colors.SpringGreen, Colors.Black, AssetCache.buttonFont)
        self.playGameCircleButton.text = "Play Game!"
        self.playGameCircleButton.clickEvent = self.playGame
        
        self.playMenuBackgroundCircle = Circle.Circle(200, 150, 100)

        self.playGameMenu = PlayGameMenu.PlayGameMenu(self)

        self.optionsCircleButton = CircleButton.CircleButton(450, 150, 100, Colors.DeepPink, Colors.Black, AssetCache.buttonFont)
        self.optionsCircleButton.text = "Options"
        self.optionsCircleButton.clickEvent = self.showOptions
        
        self.optionsMenuBackgroundCircle = Circle.Circle(450, 150, 100)

        self.creditsCircleButton = CircleButton.CircleButton(200, 400, 100, Colors.Purple, Colors.White, AssetCache.buttonFont)
        self.creditsCircleButton.text = "Credits"
        self.creditsCircleButton.clickEvent = self.showCredits

        self.creditsBackgroundCircle = Circle.Circle(200, 400, 100)

        self.exitCircleButton = CircleButton.CircleButton(450, 400, 100, Colors.MediumPurple, Colors.Black, AssetCache.buttonFont)
        self.exitCircleButton.text = "Exit Game"
        self.exitCircleButton.clickEvent = self.exitGame

        self.exitBackgroundCircle = Circle.Circle(450, 400, 100)

        self.backCircleButton = CircleButton.CircleButton(0, 0, 100, Colors.Olive, Colors.White, AssetCache.buttonFont)
        self.backCircleButton.active = False
        self.backCircleButton.text = "Back"
        self.backCircleButton.clickEvent = self.backToMainMenu

        self.transitionToMenu = False

        self.active = True

        # 0 is main menu, 1 is play game, 2 is options, 3 is credits, 4 is exit, and -1 is gameplay.
        self.selectedMenu = 0
        self.currentMenu = 0

        # 0 is none (menu)
        # 1 is classic
        # 2 is lightning
        # 3 is arcade
        self.selectedGameMode = 0

    def update(self, deltaTime):
        if not self.active: return

        for circle in self.backgroundCircles:
            circle.update(deltaTime)            

        self.playGameCircleButton.update(deltaTime)
        self.optionsCircleButton.update(deltaTime)
        self.creditsCircleButton.update(deltaTime)
        self.exitCircleButton.update(deltaTime)
        self.backCircleButton.update(deltaTime)

        # Play Game
        if (self.transitionToMenu and self.selectedMenu == 1 and self.playMenuBackgroundCircle.radius <= 1220):
            self.playMenuBackgroundCircle.radius += int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.selectedMenu == 1 and self.playMenuBackgroundCircle.radius >= 1220):
            self.exitCircleButton.active = False
            self.creditsCircleButton.active = False
            self.optionsCircleButton.active = False
            self.transitionToMenu = False
            self.currentMenu = 1
            self.backCircleButton.x = 450
            self.backCircleButton.y = 150
            self.backCircleButton.backgroundCircle.x = 450
            self.backCircleButton.backgroundCircle.y = 150
            self.backCircleButton.active = True

        # Options
        if (self.transitionToMenu and self.selectedMenu == 2 and self.optionsMenuBackgroundCircle.radius <= 1220):
            self.optionsMenuBackgroundCircle.radius += int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.selectedMenu == 2 and self.optionsMenuBackgroundCircle.radius >= 1220):
            self.exitCircleButton.active = False
            self.creditsCircleButton.active = False
            self.playGameCircleButton.active = False
            self.currentMenu = 2
            self.backCircleButton.x = 200
            self.backCircleButton.y = 400
            self.backCircleButton.backgroundCircle.x = 200
            self.backCircleButton.backgroundCircle.y = 400
            self.backCircleButton.active = True
            self.transitionToMenu = False

        # Credits
        if (self.transitionToMenu and self.selectedMenu == 3 and self.creditsBackgroundCircle.radius <= 1220):
            self.creditsBackgroundCircle.radius += int((6.66 * deltaTime) * 100)
        elif (self.transitionToMenu and self.selectedMenu == 3 and self.creditsBackgroundCircle.radius >= 1220):
            self.exitCircleButton.active = False
            self.optionsCircleButton.active = False
            self.playGameCircleButton.active = False
            self.currentMenu = 3
            self.backCircleButton.x = 200
            self.backCircleButton.y = 400
            self.backCircleButton.backgroundCircle.x = 200
            self.backCircleButton.backgroundCircle.y = 400
            self.backCircleButton.active = True
            self.transitionToMenu = False

        # Exit Game
        if (self.transitionToMenu and self.selectedMenu == 4 and self.exitBackgroundCircle.radius <= 1220):
            self.exitBackgroundCircle.radius += int((9 * deltaTime) * 100)
        elif (self.exitBackgroundCircle.radius >= 1220):
            GameInit.exitGame()

        # Transition from Play Game to Main Menu
        if (self.transitionToMenu and self.currentMenu == 1 and self.selectedMenu == 0 and self.playMenuBackgroundCircle.radius >= 100):
            self.playMenuBackgroundCircle.radius -= int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.currentMenu == 1 and self.selectedMenu == 0 and self.playMenuBackgroundCircle.radius <= 100):
            self.exitCircleButton.clickable = True
            self.creditsCircleButton.clickable = True
            self.optionsCircleButton.clickable = True
            self.playGameCircleButton.clickable = True
            self.playGameCircleButton.active = True
            self.currentMenu = 0
            self.transitionToMenu = False

        # Transition from Options Menu to Main Menu
        if (self.transitionToMenu and self.currentMenu == 2 and self.selectedMenu == 0 and self.optionsMenuBackgroundCircle.radius >= 100):
            self.optionsMenuBackgroundCircle.radius -= int((9 * deltaTime) * 100)
        elif (self.transitionToMenu and self.currentMenu == 2 and self.selectedMenu == 0 and self.optionsMenuBackgroundCircle.radius <= 100):
            self.exitCircleButton.clickable = True
            self.creditsCircleButton.clickable = True
            self.optionsCircleButton.clickable = True
            self.playGameCircleButton.clickable = True
            self.optionsCircleButton.active = True
            self.currentMenu = 0
            self.transitionToMenu = False

        # Transition from Credits to Main Menu
        if (self.transitionToMenu and self.currentMenu == 3 and self.selectedMenu == 0 and self.creditsBackgroundCircle.radius >= 100):
            self.creditsBackgroundCircle.radius -= int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.currentMenu == 3 and self.selectedMenu == 0 and self.creditsBackgroundCircle.radius <= 100):
            self.exitCircleButton.clickable = True
            self.creditsCircleButton.clickable = True
            self.optionsCircleButton.clickable = True
            self.playGameCircleButton.clickable = True
            self.creditsCircleButton.active = True
            self.currentMenu = 0
            self.transitionToMenu = False

        # Transition from Play Game to Gameplay Mode
        if (self.transitionToMenu and self.selectedMenu == -1 and self.selectedGameMode is not 0):
            self.playGameMenu.update(deltaTime)

        # Update the current menu (for button effects)
        if not self.transitionToMenu:
            if self.currentMenu is 1:
                self.playGameMenu.update(deltaTime)

    def handleInput(self, event):
        if not self.active: return

        self.playGameCircleButton.handleInput(event)
        self.optionsCircleButton.handleInput(event)
        self.creditsCircleButton.handleInput(event)
        self.exitCircleButton.handleInput(event)
        self.backCircleButton.handleInput(event)

        if (self.currentMenu == 1):
            self.playGameMenu.handleInput(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if (self.currentMenu is not 0 and not self.transitionToMenu):
                    self.backToMainMenu()

    def draw(self, deltaTime):
        if not self.active: return

        for circle in self.backgroundCircles:
            circle.draw()

        pygame.display.get_surface().blit(self.circleRenderSurface, (0, 0))

        self.playGameCircleButton.draw(Colors.Cyan, Colors.White)
        self.optionsCircleButton.draw(Colors.Gold, Colors.White)
        self.creditsCircleButton.draw(Colors.ForestGreen, Colors.Gold)
        self.exitCircleButton.draw(Colors.Tomato, Colors.Black)

        if (self.currentMenu == 1 or self.selectedMenu == 1):
            self.playMenuBackgroundCircle.draw(Colors.SpringGreen)
            if (not self.transitionToMenu or (self.transitionToMenu and self.selectedGameMode is not 0)):
                self.playGameMenu.draw(deltaTime)

        if (self.currentMenu == 2 or self.selectedMenu == 2):
            self.optionsMenuBackgroundCircle.draw(Colors.Gold)

        if (self.currentMenu == 3 or self.selectedMenu == 3):
            self.creditsBackgroundCircle.draw(Colors.Purple)

        if (self.selectedMenu == 4):
            self.exitBackgroundCircle.draw(Colors.Tomato)

        if ((self.currentMenu is not 0 or self.selectedMenu is not 0) and (self.currentMenu is not 4 or self.selectedMenu is not 4)):
            if (not self.transitionToMenu):
                self.backCircleButton.draw(Colors.White, Colors.Black)

    def playGame(self):
        AssetCache.highPopSound.play()
        self.transitionToMenu = True
        self.exitCircleButton.clickable = False
        self.creditsCircleButton.clickable = False
        self.optionsCircleButton.clickable = False
        self.playGameCircleButton.active = False
        self.selectedMenu = 1

    def showOptions(self):
        AssetCache.lowPopSound.play()
        print("options not implemented yet")
        self.selectedMenu = 2
        self.transitionToMenu = True
        self.exitCircleButton.clickable = False
        self.creditsCircleButton.clickable = False
        self.optionsCircleButton.active = False
        self.playGameCircleButton.clickable = False
    
    def showCredits(self):
        AssetCache.highPop2Sound.play()
        print("credits not yet implemented")
        self.selectedMenu = 3
        self.transitionToMenu = True
        self.creditsCircleButton.active = False
        self.exitCircleButton.clickable = False
        self.optionsCircleButton.clickable = False
        self.playGameCircleButton.clickable = False

    def backToMainMenu(self):
        self.selectedMenu = 0
        self.transitionToMenu = True
        AssetCache.badPopSound.play()
        self.playGameCircleButton.active = True
        self.optionsCircleButton.active = True
        self.creditsCircleButton.active = True
        self.exitCircleButton.active = True
        self.backCircleButton.active = False

    def exitGame(self):
        self.transitionToMenu = True
        AssetCache.badPopSound.play()
        self.exitCircleButton.active = False
        self.creditsCircleButton.clickable = False
        self.optionsCircleButton.clickable = False
        self.playGameCircleButton.clickable = False
        self.selectedMenu = 4

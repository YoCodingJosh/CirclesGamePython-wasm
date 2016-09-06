# CirclesGame.py - Updates and draws the game and the menu.
# Created by Josh Kennedy on 18 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import MainMenu

import SirklesLogoScreen

import ClassicMode
import LightningMode


class CirclesGame:
    def __init__(self):
        self.showSplashScreen = True
        self.showMainMenu = False
        self.mainMenu = MainMenu.MainMenu()
        self.splashScreen = SirklesLogoScreen.SirklesLogoScreen()
        self.classicMode = ClassicMode.ClassicMode(self.mainMenu)
        self.gameplayMode = 0
        self.lightningMode = LightningMode.LightningMode(self.mainMenu)

    def update(self, delta_time):
        if self.gameplayMode is 1 and not self.classicMode.started and not self.classicMode.active:
            self.classicMode.startGame()

        if self.gameplayMode is 2 and not self.lightningMode.started and not self.classicMode.active:
            self.lightningMode.startGame()

        if self.showSplashScreen:
            self.splashScreen.update(delta_time)
        elif self.showMainMenu:
            self.mainMenu.update(delta_time)

            self.showMainMenu = self.mainMenu.active
            self.gameplayMode = self.mainMenu.selectedGameMode
        else:
            if self.gameplayMode is 1:
                # Classic mode.
                self.classicMode.update(delta_time)
            if self.gameplayMode is 2:
                # Lightning mode.
                self.lightningMode.update(delta_time)

        # When the time is up for the splash screen, we can switch.
        self.showSplashScreen = self.splashScreen.waiting

        # Ensure that the splash screen is done showing and we have control of the menu.
        if not self.showSplashScreen and not self.mainMenu.active and not self.showMainMenu and self.gameplayMode == 0:
            self.showMainMenu = True
            self.mainMenu.active = True

        # In case, we need to go back to the menu from a gameplay mode.
        self.showMainMenu = self.mainMenu.active

    def handleInput(self, event):
        if self.showSplashScreen:
            self.splashScreen.handle_input(event)
        elif self.showMainMenu:
            self.mainMenu.handle_input(event)
        else:
            if self.gameplayMode is 1:
                # Classic mode.
                self.classicMode.handleInput(event)
            if self.gameplayMode is 2:
                # Lightning mode.
                self.lightningMode.handleInput(event)

    def draw(self, delta_time):
        if self.showSplashScreen:
            self.splashScreen.draw()
        elif self.showMainMenu:
            self.mainMenu.draw(delta_time)
        else:
            if self.gameplayMode is 1:
                # Classic mode.
                self.classicMode.draw(delta_time)
            if self.gameplayMode is 2:
                # Lightning mode.
                self.lightningMode.draw(delta_time)

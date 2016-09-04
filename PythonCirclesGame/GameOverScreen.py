# GameOverScreen.py - Displays the user's scores and the option to retry or quit.
# Created by Josh Kennedy on 23 July 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache
import CircleButton
import Colors
import TextEffects
import HelperAPI


class GameOverScreen:
    """The screen that is displayed to the user after they lose."""

    def __init__(self, gameplayMode, userScore, highScore, gameplayInstance):
        self.gameplayInstance = gameplayInstance
        self.gameplayMode = gameplayMode
        self.userScore = userScore
        self.highScore = highScore
        self.restartButton = \
            CircleButton.CircleButton(0, 0, 100, Colors.Purple, Colors.Gold, AssetCache.buttonFont, True)
        self.restartButton.text = "Restart"
        self.restartButton.clickEvent = self.restart_game
        self.menuButton = CircleButton.CircleButton(0, 0, 100, Colors.Khaki, Colors.Black, AssetCache.buttonFont, True)
        self.menuButton.text = "Menu"
        self.menuButton.clickEvent = self.gotoMenu
        self.active = True

        # Save time and pre-render the background and text surfaces.

        # Create surface with per-pixel alpha.
        self.background = pygame.Surface(AssetCache.screenResolution, pygame.SRCALPHA)
        self.background.fill(Colors.TransparentWhite.get_tuple())  # Fill with the transparent white color.

        # Figure out what to say.
        if userScore < highScore:
            self.text = "You didn't break your high score."
        elif userScore == highScore:
            self.text = "You've tied your high score. So close!"
        else:
            self.text = "Congratulations! You have a new high score!"

        # Render the message text.
        self.messageSurface = TextEffects.textDropShadow(AssetCache.gameOverFont, self.text, 5, Colors.Red.get_tuple(), Colors.DarkMediumGray.get_tuple())
        # self.messageSurface.set_colorkey(Colors.Black.getTuple())
        self.messageXPosition = HelperAPI.getCenterOfScreen()[0] - self.messageSurface.get_width() / 2
        self.messageYPosition = HelperAPI.getCenterOfScreen()[1] - self.messageSurface.get_height() / 2
        self.messageYPositionLowerLimit = self.messageYPosition - 163

        # Render the score text.
        score_text = "Your Score: " + str(userScore) + "       " + "High Score: " + str(highScore)
        self.scoreSurface = TextEffects.textDropShadow(AssetCache.scoreFont, score_text, 2, Colors.DarkOrange.get_tuple(), Colors.Black.get_tuple())
        self.scoreXPosition = HelperAPI.getCenterOfScreen()[0] - self.scoreSurface.get_width() / 2
        self.scoreYPosition = HelperAPI.getCenterOfScreen()[1] - self.scoreSurface.get_height() / 2
        self.scoreYPosition -= 50

        # Set up animations.
        self.transitionDone = False
        self.waitingTime = 80
        self.waiting = True

    def update(self, delta_time):
        if not self.active:
            return

        if not self.transitionDone:
            # We wait for roughly a second before we start the animations.
            if self.waitingTime > 0:
                self.waitingTime -= 1
            elif self.waitingTime <= 0:
                self.waiting = False

            if not self.waiting and not self.transitionDone:
                if self.messageYPosition > self.messageYPositionLowerLimit:
                    self.messageYPosition -= int((4 * delta_time) * 100)
                else:
                    self.transitionDone = True
                    self.restartButton.x = int(HelperAPI.getCenterOfScreen()[0] - (self.restartButton.radius / 2) - 100)
                    self.restartButton.y = int(self.scoreYPosition + self.restartButton.radius + 100)
                    self.menuButton.x = int(HelperAPI.getCenterOfScreen()[0] + (self.menuButton.radius / 2) + 100)
                    self.menuButton.y = int(self.scoreYPosition + self.menuButton.radius + 100)

        self.restartButton.update(delta_time)
        self.menuButton.update(delta_time)

    def handle_input(self, event):
        if not self.active:
            return

        if self.transitionDone:
            self.restartButton.handleInput(event)
            self.menuButton.handleInput(event)

    def draw(self):
        if not self.active:
            return

        # PyGame doesn't support alpha pixels in it's draw method, so I need to directly blit a surface to the screen.
        pygame.display.get_surface().blit(self.background, (0, 0))

        # Draw the text at the center of the screen.
        pygame.display.get_surface().blit(self.messageSurface, (self.messageXPosition, self.messageYPosition))

        if self.transitionDone:
            pygame.display.get_surface().blit(self.scoreSurface, (self.scoreXPosition, self.scoreYPosition))
            self.restartButton.draw(Colors.DeepPink, Colors.White)
            self.menuButton.draw(Colors.SteelBlue, Colors.White)

    def restart_game(self):
        self.active = False
        HelperAPI.playRandomPopSound()
        self.gameplayInstance.restartGame()

    def gotoMenu(self):
        AssetCache.badPopSound.play()
        self.gameplayInstance.mainMenu();

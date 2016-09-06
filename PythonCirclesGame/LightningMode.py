# LightningMode.py - Sorta like classic, but different background and thunder and lightning.
# Created by Josh Kennedy on 13 July 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache
import Colors
import HighScore


class LightningMode:
    def __init__(self, main_menu_instance):
        self.score = -1
        self.highScoreObject = HighScore.HighScore()
        self.highScore = self.highScoreObject.get_score("Lightning")
        self.started = False
        self.active = False
        self.mainMenuInstance = main_menu_instance

    def startGame(self):
        # Lights! Camera! ACTION!!
        self.score = 0
        self.started = True
        self.active = True

    def update(self, delta_time):
        _ = delta_time
        if not self.active:
            return
        pass

    def handleInput(self, event):
        _ = event
        if not self.active:
            return
        pass

    def draw(self, delta_time):
        _ = delta_time
        if not self.active:
            return

        pygame.display.get_surface().fill(Colors.Black.get_tuple())

        score_surface = AssetCache.scoreFont.render("Score: " + str(self.score), True, Colors.White.get_tuple())

        pygame.display.get_surface().blit(score_surface, (0, 0))

        placeholder_surface = AssetCache.buttonFont.render("I have no idea what to put here. Any ideas?", True,
                                                           Colors.Gold.get_tuple())

        render_x = pygame.display.get_surface().get_width() / 2 - placeholder_surface.get_rect().centerx
        render_y = pygame.display.get_surface().get_height() / 2 - placeholder_surface.get_rect().centery

        pygame.display.get_surface().blit(placeholder_surface, (render_x, render_y))

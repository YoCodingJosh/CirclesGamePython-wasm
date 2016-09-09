# SirklesLogoScreen.py - Shows the kick-ass logo.
# Created by Josh Kennedy on 5 September 2016
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache
import Colors


class SirklesLogoScreen:
    def __init__(self):
        self.waitingTime = 2.25
        self.waiting = True
        self.active = True
        self.copyrightSurface = AssetCache.copyrightFont.render("Copyright " + chr(169) + " 2015-2016 Sirkles LLC. "
                                                                                          "All rights reserved.", True,
                                                                Colors.Black.get_tuple())

    def update(self, delta_time):
        if not self.active:
            return

        if self.waiting:
            if self.waitingTime > 0:
                self.waitingTime -= delta_time
            elif self.waitingTime <= 0:
                self.waiting = False
                self.active = False

    def handle_input(self, event):
        if not self.active:
            return

        # Skip this screen.
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or
                                                                                      event.key == pygame.K_RETURN or
                                                                                      event.key == pygame.K_KP_ENTER or
                                                                                      event.key == pygame.K_SPACE)):
            self.waiting = False
            self.active = False

    def draw(self):
        if not self.active:
            return

        if self.waiting:
            pygame.display.get_surface().blit(AssetCache.sirklesLogo, ((pygame.display.get_surface().get_width() / 2)
                                                                       - (AssetCache.sirklesLogo.get_width() / 2),
                                                                       (pygame.display.get_surface().get_height() / 2)
                                                                       - (AssetCache.sirklesLogo.get_height() / 2)))

            # Draw Copyright notice.
            pygame.display.get_surface().blit(self.copyrightSurface, ((pygame.display.get_surface().get_width() / 2)
                                                                      - (self.copyrightSurface.get_width() / 2),
                                                                      (pygame.display.get_surface().get_height() / 2)
                                                                      + (AssetCache.sirklesLogo.get_height() / 2) +
                                                                      self.copyrightSurface.get_height() * 2))

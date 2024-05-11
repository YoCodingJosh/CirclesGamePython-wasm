# GameInit.py - Initializes PyGame and our game, and it contains the game loop.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import os
import sys
import platform
import random
import time

import pygame

import AssetCache

import Colors
import CirclesGame
import HelperAPI

# Our global loop condition, so we can exit the game from the menu.
gameDone = False

def wasm_initialize():
    print("Starting up...", end='')

    # Initialize PyGame TTF.
    pygame.font.init()

    # Initialize PyGame Mixer.
    pygame.mixer.pre_init(44100, -16, 1, 512)  # I don't know what these values mean, but they work best.

    # Initialize PyGame.
    pygame.init()

    # Initialize the window to 720p.
    screen = pygame.display.set_mode(AssetCache.screenResolution)
    pygame.display.set_caption("Pop a Dots", "Pop a Dots")

    # Clear the screen to white, and update it.
    screen.fill(Colors.White.get_tuple())
    pygame.display.flip()

    # Load and cache the assets.
    AssetCache.start_cache(os.path.dirname(os.path.realpath(__file__)) + "/Resources/")

    # aaaand we're done!
    print(" done!")

async def wasm_start():
    global gameDone

    import asyncio

    print("Initializing... ", end='')

    fps = 60  # Our FPS, obviously.
    fps_clock = pygame.time.Clock()  # The clock that's going to keep track of the current FPS.

    random.seed()

    circle_game = CirclesGame.CirclesGame()

    print(" done!\n")

    gameDone = False

    while not gameDone:
        await asyncio.sleep(0.0)
        fps_clock.tick(fps)

        # right now just force delta time to 1/60
        delta_time = 1.0 / 60.0

        # Clear the screen.
        pygame.display.get_surface().fill(Colors.White.get_tuple())

        # Update Game
        circle_game.update(delta_time)

        # Draw Game
        circle_game.draw(delta_time)

        pygame.display.flip()

        for event in pygame.event.get():
            circle_game.handleInput(event)

    print("Exiting game...", end='')

    # Stop all audio channels.
    pygame.mixer.stop()

    # Delete cache from memory.
    AssetCache.unload_cache()

    # Uninitialize PyGame Mixer.
    pygame.mixer.quit()

    # Uninitialize PyGame TTF.
    pygame.font.quit()

    # Uninitialize PyGame.
    pygame.quit()

    print(" done!")

    print("Bye!\n")


# Initializes PyGame and its subsystems.
def initialize():
    # Print the OS details.
    print("Detected OS: %s %s - %s\n" % (platform.system(), platform.release(), platform.version()))

    # Print the Python details.
    print("Detected Python Version: " + platform.python_implementation() + ' ' + platform.python_version())
    print("Using Python installed at: " + sys.executable + '\n')

    print("Starting up...", end='')

    # Set up environment variables for SDL (PyGame's subsystem).

    # Centers the screen.
    os.environ["SDL_VIDEO_CENTERED"] = '1'

    # Initialize PyGame TTF.
    pygame.font.init()

    # Initialize PyGame Mixer.
    pygame.mixer.pre_init(44100, -16, 1, 512)  # I don't know what these values mean, but they work best.

    # Initialize PyGame.
    pygame.init()

    # Initialize the window to 720p.
    screen = pygame.display.set_mode(AssetCache.screenResolution, vsync=1)
    pygame.display.set_caption("Pop a Dots", "Pop a Dots")

    # Set icon.
    pygame.display.set_icon(pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/Resources/Icon_Full.png"))

    # Clear the screen to white, and update it.
    screen.fill(Colors.White.get_tuple())
    pygame.display.flip()

    # Load and cache the assets.
    AssetCache.start_cache(os.path.dirname(os.path.realpath(__file__)) + "/Resources/")

    # aaaand we're done!
    print(" done!")

    # Print out graphics driver details, just so we know.
    print("\nDetected Graphics Driver: " + pygame.display.get_driver() + '\n')


# Kickstarts the game.
def start():
    global gameDone

    print("Initializing... ", end='')

    fps = 60  # Our FPS, obviously.
    fps_clock = pygame.time.Clock()  # The clock that's going to keep track of the current FPS.

    # Initialize and seed the pseudo-random number generator.
    random.seed()

    # Create an instance of the Circle Game.
    circle_game = CirclesGame.CirclesGame()

    print(" done!\n")

    last_frame = time.time()

    # Set the initial value to gameDone
    gameDone = False

    # game_title = "Pop a Dots"

    # The game loop.
    while not gameDone:
        # Calculate the fps, and delta time.
        fps_clock.tick_busy_loop(fps)
        current_frame = time.time()
        delta_time = current_frame - last_frame
        last_frame = current_frame

        # Clear the screen.
        pygame.display.get_surface().fill(Colors.White.get_tuple())

        # Update Game
        circle_game.update(delta_time)

        # Draw Game
        circle_game.draw(delta_time)

        # Update the window title.
        # pygame.display.set_caption("{} - {:6.3f} FPS".format(game_title, fpsClock.get_fps()))

        # Update the screen.
        pygame.display.flip()

        # Handle input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameDone = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F12:
                    HelperAPI.takeScreenshot()

            circle_game.handleInput(event)

    print("Exiting game...", end='')

    # Stop all audio channels.
    pygame.mixer.stop()

    # Delete cache from memory.
    AssetCache.unload_cache()

    # Uninitialize PyGame Mixer.
    pygame.mixer.quit()

    # Uninitialize PyGame TTF.
    pygame.font.quit()

    # Uninitialize PyGame.
    pygame.quit()

    print(" done!")

    print("Bye!\n")


def draw_fps_text(font, position, text, color, screen):
    text_surface = font.render(text, True, color.get_tuple())
    screen.blit(text_surface, (position.x, position.y))


def exit_game():
    global gameDone
    gameDone = True

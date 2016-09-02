Pop a Dots (Python)
===========

This is a ~~for-fun~~ **super serious** project to learn Python, real super serius bzns guise.

~~It's going to be a port of the C++ version to Python, with elements from the Android and iOS versions.~~

This is the offical PC version of Pop a Dots.

It will also be a testbed of features and functionality since Python is easy to use and prototype with.

##Prerequisites for building on Windows:
* Python 3.4.4
* PyGame 1.9.2 for Python 3.4 (https://bitbucket.org/pygame/pygame/downloads)
* Visual Studio 2015 with C++, C#, and Python Tools
* 64-bit Windows.
	* PyGame is only distributed in 64-bit form for Windows.

##Prerequisites for building on OS X:
* Intel Mac with OS X 10.7 or later (tested on 10.12) installed.
* Some free time (at least an hour) :smiley:
* Python 3.5.2 (installed via Homebrew, **NOT** the preinstalled Apple version)
* Ruby
* Latest Xcode (LLVM/clang recommended which is Xcode 4.2+, tested on Xcode 6 beta 6)
	* With Command Line Tools installed.
* Homebrew
* Latest XQuartz (X11 for OS X)
* Mercurial
* Git
* libpng, libjpeg, libogg, libvorbis built from source via Homebrew.
* SDL (built with X11 support, `--with-x11-driver`) via Homebrew.
* SDL_ttf, SDL_image built from source via Homebrew.
* SDL_mixer (built with Vorbis support, `--with-libvorbis`) from Homebrew
* PyGame built from source via pip.
* IntelliJ PyCharm IDE (Free!) recommended. :smile:

##Prerequisites for building on Linux (Ubuntu):
* Ubuntu 16.04
* Python 3.5.2
* Git
* PyCharm
* PyGame via (`pip3 install pygame`)
* Easy peasy.

## Instructions for OS X
* Install Homebrew.
* `brew install python3`
* `brew install pygame`
* `git clone <this repo>`
* boom

## Instructions for Linux
* Ensure git is installed.
* `sudo apt install python3-pip`
* `pip install pygame`
* `git clone <this repo>`
* done

OS X Notice: Retina displays causes really low FPS. AFAIK there is no solution for this.

##To Do:
* SDL2 implementation.
	* There is a experimental port of PyGame to SDL2 (https://github.com/renpy/pygame_sdl2).
* Finish implementing/porting basic Engine API. (In Progress, almost done!)
* Rewrite Windows launcher program to take advantage of Python's C/C++ API.
* Implement main menu. (In Progress, 95%)
	* Have button positions be dynamic, determined from screen size.
	* Need to add menu for Options.
	* Need to add Credits.
	* Need to finish the Play Game menu.
* Implement the basic gameplay mode, called Classic. 
	* 100% me thinks. At least with compatibility with Android version.
* Experiment with different gameplay modes (namely Lightning Mode)
* Look into porting Steamworks (Valve's Steam API for achievements and leaderboards) to Python.
	* Not my highest priority.

##What's done:
* Linux support.
* Game Over Screen
* Ported to OS X.
	* Includes a launcher script written in Bash that launches Python.
	* Bundled as a `.app`, so users can double click and not have to worry about Terminal and Python.
* Math API implemented (100%).
* Vector2 API partially implemented (What's necessary is added).
* List of Colors is up-to-date with iOS version (100%). :smiley:
* Color API 100% implemented (Alpha support implemented!).
* Circle mostly implemented (collision between circle and rectangle needs to be added).
* Saving and loading of high scores.
	* Also determining if a score was broken is also implemented.
* Added a border around classic mode.
	* It even animates!!! WOW!! :smile:
* FPS is displayed in the title bar.
	* The framerate is locked to 60 FPS.
* Rectangle API is partially implemented (collision stuff needed for both circles and other rectangles).
	* Collision is currently unnecessary for Rectangles
		* ~~Where do I even use Rectangles anyway?! :smiley:~~
			* As the border for the gameplay modes. :P
* Framework for different gameplay states (like main menu).
* TouchCircle 100% implemented.
* Bad Circle 100% implemented.
* Circle Buttons for Main Menu is 100% implemented, and tested. :smile:
* Main Menu 95% implemented.
	* Added play game and options buttons.
	* Added credits and exit game buttons.
	* Need to put things in the options and credits buttons.
* Asset cache architected and implemented.
	* This is really cool, because you don't have to reload resources like fonts or sounds every time an object goes out of scope.
		* This makes it run faster and use less memory.
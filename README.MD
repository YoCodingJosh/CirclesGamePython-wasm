Pop a Dots (Python)
===========

### Modernized build
This is a modernized build to take advantage of PyGame 2 and to fix a couple of small bugs.
You can check out the original code in the `master` branch.

Fixed in 0.2.0:
* Migrated from PyGame 1 -> PyGame 2
* Fixed screen tearing on screens > 60 FPS. It was really apparent when there were fast moving circles)
* Disabled play game menu options when transitioning back to main menu.
* Removed old PyGame 1 graphics driver init logic.
* Tweaked Python version gate keeper logic. All it checks for now is CPython 3.6 or newer, as that is the minimum version that PyGame supports.
* Fixed bug where it was impossible to go to Lightning mode after leaving Classic mode.

Start the game from `PythonCirclesGame.py`

This game is still abandoned and unsupported, just decided to fix it up to show friends and to brush up on my Python.

---

This is a ~~for-fun~~ **super serious** project to learn Python, real super serius bzns guise.

~~It's going to be a port of the C++ version to Python, with elements from the Android and iOS versions.~~

This is the offical PC version of Pop a Dots.

It will also be a testbed of features and functionality since Python is easy to use and prototype with.

## Prerequisites
* Python 3
* PyGame 2 installed (via `pip install pygame`)

##To Do:
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
* SDL2 support (in 2022 lmao)
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
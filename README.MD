CirclesGame (Python)
===========

This is a ~~for-fun~~ **super serious** project to learn Python, real super serius bzns guise.

It's going to be a port of the C++ version to Python, with elements from the Android and iOS versions.
It will also be a testbed of features and functionality since Python is easy to use and prototype with.

##Prerequisites for building on Windows:
* Python 3.3.5
* PyGame 1.9.2 for Python 3.3 (https://bitbucket.org/pygame/pygame/downloads)
* Visual Studio 2013 with C++, C#, and Python Tools

##To Do:
* Finish implementing/porting basic Engine API. (In Progress, almost done!)
* Implement main menu. (In Progress, 95%)
	* Have button positions be dynamic, determined from screen size.
	* Need to add menu for Options.
	* Need to add Credits.
	* Need to finish the Play Game menu.
* Implement the basic gameplay mode, called Classic. 
	* 100% me thinks. At least with compatibility with Android version.
* Finish Game Over Screen.
	* Show the user their score and their highest score.
	* Add the option of retrying or quitting.
* Experiment with different gameplay modes (namely Lightning Mode)
* Look into porting Steamworks (Valve's Steam API for achievements and leaderboards) to Python.
	* Not my highest priority.
* Look into cross-platform stuff.
	* Currently PyGame 1.9.2 for Python 3.3 is pre-built only for Windows.
		* So I will have to look into a shell script (Bash or Korn) installer that will grab the source and compile it for UNIX platforms (OS X, and Linux).
			* I tried building PyGame on OS X, it's a pain in the butt. You need SDL, SDL_image, SDL_ttf, SDL_mixer, libpng, libjpeg, smpeg, libvorbis, et al. already built to build PyGame. :sob:
		* That being said, I'll also have to write a launcher program or script to launch Python and the game.

##What's done:
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

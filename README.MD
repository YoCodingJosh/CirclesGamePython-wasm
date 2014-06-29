CirclesGame (Python)
===========

This is a ~~for-fun~~ **super serious** project to learn Python, real super serius bzns guise.

It's going to be a port of the C++ version to Python, with elements from the Android and iOS versions.

##Prerequisites for building:
* Python 3.3.5
* PyGame 1.9.2 for Python 3.3 (https://bitbucket.org/pygame/pygame/downloads)
* Visual Studio 2013 with Python Tools

##To Do:
* Finish implementing/porting basic Engine API. (In Progress, almost done!)
* Implement main menu. (In Progress, 95%)
	* ~~Implement other buttons.~~
	* Have button positions be dynamic, determined from screen size.
	* ~~Add some pizzazz to the menu like animations and sound effects.~~
		* Implemented button zooming to be background. It's really cool! :smile:
		* Implemented sound effects. `wow such pop`
	* Need to add menu for Options.
	* Need to add Credits.
	* Need to finish the Play Game menu.
* Implement the basic gameplay mode, called Classic. (Not sure if complete, but close though)
	* ~~I need to implement the bad circles.~~
	* ~~Look into data structures that can hold a dynamic amount of objects, akin to Java's `ArrayList`.~~
		* Python's `list` is perfect.

##What's done:
* Math API implemented (100%).
* Vector2 API partially implemented (What's necessary is added).
* List of Colors is up-to-date with iOS version (100%). :smiley:
* Color API 100% implemented (Alpha support implemented!).
* Circle mostly implemented (collision between circle and rectangle needs to be added).
* FPS is displayed.
	* The framerate is locked to 60 FPS.
* Rectangle API is partially implmented (collision stuff needed for both circles and other rectangles).
	* Collision is currently unnecessary for Rectangles
		* Where do I even use Rectangles anyway?! :smiley:
* Framework for different gameplay states (like main menu).
* TouchCircle 100% implemented.
* Bad Circle 100% implemented.
* Circle Buttons for Main Menu is 100% implemented, and tested. :smile:
* Main Menu 95% implemented.
	* Added play game and options buttons.
	* Added credits and exit game buttons.
* Asset cache architected and implemented.
	* This is really cool, because you don't have to reload resources like fonts or sounds every time an object goes out of scope.
		* This makes it run faster and use less memory.

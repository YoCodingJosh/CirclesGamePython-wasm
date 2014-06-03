CirclesGame (Python)
===========

This is a ~~for-fun~~ **super serious** project to learn Python, real super serius guise.

It's going to be a port of the C++ version to Python, with elements from the Android and iOS versions.

~~If/when I make significant progress, I'll look into porting to iOS/Android using Kivy (https://github.com/kivy/kivy)~~
**I misunderstood Kivy**, it isn't a Python compiler but a multi-touch friendly API for Python that runs on iOS and Android. The API is very different than PyGame, but it shouldn't be too hard to port later on down the road.

I found a Python-to-C++ compiler called Nuitka(http://nuitka.net/) that is statistically 258% faster than CPython (standard python). I find that this will be beneficial when/if we release. **Update (3 June 2014):** I looked into Nuitka, it's pretty fancy, but it's also really complex! I also don't know how well it would support PyGame, since PyGame is mixed code of C, Python, and Assembly. Probably not well.

##Prerequisites for building:
* Python 3.3
* PyGame 1.9.2 for Python 3.3 (https://bitbucket.org/pygame/pygame/downloads)
* Visual Studio 2013 with Python Tools

##To Do:
* Finish implementing/porting basic Engine API. (In Progress, almost done!)
* Implement main menu. (In Progress, 95%)
	* ~~Implement other buttons.~~
	* Have button positions be dynamic, determined from screen size.
	* ~~Add some pizzazz to the menu like animations and sound effects.~~
		* Implemented button zooming to be background. It's really cool! :smile:
	* Need to add menu for Options.
	* Need to add Credits.
	* Need to finish the Play Game menu.
* Implement the basic gameplay mode (Called Classic?)
	* I need to implement the bad circles.
	* Look into data structures that can hold a dynamic amount of objects, akin to Java's `ArrayList`.

##What's done:
* Math API implemented (100%).
* Vector2 API partially implemented (What's necessary is added).
* List of Colors is up-to-date with iOS version (100%). :smiley:
* Color API 100% implemented (Alpha support implemented!).
* Circle mostly implemented (collision between circle and rectangle needs to be added).
* FPS is displayed.
	* The framerate is locked to 60 FPS.
* Rectangle API is partially implmented (collision stuff needed for both circles and other rectangles).
* Framework for different gameplay states (like main menu).
* TouchCircle 100% implemented
* Circle Buttons for Main Menu is 100% implemented, and tested. :smile:
* Main Menu 95% implemented.
	* Added play game and options buttons.
	* Added credits and exit game buttons.
* Asset cache architected and implemented.
	* This is really cool, because you don't have to reload resources like fonts or sounds every time an object goes out of scope.
		* This makes it run faster and use less memory.

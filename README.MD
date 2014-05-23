CirclesGame (Python)
===========

This is a for-fun project to learn Python.

It's going to be a bare-bones port of the C++ version to Python, with some elements from the iOS version.

~~If/when I make significant progress, I'll look into porting to iOS/Android using Kivy (https://github.com/kivy/kivy)~~
**I misunderstood Kivy**, it isn't a Python compiler but a multi-touch friendly API for Python that runs on iOS and Android. The API is very different than PyGame, but it shouldn't be too hard to port later on down the road.

I found a Python-to-C++ compiler called Nuitka(http://nuitka.net/) that is statistically 258% faster than CPython (standard python). I find this will be beneficial when/if we release.

##Prerequisites for building:
* Python 3.3
* PyGame
* Visual Studio 2013 with Python Tools

##To Do:
* Finish implementing basic Engine API. (In Progress, almost done!)
* Have a circle bouncing on the screen. (Complete!)
	* From there, implement clicking on the circle. (Done!)
* Implement main menu. (In Progress, 15%)

##What's done:
* Math API implemented (100%).
* Vector2 API partially implemented (What's necessary is added).
* List of Colors is up-to-date with iOS version (100%). :smiley:
* Color API 100% implemented (Needs color alpha support, but not necessary).
* Circle mostly implemented (collision between circle and rectangle needs to be added).
* FPS is displayed.
	* The framerate is locked to 60 FPS.
* Rectangle API is partially implmented (collision stuff needed for both circles and other rectangles).
* Basic abstraction for game drawing and updating.
* TouchCircle 100% implemented
* Circle Button for Main Menu is 100% implemented, but untested.
* Main Menu skeleton created.
* Asset cache architected and implemented.
	* This is really cool, because you don't have to reload resources like fonts or sounds everytime an object goes out of scope.
		* This makes it run faster and use less memory.

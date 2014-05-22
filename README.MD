CirclesGame (Python)
===========

This is a for-fun project to learn Python.

It's going to be a bare-bones port of the C++ version to Python, with some elements from the iOS version.

~~If/when I make significant progress, I'll look into porting to iOS/Android using Kivy (https://github.com/kivy/kivy)~~
**I misunderstood Kivy**, it isn't a Python compiler but a multi-touch friendly API for Python that runs on iOS and Android. The API is very different than PyGame, but it shouldn't be too hard to port later on down the road.

##Prerequisites for building:
* Python 3.3
* PyGame
* Visual Studio 2013 with Python Tools

##To Do:
* Finish implementing basic Engine API. (In Progress, almost done!)
* Have a circle bouncing on the screen. (Complete!)
	* From there, implement clicking on the circle. (Done!)
* Implement main menu. (In Progress)

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

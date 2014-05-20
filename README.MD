CirclesGame (Python)
===========

This is a for-fun project to learn Python.

It's going to be a bare-bones port of the C++ version to Python, with some elements from the iOS version.

~~If/when I make significant progress, I'll look into porting to iOS/Android using Kivy (https://github.com/kivy/kivy)~~
**I misunderstood Kivy**, it isn't a Python compiler but a muli-touch friendly API for Python that runs on iOS and Android. The API is very different than PyGame, but it shouldn't be too hard to port later on down the road.

##Prerequisites for building:
* Python 3.3
* PyGame
* Visual Studio 2013 with Python Tools

##To Do:
* Finish implementing basic Engine API.
* Have a circle bouncing on the screen.
	* From there, implement clicking on the circle.
* Implement main menu.

##What's done:
* Math API implemented.
* Vector2 API partially implemented.
* List of Colors is up-to-date with iOS version.
* Color API partially implemented.
* Circle mostly implemented.
* FPS is displayed.
	* The framerate is locked to 60 FPS.
* Rectangle API is partially implmented
* Basic abstraction for game drawing and updating.

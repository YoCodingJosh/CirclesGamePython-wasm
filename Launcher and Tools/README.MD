Launcher and Tools
========

## Launcher

The launcher is a really cool C++ program that manages the launch and termination of the Python process that runs the game.

### What it does (in a nutshell):
* Creates a mutex.
	* If it succeeds in creating it then it means that the launcher isn't already running.
	* If it fails to create the mutex, then it means the launcher is already running.
	* A mutex is best described here: http://en.wikipedia.org/wiki/Mutual_exclusion (because frankly, I don't know what it is. :smile:)
* Initialize the paths to the main Python file (PythonCirclesGame.py) and the Python EXE (python33.exe).
	* It also checks to make sure that they exist.
* Initialize the shell execution data structure by passing in the parameters and directories.
* Execute Python
	* Then it hides the console window.
* Wait for the game to complete.
* Exit

It does more than just that, such as if the parent daemon gets terminated, then the Python process gets terminated too.

It's really advanced stuff though, but it was really fun to work on! :smiley:

## Compiler

This isn't really a "compiler" in the literal sense, but it invokes the Python compiler and compiles the Python scripts to bytecode.
It then copies the Resources folder to where the bytecode is compiled to. (This is the internal structure of the Game folder.)

This is written in about 100 lines of C# code.

### FYI

You'll also see a project called CMDHIDE, that's the predecessor to GAME. It just handles the closing and showing of the command prompt from a batch file. The reason I moved from a batch file to a C++ program was that I needed to ensure only one instance of the game can be run (I noticed some audio issues with running more than one instance), and having an icon.

The final distribution of the files will be in this structure:

* ROOT FOLDER (eg. C:\Program Files (x86)\Sirkles\WOW SUCH POP\)
	* Game
		* Where all of the compiled bytecode and resources go.
	* Python
		* Where the standalone Python 3.3.5 environment resides.
	* GAME.EXE
		* The launcher executable.

This is the best organization for all of the files, IMO.
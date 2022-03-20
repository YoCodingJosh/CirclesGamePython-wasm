# PythonCirclesGame.py - Entry point to application.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import GameInit

import platform
import sys

__version__ = "0.2.0"


# We want to check that we're running CPython 3.6 or newer and not anything older or not CPython.
def python_version_check():
    # Grab the Python version.
    first = int(platform.python_version_tuple()[0])
    second = int(platform.python_version_tuple()[1])

    # Ensure that they're using the CPython implementation
    if platform.python_implementation() is not "CPython":
        print("You must use the CPython implementation of Python!\n\n")
        sys.exit(1)

    # Detect Python version, so we can alert the user if they're using an older version.
    if first < 3 or second < 6:
        print("You need at least Python 3.6 to play this game!\n\n")
        sys.exit(2)


# Our main function.
def main():
    python_version_check()

    print("Pop a Dots Version %s\nCopyright (C) 2014-2016 Sirkles LLC\n" % __version__)

    GameInit.initialize()
    GameInit.start()

# Our actual entry point.
if __name__ == "__main__":
    main()

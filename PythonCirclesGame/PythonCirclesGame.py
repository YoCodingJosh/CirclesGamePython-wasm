# PythonCirclesGame.py - Entry point to application.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

import GameInit

import platform
import sys

version = "0.0.666"

# We want to check that we're running CPython 3.3.5 and not anything older or not CPython.
def pythonVersionCheck():
    # Grab the Python version.
    first = int(platform.python_version_tuple()[0])
    second = int(platform.python_version_tuple()[1])
    third = int(platform.python_version_tuple()[2])

    # Ensure that they're using the CPython implementation
    if (platform.python_implementation() is not "CPython"):
        print("You must use the CPython implementation of Python!\n\n")
        sys.exit(1)

    # Detect Python version, so we can alert the user if they're using an older version.
    if (first < 3 or second < 3):
        print("You need Python 3.3 to play this game!\n\n")
        sys.exit(2)

    # We need to additionally warn the user if they're using an older version of Python 3.3 to ensure the best experience.
    if (first is 3 and second is 3 and third < 3):
        print("It is EXTREMELY recommended that you use the latest version of Python 3.3 (which is 3.3.5) to run this game!\n\n")

    # We also need to warn the user if they're using a newer version, because we can't guarantee it will work.
    if (first > 3 or second > 3):
        print("It is recommended that you use Python 3.3 to play this game, as we can't guarantee the stability and performance in newer versions.\n\n")

# Our main function.
def main():
    pythonVersionCheck()

    print("Pop a Dots (Python) Version %s\nCopyright (C) 2015 Sirkles LLC\n" % version)

    GameInit.initialize()
    GameInit.start()

# Our actual entry point.
if __name__ == "__main__":
    main()

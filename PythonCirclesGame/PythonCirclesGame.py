# PythonCirclesGame.py - Entry point to application.
# Created by Josh Kennedy on 17 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import GameInit

version = "0.0.1"

# Our main function.
def main():
    print("CirclesGame (Python Version) v%s\nCopyright (C) 2014 Chad Jensen and Josh Kennedy\n" % version)

    GameInit.initialize()
    GameInit.start()

# Our actual entry point.
if __name__ == "__main__":
    main()

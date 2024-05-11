# main.py - the real entry point to the application.
# Created by Josh Kennedy on 10 May 2024
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC
# Copyright 2024 Josh Kennedy

import PythonCirclesGame

import sys

if __name__ == "__main__":
    if sys.platform == "emscripten":
        import asyncio
        asyncio.run(PythonCirclesGame.PythonCirclesGame().entry_point())
    else:
        PythonCirclesGame.PythonCirclesGame().entry_point()

#!/usr/bin/python3

import compileall
import io
import os


if __name__ == "__main__":
    print("Compiling Pop a Dots...")
    compileall.compile_dir("./PythonCirclesGame/", force=1)

    # Python seems a bit dumb in this respect, the files extensions are renamed and are unusable.
    # We'll need to rename these files from .cpython-35.pyc to just .pyc.

    # First, we'll copy it to a new folder called bin

    pass

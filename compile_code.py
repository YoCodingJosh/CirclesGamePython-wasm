#!/usr/bin/python3

# compile_code.py - Compiles Python code.
# Created by Josh Kennedy on 8 September 2016
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import compileall
import io
import os
import shutil


class Util:
    """
    Utility class.
    """

    @staticmethod
    def copy_files(src_dir, dest_dir, file_ext='*'):
        src_files = os.listdir(src_dir)

        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)

        for file_name in src_files:
            if file_ext is '*' or file_name.endswith(file_ext):
                full_file_name = os.path.join(src_dir, file_name)
                if os.path.isfile(full_file_name):
                    shutil.copy(full_file_name, dest_dir)

            pass


class Compile:
    """
    Compiles the Python source code to bytecode.
    """

    @staticmethod
    def start():
        print("Compiling Pop a Dots...")

        # First copy all of the Python files to ./bin/
        Util.copy_files("./PythonCirclesGame/", "./bin/", '.py')

        # Then compile all.
        compileall.compile_dir("./bin/", force=1)

        # Python seems a bit dumb in this respect, the files extensions are renamed and are unusable.
        # We'll need to rename these files from .cpython-35.pyc to just .pyc.

        pass


class Linux:
    """
    Compiles a Debian package for Debian/Ubuntu.
    """

    pass


class Mac:
    """
    Compiles a .app application bundle for macOS / OS X.
    """

    pass


class Windows:
    """
    Compiles an exe for Windows (not UWP!)
    """

    pass


if __name__ == "__main__":

    Compile.start()

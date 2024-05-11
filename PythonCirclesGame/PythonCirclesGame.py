# PythonCirclesGame.py - Entry point to application.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import GameInit

__version__ = "0.2.0"

class PythonCirclesGame():
    def normal_entry_point(self):
        print("Pop a Dots Version %s\nCopyright (C) 2014-2016 Sirkles LLC\n" % __version__)

        GameInit.initialize()
        GameInit.start()

    async def wasm_entry_point(self):
        print("Pop a Dots Version (WebAssembly) %s\nCopyright (C) 2014-2016 Sirkles LLC\nCopyright (C) 2024 Josh Kennedy\n" % __version__)

        GameInit.initialize()
        GameInit.start()

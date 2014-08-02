# HighScore.py - New high score. Woo hoo!! :D
# Created by Josh Kennedy on 30 June 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import os

class HighScore():
    def setScore(self, gameplay, score):
        gameplayMode = gameplay
        directory = os.path.dirname(os.path.realpath(__file__)) + "/Scores/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + gameplay + ".cgs"
        file = open(filename, "w")
        newScore = hex(int((score * 6 / 2) + 100))
        file.write(str(newScore))
        file.write('\n')
        file.close()

    def getScore(self, gameplay):
        gameplayMode = gameplay
        directory = os.path.dirname(os.path.realpath(__file__)) + "/Scores/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + gameplay + ".cgs"

        try:
            file = open(filename, "r")
            scoreString = file.readline()
            file.close()
        except FileNotFoundError:
            # If there isn't a score file, then there isn't a score.
            return 0
        except io.UnsupportedOperation:
            # The file is empty or something else... :\
            file.close()
            return 0

        if (scoreString is None or scoreString is ''):
            return 0
        else:
            try:
                return int((int(scoreString, 0) - 100) * 2 / 6)
            except ValueError:
                # The contents of the file can not be parsed to an integral value.
                return 0

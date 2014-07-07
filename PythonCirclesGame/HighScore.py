# HighScore.py - New high score. Woo hoo!! :D
# Created by Josh Kennedy on 30 June 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

class HighScore():
    def setScore(self, gameplay, score):
        gameplayMode = gameplay
        filename = gameplay + ".cgs"
        file = open(filename, "w")
        file.write(str(score))
        file.write('\n')
        file.close()

    def getScore(self, gameplay):
        gameplayMode = gameplay
        filename = gameplay + ".cgs"

        try:
            file = open(filename, "r")
            scoreString = file.readline()
            file.close()
        except FileNotFoundError:
            return 0
        except io.UnsupportedOperation:
            file.close()
            return 0

        if (scoreString is None or scoreString is ''):
            return 0
        else:
            return int(scoreString)

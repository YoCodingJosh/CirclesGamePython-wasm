# HighScore.py - New high score. Woo hoo!! :D
# Created by Josh Kennedy on 30 June 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import os
import io

# Cypher Algorithm:
# output = (((userScore * 6 / 2) + 100) * 7) + (1, if score is even, otherwise 0)
#
# userScore is the score that the user got. [0, Infinity)
# 6 is the non-prime multiplier constant, preferably even.
# 2 is the LCM of the non-prime multiplier constant.
# 100 is a constant, can be any value.
# 7 is the prime multiplier constant, must not be 2 (especially if the non-prime multiplier constant is even).
#
# We conditionally add 1 if the score is even.

# It would be very fun to implement a simple RSA public key encrypter on top of this.


class HighScore:
    @staticmethod
    def set_score(gameplay, score):
        directory = os.path.dirname(os.path.realpath(__file__)) + "/Scores/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + gameplay + ".shsf"  # Sirkles High Score File = SHSF
        file = open(filename, "w")
        new_score = hex(int(((score * 6 / 2) + 100) * 7 + (1 if score % 2 is 0 else 0)))
        file.write(str(new_score))
        file.write('\n')
        file.close()

    @staticmethod
    def get_score(gameplay):
        directory = os.path.dirname(os.path.realpath(__file__)) + "/Scores/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + gameplay + ".shsf"

        # Fix use before assignment warnings.
        file = None

        try:
            file = open(filename, "r")
            score_string = file.readline()
            file.close()
        except FileNotFoundError:
            # If there isn't a score file, then there isn't a score.
            return 0
        except io.UnsupportedOperation:
            # The file is empty or something else... :\
            file.close()
            return 0

        if score_string is None or score_string is '':
            return 0
        else:
            try:
                return int(((int(score_string, 0) / 7) - 100) * 2 / 6)
            except ValueError:
                # Fall through if it resolves with a remainder.
                # This may be a hack, but idgad. :P
                try:
                    return int((((int(score_string, 0) - 1) / 7) - 100) * 2 / 6)
                except ValueError:
                    # The contents of the file can not be parsed to an integral value.
                    return 0

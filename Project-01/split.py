#!/usr/bin/env python

"""
A filter that splits 1 word per line and strips special characters.
"""

import fileinput


def process(line):
    for word in line.split():
           print(word.strip(',.!?\'_(){}[]-–`~&*;:/"" ')) 


for line in fileinput.input():
    process(line)

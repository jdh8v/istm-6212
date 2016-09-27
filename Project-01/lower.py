#!/usr/bin/env python

"""
A filter that takes input text and converts to lowercase.
"""

import fileinput


def process(line):
	print(line.lower())


for line in fileinput.input():
    process(line)

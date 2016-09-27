#!/usr/bin/env python

"""
A filter that removes stop words.
"""

import fileinput
stop_words = ['and', 'the', 'to', 'a', 'of', 'her', 'i', 'in', 'it', 'she']

def process(line):
    """For each line of input, _____."""
    words = line.split()
    for word in words:
        if word not in stop_words:
            print(word)

for line in fileinput.input():
    process(line)

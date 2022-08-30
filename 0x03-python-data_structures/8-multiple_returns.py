#!/usr/bin/python3

def multiple_returns(sentence):
    size = len(sentence)
    if not sentence:
        return (size, None)
    return (size, sentence[0])

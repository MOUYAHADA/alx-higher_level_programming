#!/usr/bin/python3
def multiple_returns(sentence):
    """Multiple returns"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

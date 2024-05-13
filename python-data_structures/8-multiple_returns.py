#!/usr/bin/python3
def multiple_returns(phrase):
    if len(phrase) == 0:
        return 0, None
    else:
        return len(phrase), phrase[0]

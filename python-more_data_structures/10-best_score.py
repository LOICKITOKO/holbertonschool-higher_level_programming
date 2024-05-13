#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_score = max(a_dictionary.values())
    best_students = [key for key, value in a_dictionary.items() if value == max_score]

    return best_students[0]

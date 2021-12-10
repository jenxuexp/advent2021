import os
import numpy as np
import copy
from scipy import ndimage
import matplotlib.pyplot as plt

def parse_rules(fname):
    bracket_list = []
    for line in open(fname):
        print(line)
        line = line.strip()
        brackets = [bracket for bracket in line]
        bracket_list.append(brackets)
    return bracket_list

def main():
    bracket_list = parse_rules('input.txt')
    lefts = {'(': ')', '[': ']', '{': '}', '<': '>'}
    rights = {')': '(', ']': '[', '}': '{', '>': '<'}
    right_score = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for bracket in bracket_list:
        bracket_holder = []
        cur_score = 0
        found_corrupted = False
        for bracket_val in bracket:
            if bracket_val in lefts:
                bracket_holder.append(bracket_val)
            else:
                last_value = bracket_holder.pop()
                if rights[bracket_val] != last_value:
                    print('Found corrupted line, discarding')
                    found_corrupted = True
                    break
        while len(bracket_holder) > 0 and not found_corrupted:
            cur_score = cur_score*5 + right_score[lefts[bracket_holder.pop()]]
        if cur_score > 0:
            scores.append(cur_score)
    scorted = sorted(scores)
    print('all incomplete lines: ')
    print(scorted)
    print("Final extra syntax score: ", scorted[len(scorted)//2])



if __name__== main():
    main()
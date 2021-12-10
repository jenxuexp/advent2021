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
    lefts = ['(', '[', '{', '<']
    rights = {')': '(', ']': '[', '}': '{', '>': '<'}
    right_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for bracket in bracket_list:
        bracket_holder = []
        for bracket_val in bracket:
            if bracket_val in lefts:
                bracket_holder.append(bracket_val)
            else:
                last_value = bracket_holder.pop()
                if rights[bracket_val] != last_value:
                    score += right_score[bracket_val]
    print("Final syntax score: ", score)



if __name__== main():
    main()
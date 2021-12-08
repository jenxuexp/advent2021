import os
import numpy as np
import copy


def parse_rules(fname):
    code_vals = []
    for line in open(fname):
        print(line)
        line = line.strip()
        code_digits = line.split('|')[1].strip()
        code_vals.append([str_val for str_val in code_digits.split()])
    return code_vals

def main():
    num_unique = 0
    code_vals = parse_rules('input.txt')
    for code_val in code_vals:
        for str_val in code_val:
            if len(str_val) in [2, 3, 4, 7]:
                num_unique += 1
    print('Number of unique numbers: ', num_unique)

if __name__== main():
    main()
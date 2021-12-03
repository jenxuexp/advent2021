import os
import numpy as np


def parse_line(line):
    line = line.strip()
    list_line = [int(digit) for digit in line]
    return list_line

def parse_rules(fname):
    digits_list = []
    for line in open(fname):
        digits_list.append(parse_line(line))
    return np.array(digits_list)

def main():
    digits_array = parse_rules('day3_input.txt')
    print(digits_array.shape[1])
    little_endian_array = np.fliplr(digits_array)
    gamma_value = 0
    epsilon_value = 0
    for col_num in range(digits_array.shape[1]):
        col_sum = np.sum(little_endian_array[:, col_num])
        if col_sum >= digits_array.shape[0]/2:
            gamma_value += 2**col_num
        else:
            epsilon_value += 2**col_num
    print('Gamma: ', gamma_value)
    print('Epsilon: ', epsilon_value)
    print('Product: ', gamma_value*epsilon_value)


if __name__== main():
    main()
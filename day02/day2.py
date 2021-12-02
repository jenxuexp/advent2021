import numpy as np
import os


# def get_input_as_list(filepath):
#     with open(filepath) as f:
        
# 	    input = [line.strip() for line in f.readlines()]
#     return input


def parse_line(line):
    horizontal_dict = {'forward': 1, 'up': 0, 'down': 0}
    vertical_dict = {'forward': 0, 'up': -1, 'down': 1}
    line = line.strip()
    direction, value = line.split(' ')
    return horizontal_dict[direction], vertical_dict[direction], int(value)

def parse_rules(fname):
    horizontal_sum = 0
    vertical_sum = 0
    node_dict = {}
    for line in open(fname):
        hmult, vmult, value = parse_line(line)
        # print('parsed values: ', hmult, vmult, value)
        horizontal_sum += value * hmult
        vertical_sum += value * vmult
    print("Horizontal sum: ", horizontal_sum)
    print("Vertical sum: ", vertical_sum)
    return horizontal_sum, vertical_sum

def parse_rules_star2(fname):
    horizontal_sum = 0
    vertical_sum = 0
    aim = 0
    node_dict = {}
    for line in open(fname):
        hmult, vmult, value = parse_line(line)
        # print('parsed values: ', hmult, vmult, value)
        horizontal_sum += value * hmult
        vertical_sum += aim * hmult * value
        aim += value * vmult
        print(horizontal_sum, vertical_sum, aim)
    print("Horizontal sum: ", horizontal_sum)
    print("Vertical sum: ", vertical_sum)
    return horizontal_sum, vertical_sum

def main():
    # inputs = get_input_as_list('day2_input.txt')
    # print(inputs)
    hsum, vsum = parse_rules('day2_input.txt')
    print('Multiplied v*h:', hsum*vsum)

    hsum2, vsum2 = parse_rules_star2('day2_input.txt')

    print('star 2 v*h:', hsum2*vsum2)


if __name__== main():
    main()


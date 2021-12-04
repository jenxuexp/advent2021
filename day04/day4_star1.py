import os
import numpy as np
import copy


def parse_line(line):
    line = line.strip()
    
    return 

def parse_rules(fname):
    line_num = 0
    array_list = []
    current_array = []
    for line in open(fname):
        if line_num == 0:
            numbers_list = [int(num) for num in line.strip().split(',')]
        else:
            if len(line.strip()) == 0 and len(current_array) > 0:
                array_list.append(np.array(current_array.copy()))
                current_array = []
            elif len(line.strip()) > 0:
                current_array.append([int(num) for num in line.strip().split()])
        line_num += 1
    array_list.append(np.array(current_array.copy()))
    return array_list, numbers_list

def initialize_array_checkers(array_list):
    array_checkers = []
    for an in range(len(array_list)):
        array_checkers.append(np.zeros_like(array_list[an]))
    return array_checkers

def check_array(input_array, array_tracker, number):
    # Update the array tracker based on the current number
    matching_inds = input_array == number
    array_tracker[matching_inds] = 1
    row_sums = np.sum(array_tracker, axis=0)
    col_sums = np.sum(array_tracker, axis=1)
    if max(row_sums) >= array_tracker.shape[0] or max(col_sums) >= array_tracker.shape[1]:
        print('row and column sum value: ', row_sums, col_sums)
        print('Scoring winning array \n', input_array)
        print('Tracking array has values: \n', array_tracker)
        # winning board, return sum of all unmarked numbers
        score = np.sum(input_array[~array_tracker.astype(bool)])
        return True, score*number
    else:
        return False, array_tracker

def main():
    array_list, numbers_list = parse_rules('day4_input.txt')
    array_trackers = initialize_array_checkers(array_list)
    for num in numbers_list:
        print('Checking Number ', num)
        for array_num, array_val in enumerate(array_list):
            print('Checking Array Number ', array_num)
            is_match, return_val = check_array(array_val, array_trackers[array_num], num)
            if is_match:
                print('Matching array score: ', return_val)
                return
            else:
                array_trackers[array_num] = return_val
                print('No match for array, new tracking array = \n', array_trackers[array_num])


if __name__== main():
    main()
import os
import copy
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

def binary_array_to_decimal(binary_array):
    little_endian = np.flip(np.squeeze(binary_array))
    value = 0
    print('Turning binary array', binary_array, 'into little-endian ', little_endian)
    for power, digit in enumerate(little_endian):
        print('power and digit: ', power, digit)
        value += digit* (2**power)
    return value

def main():
    digits_array = parse_rules('day3_input.txt')

    # Loop through each of the selected bits and copy over only the numbers with those values in each column
    oxygen_array = digits_array.copy()
    co2_array = digits_array.copy()
    for col_num in range(oxygen_array.shape[1]):
        current_bit_value = int(np.sum(oxygen_array[:, col_num]) >= oxygen_array.shape[0]/2)
        valid_inds = oxygen_array[:, col_num] == current_bit_value
        oxygen_array = oxygen_array[valid_inds]
        if oxygen_array.shape[0] == 1:
            oxygen_value = binary_array_to_decimal(oxygen_array) #yikes
            print('Oxygen binary value: ', oxygen_array)
            print('Oxygen decimal value: ', oxygen_value)
            break

    # yeah I probably should've made that into a function. I'm sorry Cheryl. :'(
    for col_num in range(co2_array.shape[1]):
        current_bit_value = int(np.sum(co2_array[:, col_num]) < co2_array.shape[0]/2)
        valid_inds = co2_array[:, col_num] == current_bit_value
        co2_array = co2_array[valid_inds]
        if co2_array.shape[0] == 1:
            co2_value = binary_array_to_decimal(co2_array)
            print('CO2 binary value: ', co2_array)
            print('CO2 decimal value: ', co2_value)
            break
    
    print('Number of rows to make them equal: ', digits_array.shape[0]/2)
    print('Oxygen find bits: ', oxygen_bit_values)
    print('CO2 binary find bits: ', co2_bit_values)
    print('Product: ', oxygen_value*co2_value)


if __name__== main():
    main()
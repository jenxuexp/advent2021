import os
import numpy as np
import copy


def parse_rules(fname):
    code_vals = []
    lookup_vals = []
    for line in open(fname):
        line = line.strip()
        lookup_digits = line.split('|')[0].strip()
        code_digits = line.split('|')[1].strip()
        lookup_vals.append([set(str_val) for str_val in lookup_digits.split()])
        code_vals.append([set(str_val) for str_val in code_digits.split()])
    return lookup_vals, code_vals

def set_to_string(input_set):
    return "".join(str_val for str_val in sorted(input_set))

def disambiguate_digits(fives, sixes, lookup_dict, inv_lut):
    # First, can get sixen
    for ind, six in enumerate(sixes):
        if len(six.intersection(inv_lut[1])) == 1:
            lookup_dict[set_to_string(six)] = 6
            inv_lut[6] = six
        elif len(six.intersection(inv_lut[4])) == 4:
            lookup_dict[set_to_string(six)] = 9
            inv_lut[9] = six
        else: 
            lookup_dict[set_to_string(six)] = 0
            inv_lut[0] = six
    #Then, get 5s
    for ind, five in enumerate(fives):
        if len(five.intersection(inv_lut[1])) == 2:
            lookup_dict[set_to_string(five)] = 3
            inv_lut[3] = five
        elif len(five.intersection(inv_lut[6])) == 5:
            lookup_dict[set_to_string(five)] = 5
            inv_lut[5] = five
        else:
            lookup_dict[set_to_string(five)] = 2
            inv_lut[2] = five
    return lookup_dict, inv_lut

    
def main():
    display_intersects()
    sum_counter = 0
    multipliers = [1000, 100, 10, 1]
    lookup_vals, code_vals = parse_rules('input.txt')
    for lookup_val, code_val in zip(lookup_vals, code_vals):
        lookup_dict = dict()
        inverse_lookup_dict = dict()
        fives = []
        sixes = []
        for lookup_set in lookup_val:
            lookup_str = set_to_string(lookup_set)
            if len(lookup_str) == 2:
                lookup_dict[lookup_str] = 1
            elif len(lookup_str) == 4:
                lookup_dict[lookup_str] = 4
            elif len(lookup_str) == 7:
                lookup_dict[lookup_str] = 8
            elif len(lookup_str) == 3:
                lookup_dict[lookup_str] = 7
            elif len(lookup_str) == 5:
                fives.append(lookup_set)
            else:
                sixes.append(lookup_set)
        #wow such inefficient
        inverse_lookup_dict = {v: set(k) for k, v in lookup_dict.items()}
        lookup_dict, inverse_lookup_dict = disambiguate_digits(fives, sixes, lookup_dict, inverse_lookup_dict)
        for k,v in lookup_dict.items():
        for multiplier, code_str in zip(multipliers, code_val):
            sum_counter += multiplier * lookup_dict[set_to_string(code_str)]
    print('Final sum: ', sum_counter)

def display_intersects():
    standard_dict = {
        0: set('abcefg'),
        1: set('cf'),
        2: set('acdeg'),
        3: set('acdfg'),
        4: set('bcdf'),
        5: set('abdfg'),
        6: set('abdefg'),
        7: set('acf'),
        8: set('abcdefg'),
        9: set('abcdfg')
    }
    disp_array = np.zeros((10,10))
    for row in range(10):
        for col in range(10):
            disp_array[row, col] = len(standard_dict[row].intersection(standard_dict[col]))
    print(disp_array)
    print("Fives intersections (2, 3, 5): ")
    print(np.arange(10).astype(float))
    print(disp_array[[2, 3, 5], :])
    print('Sixes intersections (0, 6, 9): ')
    print(np.arange(10).astype(float))
    print(disp_array[[0, 6, 9], :])


if __name__== main():
    main()
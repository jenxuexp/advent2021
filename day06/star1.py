import os
import numpy as np
import copy


def parse_rules(fname):
    for line in open(fname):
        print(line)
        line = line.strip()
        starter_fishies = [int(num) for num in line.split(',')]
    return starter_fishies

def main():
    starter_fishies = parse_rules('input.txt')
    fish_pond = starter_fishies.copy()
    day = 0
    end_day = 80
    # Try the dumbest solution and see if it works
    while day < end_day:
        new_fish = []
        for fid, fish in enumerate(fish_pond):
            if fish == 0:
                new_fish.append(8)
                fish_pond[fid] = 6
            else:
                fish_pond[fid] -= 1
        fish_pond.extend(new_fish)
        new_fish = 0
        day += 1
    print('Number of fish: ', len(fish_pond))

if __name__== main():
    main()
import os
import numpy as np
import copy
from collections import defaultdict

NEW_FISH_RATE = 8
EQ_FISH_RATE = 6

def parse_rules(fname):
    for line in open(fname):
        line = line.strip()
        starter_fishies = [int(num) for num in line.split(',')]
    return starter_fishies

def main():
    starter_fishies = parse_rules('input.txt')
    fish_pond = starter_fishies.copy()

    fish_tracker = defaultdict(int)
    
    for fish in fish_pond:
        fish_tracker[fish] += 1
    day = 0
    end_day = 256
    num_fish = len(starter_fishies)
    while day < end_day:
        num_fish += fish_tracker[day]
        fish_tracker[day + NEW_FISH_RATE + 1] += fish_tracker[day] # new fish will spawn in 8 days
        fish_tracker[day + EQ_FISH_RATE + 1] += fish_tracker[day] # old fish will spawn again in 6 days
        day += 1
    print("Day ", day, ", total fish in pond = ", num_fish)

if __name__== main():
    main()
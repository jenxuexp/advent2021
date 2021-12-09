import os
import numpy as np
import copy
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import measure

def parse_rules(fname):
    map_vals = []
    for line in open(fname):
        print(line)
        line = line.strip()
        code_digits = [int(height) for height in line]
        map_vals.append(code_digits)
    return np.array(map_vals)

def main():
    map_vals = parse_rules('input.txt')

    # Binary clustering for glory and profit
    binary_im = map_vals < 9
    all_labels = measure.label(binary_im, connectivity=1)
    regions = measure.regionprops(all_labels)
    areas = []
    for region in regions:
        areas.append(region.area)
    areas = sorted(areas)
    print('maximum three areas multiplificated: ', areas[-1]*areas[-2]*areas[-3])

    
if __name__== main():
    main()
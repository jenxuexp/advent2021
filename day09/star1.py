import os
import numpy as np
import copy
from scipy import ndimage
import matplotlib.pyplot as plt

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
    max_find_footprint = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    max_locs = ndimage.maximum_filter(-map_vals, footprint = max_find_footprint, mode='constant', cval=-9)
    min_inds = max_locs == -map_vals


    # This hurts...
    dumb_risk = 0
    row_col_inds = []
    for row in np.arange(0, map_vals.shape[0]):
        for col in np.arange(0, map_vals.shape[1]):
            compare_vals = []
            # I am being belligerently anti-computer scientist...we could have had peace in this land
            # if row == 0:
            #     if col == 0:
            #         compare_vals = np.array([map_vals[row, col + 1], map_vals[row + 1, col]])
            #     else:
            #         compare_vals = np.array([map_vals[row, col + 1], map_vals[row + 1, col],
            #             map_vals[row, col - 1]])
            # elif row == map_vals.shape[0] - 1:
            # compare_vals = np.array([map_vals[row-1, col], map_vals[row, col-1], 
            #     map_vals[row + 1, col], map_vals[row, col + 1]])
            if row > 0:
                compare_vals.append(map_vals[row - 1, col])
            if col > 0:
                compare_vals.append(map_vals[row, col - 1])
            try:
                compare_vals.append(map_vals[row + 1, col])
            except:
                print('found invalid row (bottom)', row, col)
            try:
                compare_vals.append(map_vals[row, col + 1])
            except:
                print('found invalid column (right)')
            compare_vals = np.array(compare_vals)
            if np.sum(map_vals[row, col] >= compare_vals) == 0 and len(compare_vals) > 0:
                dumb_risk += map_vals[row, col] + 1
                row_col_inds.append([row, col])
    print('Doing risk calculating the dumb way: ', dumb_risk)
    row_col_inds = np.array(row_col_inds)
    # # Oh lawd it didn't work for the input...time to debug
    XX, YY = np.meshgrid(np.arange(map_vals.shape[0]), np.arange(map_vals.shape[1]))
    xx = XX[min_inds]
    yy= YY[min_inds]
    fig, ax = plt.subplots(1, 3, figsize=(8, 4))
    ax[0].imshow(map_vals)
    ax[0].plot(xx, yy, 'bx')
    ax[0].plot(row_col_inds[:, 1], row_col_inds[:, 0], 'r+')
    ax[1].imshow(-max_locs)
    ax[2].imshow(map_vals * min_inds)
    plt.show()
    # I am sad. This should have worked. I think it is strictly less than, not less than equal to. Curse you prompt!


    risk = np.sum(map_vals[min_inds] + 1)
    print('Risk for map: ', risk)
    other_risk = np.sum(((map_vals + 1)*min_inds).flatten())
    print('Other way of calculating risK: ', other_risk)

if __name__== main():
    main()
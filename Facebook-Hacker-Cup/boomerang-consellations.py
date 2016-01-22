# Facebook Hacker Cup 2016 Qualification Round
# Time execution: 19 seconds

import numpy as np
from collections import Counter


def distances(a, b, X, Y):
    return (X-a)**2 + (Y-b)**2


def binom(a, b):
    # about 5 times slower than x*(x-1)/2
    n = math.factorial(a)
    k = math.factorial(b)
    return n//(math.factorial(a-b)*k)


def numpy():
    cases = int(input())
    for CASE in range(cases):
        stars = int(input())
        X = np.empty(stars, dtype=np.int32)
        Y = np.empty(stars, dtype=np.int32)

        for j in range(stars):
            X[j], Y[j] = input().split()

        boomerangs = 0
        for i in range(stars):
            dist_arr = distances(X[i], Y[i], X, Y)

            # GET NUMBER OF POSSIBLE PAIRS
            # METHOD 1 18.7s
            dups = Counter(dist_arr)
            boomerangs += sum((num*(num-1)/2 for num in dups.values() if num > 1))

            # METHOD 2 22s
            # dups = np.unique(dist_arr, return_counts=True)[1]
            # boomerangs += sum((num*(num-1)/2 for num in dups if num > 1))

            # METHOD 3 inf.
            # boomerangs += sum((num*(num-1)/2 for num in np.bincount(dist_arr) if num > 1))

            #print(dist_arr)

        print("Case #{}: {}".format(CASE+1, int(boomerangs)))


numpy()

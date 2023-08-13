import numpy as np
import matplotlib.pyplot as plt
 
 ## sin(k / n power (2i/d)) -- even positions
 ## cos(k / n power (2i/d)) -- odd positions


def getPositionEncoding(seq_len, d, n=10000):
    base_mat = np.zeros([seq_len, d])
    for k in range(seq_len):
        for i in np.arange(d / 2):
            denominator = np.power(n, 2 * i / d)
            base_mat[k, int(2 * i)] = np.sin(k / denominator)
            base_mat[k, int(2 * i) + 1] = np.cos(k / denominator)
    return base_mat


P = getPositionEncoding(seq_len=4, d=8, n=100)
print(P)
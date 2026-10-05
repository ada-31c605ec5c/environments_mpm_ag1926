from turtle import pd

import numpy as np
from scipy.ndimage import gaussian_filter

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'pandas_table']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def pandas_table(data, columns):
    import pandas as pd
    return pd.DataFrame(data, columns=columns)
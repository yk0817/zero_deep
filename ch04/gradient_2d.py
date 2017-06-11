# coding: utf-8

import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D #3次元


def _numerical_gradient_no_batch(f,x):
    h = 1e-4
    
    

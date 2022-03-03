# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:02:16 2022

@author: johan
"""

from rbf_cython import rbf_cython
import numpy as np
import time
D = 5
N = 1000
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10
t0 = time.time()
rbf_cython(X, beta, theta)
print("cython: ", time.time() - t0)
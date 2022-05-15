# -*- coding: utf-8 -*-

import numpy as np


def create_rhs_from_1darr(arr):
    n = arr.shape[0]
    n2 = int(np.sqrt(n))
    arr2 = arr.reshape(n2, -1)
    print(arr)
    print(arr2)

    return rhs_factory(arr2)


def rhs_factory(A):
    n, m = A.shape
    # sicherstellen, dass A quadratisch ist
    assert n == m

    def rhs(state, time):
        x_dot = np.dot(A, state)

        return x_dot

    rhs.number_of_states = m

    return rhs

# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from data_tools import create_rhs_from_1darr


def simulate(rhs):
    np.random.seed(75)
    xx0 = np.random.rand(rhs.number_of_states)

    res = odeint(rhs, xx0, tt)

    x1 = res[:, 0]

    plt.plot(tt, x1)


rhs_list = []

for k in range(1, 5):
    fname = "data{}.txt".format(k)
    print(fname)
    try:
        x = np.loadtxt(fname)
    except ValueError as ve:
        print("Fehler:", ve)
    else:
        rhs = create_rhs_from_1darr(x)
        rhs_list.append(rhs)

tt = np.linspace(0, 5, 1000)

# zwei verschiedene Varianten die Simulation auf Systeme mit
# Zustandsdimension kleiner 3 einzuschränken.

# rhs_list = filter(lambda q: q.number_of_states < 3, rhs_list)
rhs_list = [q for q in rhs_list if q.number_of_states < 3]

list(map(simulate, rhs_list))
plt.show()

from scipy.integrate import odeint, ode
import numpy as np
import math


def undamped():
    '''
    :return: numpy.ndarray
    '''
    # initial state:
    y0 = [1.0, 0.0]
    # time coodinate to solve the ODE for:
    t = np.linspace(0, 10, 10)
    # frequency:
    w0 = 2.0 * math.pi
    return [[math.cos(w0 * s + y0[0]), y0[1]] for s in t]

print(undamped())

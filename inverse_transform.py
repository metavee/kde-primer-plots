"""
Functions for creating random number generators that obey (nearly) arbitrary distributions.
"""


import numpy as np
import sympy as sp
import scipy.optimize as opt


def rng(pdf, x_lo, x_hi):
    """
    Take a sympy expression for a probability density function along with a numerical domain, and return a random number generator obeying that distribution.
    """

    assert x_lo < x_hi

    cdf = get_cdf(pdf, x_lo, x_hi)
    symbols = list(cdf.free_symbols)
    assert len(symbols) == 1
    x_mid = symbols[0]
    cdf_num = cdf_num = sp.lambdify(x_mid, cdf, 'mpmath')

    icdf_num = inverse(cdf_num, x_lo, x_hi)

    def rand():
        return icdf_num(np.random.random())

    return rand


def get_cdf(pdf, x_lo, x_hi):
    """
    Take a sympy expression for a probability density function, and return an expression for the cumulative probability density function.
    """

    symbols = list(pdf.free_symbols)
    assert len(symbols) == 1
    x_symbol = symbols[0]

    # variable such that x_lo <= x_mid <= x_hi
    x_mid = sp.symbols('x_mid')

    cdf = sp.integrate(pdf, (x_symbol, x_lo, x_mid))
    # normalize cdf range to [0, 1]
    cdf /= cdf.subs(x_mid, x_hi).evalf()

    return cdf


def inverse(cdf, x_lo, x_hi):
    """
    Take a numeric cumulative probability density function and return its inverse.
    """

    def icdf(m):
        assert 0 <= m <= 1

        objective = lambda x: cdf(x) - m

        return opt.brentq(objective, x_lo * 0.99, x_hi * 1.01)

    return icdf

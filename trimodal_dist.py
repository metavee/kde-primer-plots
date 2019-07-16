import numpy as np
import sympy as sp

import inverse_transform


# symbolically define PDF: f(x) = x sin^2(x)
x_sym = sp.symbols('x')
x_lo = 0
x_hi = 3*np.pi

trimodal_pdf_sym = x_sym * sp.sin(x_sym)**2
trimodal_pdf_sym /= sp.integrate(trimodal_pdf_sym, (x_sym, x_lo, x_hi))
trimodal_pdf_num = sp.lambdify(x_sym, trimodal_pdf_sym)


def trimodal_pdf(n_points):
    x_num = np.linspace(x_lo, x_hi, n_points)

    return x_num, np.array([trimodal_pdf_num(x) for x in x_num])


def make_dataset(n_points, seed=None):
    # set RNG state if specified
    if seed is not None:
        rng_state = np.random.get_state()
        np.random.seed(seed)

    rng = inverse_transform.rng(trimodal_pdf_sym, x_lo, x_hi)

    xs = np.array([rng() for i in range(n_points)])

    # restore RNG state
    if seed is not None:
        np.random.set_state(rng_state)

    return xs

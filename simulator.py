import tensorflow as tf
import numpy as np
import itertools
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()
import GPy

"""
basic utilities for simulating data
"""

def sim_f(X, k=GPy.kern.RBF(input_dim=2, variance=1., lengthscale=10), mu=5):
    """
    simulates function values given X
    Args:
        X (np.array): data points
        k (GPy.kernel): kernel function
        mu (np.array): prior mean

    Returns: sampled function values

    """
    return np.random.multivariate_normal(np.ones(X.shape[0]) * mu, k.K(X, X))

def sim_X(D=2, N_dim=30, lower=0, upper=100):
    """
    Simulates X on a rectilinear grid
    Args:
        D (int): dimensions
        N_dim (int): number of points per dimension
        lower (float): lower bound for uniform draw
        upper (float): upper bound for uniform draw

    Returns: points on a grid

    """
    grid = [np.sort(np.random.uniform(lower, upper, size=N_dim)) for d in range(D)]

    return np.array(list(itertools.product(*grid)))


def poisson_draw(f, noise_val):
    """

    Args:
        f (np.array): draws a poisson based on function values (with some noise added)
        noise_val(float): between zero and one, add normal noise to f

    Returns: poisson draws

    """
    return np.random.poisson(np.exp(f + noise_val* np.random.normal(0, 1, size=len(f))))
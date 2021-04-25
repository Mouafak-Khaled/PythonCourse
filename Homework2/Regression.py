import numpy as np
import pandas as pd


def linearRegresson(X, Y):

    if X.size == 0 or Y.size = 0:
        return (-1, -1, -1, -1)

    if not isinstance(X, np.array):
        print("X must be a numpy array!")
        return (-1, -1, -1, -1)

    if not isinstance(Y, np.array):
        print("Y must be a numpy array!")
        return (-1, -1, -1, -1)

    if (X.shape != Y.shape):
        print("X and Y must have equal shape!")
        return (-1, -1, -1, -1)

    N = X.shape[0]
    K = X.shape[1]


    #appending a vector of ones to avoid singularity.
    ones_vector = np.ones((N,1))
    X = np.hstack((ones_vector, X))


    #Calculating the estimate
    X_transpose_inverse = np.linalg.inv(np.matmul(X.transpose(), X))
    beta_estimate = np.matmul(np.matmul(X_transpose_inverse, X.transpose()), Y)

    error = Y - np.matmul(new_X, beta_estimate)
    error = np.array(error)

    segma_square = np.matmul(error.transpose(), error)/(N - K - 1)
    variance = np.matmul(segma_square, X_transpose_inverse)





import numpy as np
import pandas as pd


def linearRegression(X, Y):

    if X.size == 0 or Y.size == 0:
        raise Exception("X or Y should not be Empty!")
        return -1, -1, -1, -1

    if not isinstance(X, (np.ndarray, list)):
        raise Exception("X must be a numpy array or a normal python array!")
        return -1, -1, -1, -1

    if not isinstance(Y,  (np.ndarray, list)):
        raise Exception("Y must be a numpy array or a normal python array!")
        return -1, -1, -1, -1

    if X.shape != Y.shape:
        raise Exception("X and Y must have equal shape!")
        return -1, -1, -1, -1

    #handling the Nan values in my data
    list_wise_delete(X, Y)

    N = X.shape[0]
    K = X.shape[1]


    #appending a vector of ones to avoid singularity.
    ones_vector = np.ones((N,1))
    X = np.hstack((ones_vector, X))


    #Calculating the estimate
    X_transpose_inverse = np.linalg.inv(np.matmul(X.transpose(), X))
    beta_estimate = np.matmul(np.matmul(X_transpose_inverse, X.transpose()), Y)

    #calculating the errors
    error = Y - np.matmul(X, beta_estimate)
    error = np.array(error)

    #calculating the variances
    segma_square = np.matmul(error.transpose(), error)/(N - K - 1)
    Var = np.multiply(segma_square, X_transpose_inverse)

    #calculating the credible intervals

    STD_ERROR = np.sqrt(Var.diagonal() / N)

    CL = beta_estimate - 1.96 * STD_ERROR
    CR = beta_estimate + 1.96 * STD_ERROR

    return beta_estimate, STD_ERROR, CL, CR


def list_wise_delete(X, Y):

    for i in range(len(X)):
        if not isinstance(X[i], (float, int)) or not isinstance(Y[i], (float, int)):
            np.delete(X, X[i])
            np.delete(Y, Y[i])




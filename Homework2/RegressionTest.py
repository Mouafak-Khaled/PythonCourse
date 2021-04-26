import numpy as np
import pandas as pd
import Regression
import unittest

class RegressionTest(unittest.TestCase):

    X = np.array([])
    Y = np.array([])

    def empty_test(self):
        with self.assertRaises(Exception) as context:
            beta, error, CL, CR = Regression.linearRegression(X, Y)
        self.assertTrue("X or Y should not be Empty!" in context.exception)
        self.assertEqual(beta, -1)
        self.assertEqual(error, -1)
        self.assertEqual(CL, -1)
        self.assertEqual(CR, -1)

    X = np.array([0.85, 0.36, 0.95, 0.93, 1.0, 0.15, 0.75, 0.69, 0.65, 0.57])
    Y = np.array([17.5, 11.4, 10.0, 15.0, 15.7, 16.9, 14.6])

    def data_shape_test(self):
        with self.assertRaises(Exception) as context:
            beta, error, CL, CR = Regression.linearRegression(X, Y)
        self.assertTrue("X and Y must have equal shape!" in context.exception)
        self.assertEqual(beta, -1)
        self.assertEqual(error, -1)
        self.assertEqual(CL, -1)
        self.assertEqual(CR, -1)

    X = (0.5, 0.10, 0.95, 0.37, 1.0)
    Y = np.array([14.0, 12.5, 16.9, 17.8, 11.6])

    def parameter_type_test(self):
        with self.assertRaises(Exception) as context:
            beta, error, CL, CR = Regression.linearRegression(X, Y)
        self.assertTrue("X and Y must be numpy arrays or python lists!" in context.exception)
        self.assertEqual(beta, -1)
        self.assertEqual(error, -1)
        self.assertEqual(CL, -1)
        self.assertEqual(CR, -1)





if __name__ == '__main__':  # Add this if you want to run the test with this script.
    unittest.main()

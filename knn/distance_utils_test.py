import unittest
import distance_utils
import numpy as np


class TestDistanceUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_euclidean_distance(self):

        # arrange
        vector1 = np.array([5.1, 3.5, 1.4, 0.2])
        vector2 = np.array([4.9, 3.0, 1.4, 0.2])
        expected_result = 0.538516

        # act
        result = distance_utils.euclidean_distance(vector1, vector2)

        # assert
        self.assertAlmostEqual(expected_result, result, 3)

    def test_manhattan_distance(self):

        # arrange
        vector1 = np.array([5.1, 3.5, 1.4, 0.2])
        vector2 = np.array([4.9, 3.0, 1.4, 0.2])
        expected_result = 0.7

        # act
        result = distance_utils.manhattan_distance(vector1, vector2)

        # assert
        self.assertAlmostEqual(expected_result, result, 3)

    def test_chebyshev_distance(self):

        # arrange
        vector1 = np.array([5.1, 3.5, 1.4, 0.2])
        vector2 = np.array([4.9, 3.0, 1.4, 0.2])
        expected_result = 0.5

        # act
        result = distance_utils.chebyshev_distance(vector1, vector2)

        # assert
        self.assertAlmostEqual(expected_result, result, 3)


if __name__ == '__main__':
    unittest.main()

from one_hot_encoder import fit_transform

import unittest


class TestOneHotEncoding(unittest.TestCase):
    def test_cities(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_samewords(self):
        self.assertEqual(fit_transform(['Moscow', 'Moscow']), [('Moscow', [1]), ('Moscow', [1])])

    def test_tuple_integers(self):
        self.assertEqual(fit_transform((1, 0, 0, 1)), [(1, [0, 1]), (0, [1, 0]), (0, [1, 0]), (1, [0, 1])])

    def test_range(self):
        self.assertEqual(fit_transform(range(3)), [(0, [0, 0, 1]), (1, [0, 1, 0]), (2, [1, 0, 0])])

    def test_one_string(self):
        self.assertEqual(fit_transform('ars'), [('ars', [1])])

    def test_empty_string(self):
        self.assertIsNot(fit_transform(''), '')  # should be [('', [1])]

    def test_typeerror(self):
        with self.assertRaises(TypeError):
            fit_transform()
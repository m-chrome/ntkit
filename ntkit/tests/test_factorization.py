"""
Tests for factorization algorithms
"""

from unittest import TestCase
from unittest import main as test

from ntkit.factorization import fermat_method


class FermatTest(TestCase):
    def test_on_composite_numbers(self):
        self.assertEqual(set(fermat_method(217513)), {443, 491})
        self.assertEqual(set(fermat_method(265357)), {443, 599})
        self.assertEqual(set(fermat_method(272551)), {479, 569})
        self.assertEqual(set(fermat_method(239011)), {457, 523})
        self.assertEqual(set(fermat_method(308911)), {541, 571})
        self.assertEqual(set(fermat_method(327653)), {547, 599})
        self.assertEqual(set(fermat_method(364087)), {577, 631})

    def test_on_prime_numbers(self):
        self.assertEqual(set(fermat_method(1279)), {1279, 1})
        self.assertEqual(set(fermat_method(1877)), {1877, 1})
        self.assertEqual(set(fermat_method(2347)), {2347, 1})
        self.assertEqual(set(fermat_method(2371)), {2371, 1})
        self.assertEqual(set(fermat_method(2389)), {2389, 1})
        self.assertEqual(set(fermat_method(2437)), {2437, 1})
        self.assertEqual(set(fermat_method(2467)), {2467, 1})
        self.assertEqual(set(fermat_method(2677)), {2677, 1})

    def test_on_square_numbers(self):
        self.assertEqual(fermat_method(81), (9, 9))
        self.assertEqual(fermat_method(1024), (32, 32))
        self.assertEqual(fermat_method(208849), (457, 457))


if __name__ == "__main__":
    test()

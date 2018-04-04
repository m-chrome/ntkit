"""
Tests for factorization algorithms
"""

from unittest import TestCase
from unittest import main as test

from ntkit.factorization import brent_method
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


class BrentTest(TestCase):
    def test_on_composite_numbers(self):
        self.assertEqual(set(brent_method(217513, 10)), {443, 491})
        self.assertEqual(set(brent_method(265357, 10)), {443, 599})
        self.assertEqual(set(brent_method(272551, 10)), {479, 569})
        self.assertEqual(set(brent_method(239011, 10)), {457, 523})
        self.assertEqual(set(brent_method(308911, 10)), {541, 571})
        self.assertEqual(set(brent_method(327653, 10)), {547, 599})
        self.assertEqual(set(brent_method(364087, 10)), {577, 631})

    def test_on_prime_numbers(self):
        self.assertEqual(brent_method(1279, 6), None)
        self.assertEqual(brent_method(1877, 6), None)
        self.assertEqual(brent_method(2347, 6), None)
        self.assertEqual(brent_method(2371, 6), None)
        self.assertEqual(brent_method(2389, 6), None)
        self.assertEqual(brent_method(2437, 6), None)
        self.assertEqual(brent_method(2467, 6), None)
        self.assertEqual(brent_method(2677, 6), None)


if __name__ == "__main__":
    test()

######################################################################################
# Test NUMBTHY.PY
# Basic Number Theory functions implemented in Python
# Author: Robert Campbell, <campbell@math.umbc.edu>
# Date: 14 Oct 2014
# Version 0.8
######################################################################################

import unittest
import numbthy
import random

class Test_numbthy(unittest.TestCase):

    def test_gcd(self):
        for (a, b, expected_gcd) in ((1,1,1),(-1,1,1),(6,0,6),(0,6,6),(6,6,6),(1234,5678,2),(12345675,34567890,2469135)):
            self.assertEqual(numbthy.gcd(a,b),expected_gcd)

    def test_xgcd(self):
        for a,b,g,x,y in ((1,-1,1,0,-1),(6,8,2,-1,1),(12345,2345,5,87,-458),(98760,76540,20,1898,-2449)):
            self.assertEqual(numbthy.xgcd(a,b),(g,x,y))

    def test_xgcd_random(self):
        for testnum in range(10):
            a = random.randint(0,10**20); b = random.randint(0,10**20)
            (g,x,y) = numbthy.xgcd(a,b)
            self.assertEqual(g,a*x+b*y, "xgcd error: {2} != ({0})*({3}) + ({1})*({4})".format(a,b,g,x,y))

    def test_power_mod(self):
        for (b,e,n,expected_pow) in ((2,5,13,6),(2,-21,31,16),(-2,-21,31,15),(0,5,31,0),(5,0,31,1)):
            self.assertEqual(numbthy.power_mod(b,e,n),expected_pow)

    def test_power_mod_raise_ValueError(self):  # Error for power_mod(2,-11,26)
        self.assertRaises(ValueError,numbthy.power_mod,2,-11,26)

    def test_power_mod_raise_ZeroDivisionError(self):  # Error for power_mod(2,5,0)
        self.assertRaises(ZeroDivisionError,numbthy.power_mod,2,5,0)

    def test_is_prime(self):
        for n,expected_prime in ((1,False),(0,False),(-2,True),(19,True),(1236,False),(1237,True),(321197185,False)):
            self.assertEqual(numbthy.is_prime(n),expected_prime)

    def test_euler_phi(self):
        for n,expected_phi in ((-5,0),(0,0),(1,1),(2,1),(4,2),(8*7,24),(2**4*3**3*7**2*19,108864)):
            self.assertEqual(numbthy.euler_phi(n),expected_phi)

    def test_carmichael_lambda(self):
        for n,expected_carm in ((1,1),(2,1),(4,2),(8*7,6),(2**4*3**3*7**2*19,252)):
            self.assertEqual(numbthy.carmichael_lambda(n),expected_carm)

    def test_carmichael_lambda_raise_ValueError(self):  # Error for carmichael_lambda(0)
        self.assertRaises(ValueError,numbthy.carmichael_lambda,0)

    def test_factor(self):
        for n,expected_factors in ((-15,((3, 1), (5, 1))),(1234561000,((2, 3), (5, 3), (211, 1), (5851, 1)))):
            self.assertEqual(numbthy.factor(n),expected_factors)

    def test_properties_on_random_int(self):
        # for n in range(2, 20):
        for testnum in range(10):
            n = random.randint(2,10**20)
            self.assertEqual(numbthy.gcd(n, n), n, "gcd(%d,%d) should be %d" % (n, n, n))
            is_prime = numbthy.is_prime(n)
            phi = numbthy.euler_phi(n)
            factor = numbthy.factor(n)
            factors = numbthy.factors(n)

            prod = 1
            prev_p = None
            for p, e in factor:
               self.assertTrue(numbthy.is_prime(p), "Factors of %d should be prime: %d is not" % (n, p))
               if prev_p is not None:
                   self.assertGreater(p, prev_p, "Factors of %d are not stricly sorted: %s" % (n, factors))
               prod *= p**e
               prev_p = p
            self.assertEqual(prod, n, "Product of factors should be equal to %d" % n)

            prod = 1
            prev_p = None
            for p in factors:
               self.assertTrue(numbthy.is_prime(p), "Factors of %d should be prime: %d is not" % (n, p))
               if prev_p is not None:
                   self.assertGreaterEqual(p, prev_p, "Factors of %d are not sorted: %s" % (n, factors))
               prod *= p
               prev_p = p
            self.assertEqual(prod, n, "Product of factors should be equal to %d - bis" % n)

            if is_prime:
                self.assertEqual(factor, ((n, 1),), "Prime number %d should have no other factors" % n)
                self.assertEqual(factors, [n])
                self.assertEqual(phi, n-1)
            else:
                self.assertGreater(len(factors), 1)


if __name__ == '__main__':
    unittest.main()


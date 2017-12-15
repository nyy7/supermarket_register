#!/usr/bin/python

##########
# author: Yanyan Ni
# date: 12/15/17
# description: unittest for calculator.py
##########

import sys
sys.path.append('../scripts')
from calculator import Calculator
import unittest
import xmlrunner

def suite():
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.makeSuite(test_calculator))
    return testsuite

class test_calculator(unittest.TestCase):
    def setUp(self):
        self.empty = Calculator('')
        self.calculator = Calculator('A12T-4GH7-QPL9-3N4M;65P1-UDGM-XH2M-LQW2')
        self.calculatorLower = Calculator('a12t-4GH7-QPL9-3n4m;65p1-udgm-xh2m-lqw2')
        self.calculatorExtra = Calculator('A12T-4GH7-QPL9-3N4MABCDE;65P1-UDGM-XH2M-LQW2')
        self.calculatorSpace = Calculator('A12T-4GH7-QPL9-3N4M; 65P1-UDGM-XH2M-LQW2  ')
        self.calculatorBadInput = Calculator('A12T-4GH7-QPL9-3N4M;ABCDEFGH')

    def test_input_validation(self):
        self.assertEqual(False, self.empty.input_validation())
        self.assertEqual(True, self.calculatorLower.input_validation())
        self.assertEqual(True, self.calculator.input_validation())
        self.assertEqual(True, self.calculatorExtra.input_validation())
        self.assertEqual(True, self.calculatorSpace.input_validation())
        self.assertEqual(False, self.calculatorBadInput.input_validation())

    def test_price_calculator(self):
        self.assertEqual(9.35, self.calculator.price_calculator())
        self.assertEqual(9.35, self.calculatorLower.price_calculator())
        self.assertEqual(9.35, self.calculatorExtra.price_calculator())
        self.assertEqual(9.35, self.calculatorSpace.price_calculator())

    def test_tax(self):
        self.assertEqual(10.17, self.calculator.add_tax(9.35))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../../test-reports/calculator', verbosity=2))


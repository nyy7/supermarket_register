#!/usr/bin/python

##########
# author: Yanyan Ni
# date: 12/15/17
# description: unittest for __main__.py
##########

import sys
sys.path.append('../scripts')
import register
import unittest
import xmlrunner

def suite():
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.makeSuite(test_register))
    return testsuite

class test_register(unittest.TestCase):
    def test_run(self):
        sku = "A12T-4GH7-QPL9-3N4M;65P1-UDGM-XH2M-LQW2"
        result = register.run(sku)
        self.assertEqual(True, result)
        sku = "A12T-4GH7-QPL9-3N4M;65P1-UDGM-XH2M"
        result = register.run(sku)
        self.assertEqual(False, result)
        sku = ""
        result = register.run(sku)
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../../test-reports/register', verbosity=2))


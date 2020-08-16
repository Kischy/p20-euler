# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:20:22 2020

@author: kisch
"""

import unittest

from digit_sum import DigitSum


class TestDigitSumClass(unittest.TestCase):  
    
    def setUp(self):
        self.DS = DigitSum()
        
    def test_get_last_digit(self):     
        
        result = self.DS.get_last_digit(372)              
        self.assertEqual(result, (2,37))
        
        result = self.DS.get_last_digit(370)              
        self.assertEqual(result, (0,37))
        
        result = self.DS.get_last_digit(894356)              
        self.assertEqual(result, (6,89435))
        
        
    def test_get_digit_sum(self):
        result = self.DS.get_digit_sum(3628800)
        self.assertEqual(result, 27)
        



if __name__ == '__main__':
    unittest.main(verbosity=0)

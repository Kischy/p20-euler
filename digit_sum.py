# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:51:42 2020

@author: kisch
"""


class DigitSum():
    
    def get_digit_sum(self,number):
        sum_digit = 0
        
        while(number > 0):
            digit, number = self.get_last_digit(number)
            sum_digit += digit
        
        return sum_digit
    
    def get_last_digit(self,number):
        digit = number % 10
        new_number = number // 10
        
        return digit,new_number

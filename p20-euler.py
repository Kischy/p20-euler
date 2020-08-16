# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:20:22 2020

@author: kisch
"""

from digit_sum import DigitSum
from math import  factorial


problem_number = 20


print("Calculation started")


DS = DigitSum()



the_answer = DS.get_digit_sum(factorial(100))

print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)



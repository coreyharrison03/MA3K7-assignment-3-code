# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def paper_hat(n, hat, total):
    
    for j in range(n**2):
        num1 = j // n
        num2 = j % n
        diff = np.absolute(hat[num1] - hat[num2])
        if num1 > num2:
            hat2 = np.delete(hat,num1)
            hat2 = np.delete(hat2,num2)
            hat2 = np.append(hat2,diff)
            
            if len(hat2) == 1:
                total += hat2[0]
            
            add = paper_hat(n-1, hat2, total)
            total = add
            
    return total
        

def paper_hat_est(n, loops):
    total = 0
    for i in range(loops):    
        hat = np.arange(1,n+1)
        for i in range (n-1):
            num1 = np.random.randint(0, len(hat))
            val1 = hat[num1]
            hat = np.delete(hat, num1)
            num2 = np.random.randint(0, len(hat))
            val2 = hat[num2]
            hat = np.delete(hat, num2)
            diff = np.absolute(val1 - val2)
            hat = np.append(hat, diff)
        total += hat[0]
    return total/loops

num_in_hat = 2024

paper_est = paper_hat_est(num_in_hat, 10000)

print(paper_est)

numerator = paper_hat(num_in_hat, np.arange(1,num_in_hat+1), 0)

denominator = 1
for i in range(2,num_in_hat+1):
    denominator *= np.math.factorial(i) / (2*np.math.factorial(i-2))
    
simplify = np.gcd(int(numerator), int(denominator))

print(int(numerator/simplify), "/" , int(denominator/simplify))
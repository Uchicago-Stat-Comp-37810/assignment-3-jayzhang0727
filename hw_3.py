# Name: Jinjie Zhang
# hw3.py

import math
import random

# Exercise 1

# Define is_divisible function here

def is_divisible(m,n):
    if n==0:
        return False
    elif m%n==0:
        return True
    else:
        return False

# Test cases for is_divisible

print(is_divisible(10, 5))  # This should return True
print(is_divisible(18, 7))  # This should return False
print(is_divisible(42, 0))  # What should this return? The result should be False

# ********** Exercise 2 **********

# Define not_equal function here

def not_equal(a,b):
    if a==b:
        return False
    else:
        return True

# Test cases for not_equal

not_equal(3,5) #The result should be TRUE
not_equal(20,20) #The result should be FALSE

# ********** Exercise 3 **********

## 1 - multadd function
def multadd(a,b,c):
    return a*b+c


# Test Cases
angle_test = multadd(math.cos(math.pi/4),1/2,math.sin(math.pi/4))
print("sin(pi/4) + cos(pi/4)/2 is:", math.sin(math.pi/4) + math.cos(math.pi/4)/2)
print(angle_test)

ceiling_test = multadd(math.log(12,7),2, math.ceil(276/19))
print("ceiling(276/19) + 2 log_7(12) is:", math.ceil(276/19) + 2 *math.log(12,7))
print(ceiling_test)

# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

def rand_divis_3():
    num = random.randint(0, 100)
    print("The generated random number is:", num)
    if num%3==0:
        return True
    else:
        return False

# Test Cases
    print("Is this random number divided by 3?", rand_divis_3())


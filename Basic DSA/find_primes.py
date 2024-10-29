# Write a function that returns a list of prime numbers up to a given integer n.

# may need to import math and use sqrt


list_of_factors = []

def factors(number):

    if number > 1:
        for i in range(1,number):
            if number % i == 0:
                list_of_factors.append(i)

factors(24)
print(list_of_factors)


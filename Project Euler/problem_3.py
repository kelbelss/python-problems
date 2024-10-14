import math

# square root = (math.sqrt)


allFactors = []
prime_factors = []


def factors(number):
    # find all factors of number and add to list above
    if number > 1:
        for i in range(1,int(math.sqrt(number))+1):
            if number % i == 0:
                allFactors.append(i)

factors(600851475143)

print(allFactors)


def is_prime(p_prime) -> bool: 
    
    if p_prime > 1:
        for i in range(2,p_prime):
             if p_prime % i == 0:
                 return False
        return True    


for factor in allFactors:
#    print("checking if", factor, "is prime")
#    result = is_prime(factor)
    if is_prime(factor) == True:
        prime_factors.append(factor)
    print(prime_factors)
    

# for x in range(2, num):
#     if num % x == 0:
#         print(f"{num} is divisible by {x}")


    


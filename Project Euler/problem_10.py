# Find the sum of all the primes below two million.

import math 

#  primeNumbers = []
result = 0


def prime(poss_prime) -> bool:

    if poss_prime > 1:
        for i in range(2,int(math.sqrt(poss_prime)+1)):
            if poss_prime % i == 0:
                return False
        return True    
  

for number in range(1,2000000):
    # print("checking if", number, "is prime")
    if prime(number) == True:
        result += number
        # primeNumbers.append(number)
    

print(result)
# print(primeNumbers)
# answer = sum(primeNumbers)
# print(answer)



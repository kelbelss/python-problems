# Write a function that returns a list of prime numbers up to a given integer n.

list_of_primes = []

input = 1297

def prime(number) -> bool:
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
                

for i in range(1, input+1):
    if prime(i) == True:
        list_of_primes.append(i)
    
print(list_of_primes)








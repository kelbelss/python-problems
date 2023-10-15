# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# prime_number = number divisible by only 1 and itself

primeNumbers = []
list = []

numbers = 0

while numbers < 150000:
    numbers += 1
    list.append(numbers)


def is_prime(poss_prime) -> bool:

    if poss_prime > 1:
        for i in range(2,poss_prime):
            if poss_prime % i == 0:
                return False
        return True


for eachNum in list:
    if is_prime(eachNum) == True:
        primeNumbers.append(eachNum)

print(primeNumbers[10000])        



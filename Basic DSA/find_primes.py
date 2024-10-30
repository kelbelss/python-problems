# Write a function that returns a list of prime numbers up to a given integer n.

input = 3578

def prime(number) -> bool:
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
                
def list_primes(input):

    list_of_primes = []

    for i in range(1, input+1):
        if prime(i) == True:
            list_of_primes.append(i)
            
    return list_of_primes
    
print(list_primes(input))

def run_tests():
    assert prime(9) == False
    assert prime(13) == True
    assert list_primes(13) == [2, 3, 5, 7, 11, 13]
    assert list_primes(35) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    print("All tests passed!")

run_tests()






# FIBONACCI SEQUENCE

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# F1 = 1
# F2 = 1
# F3 = 2

# F12 = 144
# F25 = 75025
# F41 = 165580141
# F44 = 701408733
# F45 = 1134903170

memo = {0: None, 1: 1, 2: 1 }

# dictionary = null, n+1

def fibonnaci(n, memo):
    
    if memo[n] != None:
        return memo[n]
    
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonnaci(n - 1) + fibonnaci(n - 2)
    memo[n] = result
    return result


i = 1
# print(fibonnaci(i))


# 10**100

while fibonnaci(i) <= 10:
    i += 1
    print(fibonnaci(i))
    print(i)
          
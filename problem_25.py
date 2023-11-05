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

def fibonnaci(n):

    if n in [1,2]:
        return 1
    
    return fibonnaci (n - 1) + fibonnaci (n - 2)


i = 1
print(fibonnaci(i))


while fibonnaci(i) <= 10**100:
    i += 1
    print(fibonnaci(i))
    print(i)
          
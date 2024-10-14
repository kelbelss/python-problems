
fib = []
even = []

def fibonnaci(n):

    if n in [1,2]:
        return 1
    
    return fibonnaci (n - 1) + fibonnaci (n - 2)
    

# for i in range(1, 40): # less than 4 000 000 

i = 1 

while True:
    
    fib_num = fibonnaci(i)

    if fib_num < 4000000:
        fib.append(fib_num)
        # print(fib)
    else:
        break    
    i += 1


for i in fib:
    if (i % 2 == 0):
        even.append(i)
        # print(even)

final = sum(even)
print(final)


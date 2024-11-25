# Given a list of integers, write a function to return the sum of all even numbers.

def sum_even_numbers(input):

    even = []

    for x in input:
        if x % 2 == 0:
            even.append(x)

    return sum(even)


input = [1, 2, 3, 4, 5, 6]

print("Input:", input)

answer = sum_even_numbers(input)
print("Sum of even numbers is: ", answer)


def run_tests():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([2, 4, 6, 8]) == 20
    assert sum_even_numbers([]) == 0
    assert sum_even_numbers([1, 3, 5]) == 0
    print("All tests passed!")

run_tests()
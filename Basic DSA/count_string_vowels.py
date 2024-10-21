# Write a function to count the number of vowels (a, e, i, o, u) in a given string.

def count_vowels(input):

    vowel_count = 0

    for char in input:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": # in "aeiou" can be used
            vowel_count += 1

    return vowel_count 

input = "sunflower"

def run_tests():
    assert count_vowels("dougas") == 3
    assert count_vowels("flower") == 2
    assert count_vowels("") == 0
    assert count_vowels("hello") == 2
    print("All tests passed!")

run_tests()
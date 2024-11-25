# Write a function that checks if a given string is a palindrome (reads the same forward and backward).


def is_palindrome(word):

        if word[0] == word[-1]:
            return True
        else:
            print("letters being compared", word[0], "and", word[-1])
            return False
    

# check size of word in order to work out what must be checked  


print(is_palindrome("hello"))

# def run_tests():
#     assert is_palindrome("madam") == True
#     assert is_palindrome("flower") == False
#     assert is_palindrome("racecar") == True
#     assert is_palindrome("hello") == False
#     print("All tests passed!")

# run_tests()
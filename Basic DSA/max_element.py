# Write a function to find the largest number in a list without using the built-in max() function.

def bubble_sort(array):

    length = len(array)

    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array
   

def largest_num(arr):
    return (arr[-1])
    

full_list = [3, 5, 7, 2, 8]
bubble_sort(full_list)
print(largest_num(full_list))


def run_tests():
    assert bubble_sort([3, 1, 6, 13, 65, 3, 2, 4]) == [1, 2, 3, 3, 4, 6, 13, 65]
    assert largest_num([1, 2, 3, 3, 4, 6, 13, 65]) == 65
    
    print("All tests passed!")

run_tests()
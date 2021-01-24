# CSC 532 - Homework 1
# Dillon Harless

"""
Read in a file (called "numbers.txt") of integers.  There will be one integer per line.
Your program should:
1) read the file and keep all the values in a list of integers
2) implement a bubble sort algorithm in a function called bubble_sort(),
      use the pseudocode is provided in the textbook, in question 2-2.
3) use the bubble_sort() function to sort the values in the list
4) write the sorted list into an output file called out.txt

"""

import io

def bubble_sort(array):
    ''' Takes a list of numbers and sorts them using a variation of bubble sort. '''
    
    print("Length of array {}".format(len(array)))
    for i in range(0, len(array)):
        print('Outer iteration: {}'.format(i))
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


# create an empty list
nums = []

# open the input file
with open('numbers.txt', 'r') as input_numbers:
    # read in the lines from the input file, and add the values to the list
    for line in input_numbers:
        nums.append(int(line))

print(nums)

# bubble sort
sorted_array = bubble_sort(nums)

# write the sorted values into the output file, one value each line.
with open('numbers_sorted.txt', 'w') as file_handler:
    for i in sorted_array:
        file_handler.write('{}\n'.format(i))
    print('First 3:    {} {} {}'.format(sorted_array[0], sorted_array[1], sorted_array[2]))
    print('Last 3:    {} {} {}'.format(sorted_array[-3], sorted_array[-2], sorted_array[-1]))
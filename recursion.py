# Write a Python program to calculate the sum of a list of numbers.
'''
def sum_list(list_name):
    if len(list_name) == 1:
        return list_name[0]
    else:
        return list_name[0] + sum_list(list_name[1:])

print(sum_list([1,4,7,8,9,5]))
'''

# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
def sum_list(num_list):


# Write a Python program to calculate the sum of a list of numbers.
'''
def sum_list(list_name):
    if len(list_name) == 1:
        return list_name[0]
    else:
        return list_name[0] + sum_list(list_name[1:])

print(sum_list([1,4,7,8,9,5]))
'''
'''
# Test_Data = [1, 2, [3,4], [5,6]]
# Expected Result: 21
def sum_list(num_list):
    total = 0
    for element in num_list:
        if type(element) == type([]):
            total = total + sum_list(element)
        else:
            total = total + element
    return total
print(sum_list([1, 2, [3,4], [5,6],15]))
'''
'''
#  Write a Python program to get the factorial of a non-negative integer.
def factorial(num):
    if num <= 0:
       return 1
    else:
        num = num * factorial(num-1)
    return num

print(factorial(0))
'''

'''
# Write a Python program to solve the Fibonacci sequence using recursion.
def fibbo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fibbo(n-1) + (fibbo(n-2)))


print(fibbo(7))
'''

# sumDigits(345) -> 12
# sumDigits(45) -> 9

'''
def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))
    
print(sumDigits(345))
print(sumDigits(45))
'''
# sum_series(6) -> 12
# sum_series(10) -> 30

def sum_num(n):
    if n<0:
        return 0
    else:
        return n + sum_num(n-2)

print(sum_num(6))


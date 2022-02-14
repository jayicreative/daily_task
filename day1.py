'''
for i in range(1,100000):
    number = 0
    y = str(i)
    digits = len(y)
    digits1 = int(digits)
    y = str(i)
    for x in y:
        i = int(y)
        z = str(x)
        x1 = int(z)
        power = x1 ** digits1
        number+=power
    if number == i:
        print(number)
'''
'''
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

def who_is_jay():
    print("jay is good boy")

who_is_jay = dec1(who_is_jay)

who_is_jay()

#same task done by using decorators

def dec1(func1):
    def nowexec():
        print("executing now")
        print("executed")
        func1()
    return nowexec
@dec1
def who_is_jay():
    print("this task is done by using decorators")

#who_is_jay = dec1(who_is_jay)-->this is the task which done by decorators

who_is_jay()
'''
'''
def shandar(func):
    def wrapped():
        return "shandar " + func()
    return wrapped

def zabardast(func):
    def wrapped():
        return "zabardast " + func()
    return wrapped

def zindabad(func):
    def wrapped():
        return "zindabad " + func()
    return wrapped

@shandar
@zabardast
@zindabad
def first_name():
    return "jay"

print(first_name())
'''
'''
def f1(x=20,y=50,z=[]):


    return 5,10,20

print(f1())

# a,b,c = f1(x=20,y={},z = 30)
# print(a,b,c)
'''
'''
def xyz(start=0,end):
    print(start)
    print(end)

xyz(end=5,30)
'''
# from sys import setrecursionlimit
# from sys import getrecursionlimit
#
# print(setrecursionlimit(500))
# print(getrecursionlimit())




#
# def count_down(n):
#     if n > 1:
#         return  n*count_down(n-1)
#     else:
#           return 1
#
# print(count_down(5))

# def factorial(n):
#     return 1 if n <= 1 else n*factorial(n-1)
#
# print(factorial(5))


#
# def factorial(n):
#       print(f"factorial() called with n = {n}")
#       return_value = 1 if n <= 1 else n * factorial(n -1)
#       print(return_value)
#       return return_value
#
#
# factorial(4)








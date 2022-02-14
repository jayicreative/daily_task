#program 1
'''
num_seq = []
for i in range(2000,3201):
    if (i % 7 == 0) and (i % 5 != 0):
        num_seq.append(i)
print(num_seq)
'''
#program 2
'''
num = int(input("enter any number"))
list1 = []
num1 = 1
for i in range(num,0,-1):
    list1.append(i)
    num1 = num1*i

print(f"{list1}={num1}")
'''
'''
# program 3
number = int(input("enter any number"))
dict1 = {}
for i in range(1,number+1):
    y = i*i
    dict1[i] = y

print(dict1)
'''
'''
#program3
input1 = 34,67,55,33,12,98
list1=[]
tuple1 = tuple(input1)
print(tuple1)
for i in input1:
    list1.append(i)

print(list1)
'''
#
# lines = []
# while True:
#     l = input("say something and say finish once you done:")
#
#     if l:
#         lines.append(l.upper())
#     elif l == "finish":
#         break
# print(lines)
#
# for l in lines:
#     print(l)
'''
# program5
l=[]
for i in range(0,int(input("how many lines you want :"))):
    x = input("Enter the line : ")
    l.append(x.upper())

for i in l:
    print(i)
    # print("".join(i))
'''
# program6
sentence = input("Enter any sentence"):


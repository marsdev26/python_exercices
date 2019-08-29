# EX 1
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
year = (2019 - age) + 100
print("Turn 100 years old in ", year)


# EX 2
num = int(input("Please enter a number: "))
check = int(input("Enter a divider: "))
if num % 4 == 0:
    print("Multiple of 4")
elif num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

if num % check == 0:
    print("The result of ", num ,"divided by", check, "is even")
else:
    print("The result of ", num ,"divided by", check, "is NOT even")


# EX 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
your_num = int(input("Enter number: "))
newList = []
for num in a:
    if num < your_num:
        newList.append(num)
print(newList)

# EX 4
num = int(input("Please enter a number: "))
divisor_list = []

for i in range(1 ,num + 1):
    if num % i == 0:
        divisor_list.append(i)
print(divisor_list)

# EX 5
import random

random_list1 = random.sample(range(100), 10)
random_list2 = random.sample(range(100), 15)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = []

print(random_list1,"\n",random_list2, "\n")

for termOf1 in random_list1:
    for termOf2 in random_list2:
        if termOf1 == termOf2:
            if termOf1 in common_list:
                continue
            common_list.append(termOf1)
print(common_list)

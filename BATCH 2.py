#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

number1 = int(input("Give me ten numbers, first one = "))
number2 = int(input("second one = "))

if number1 <= number2:
    print(number1)
elif number2 <= number1:
    print(number2)

#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

if number1 != number2:
    print("not equal")

#Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

difference = int(number1) - int(number2)
print(difference)

#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

quotient = int(number1) // int(number2)
print(quotient)

#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

remainder = int(number1) % int(number2)
print(remainder)

#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

n3 = input("third = ")
n4 = input("fourth = ")
n5 = input("fifth = ")
n6 = input("sixth = ")
n7 = input("seventh = ")
n8 = input("eight = ")
n9 = input("ninth = ")
n10 = input("tenth = ")
difference2 = number1 - (number2 + int(n3) + int(n4) + int(n5) + int(n6) + int(n7) + int(n8) + int(n9) + int(n10))
print(difference2)

#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

numbers = [number1, number2, n3, n4, n5, n6, n7, n8, n9, n10]
b = [int(item) for item in numbers]
odd = 0
even = 0

for x in b:
    if x %2 == 1:
        odd += 1
    elif x %2 == 0:
        even += 1

print(f"There are a total of {even} even numbers")

#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

empty = []

for x in range(101):
    empty.append(x)

odd = []
for i in empty:
    if i %2 == 1:
        odd.append(i)

print(odd)

#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.


numbers_not_divisible_by_five = []
for a in empty:
    if a %5 != 0 and a %10 != 0: 
        numbers_not_divisible_by_five.append(a)

print(numbers_not_divisible_by_five)

#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

n1 = int(input("Give two more numbers = "))
n2 = int(input("Last one = "))

in_between = []
for b in range(n1 + 1, n2):
    in_between.append(b)

print(in_between)
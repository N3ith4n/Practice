#1 prints the bigger number

number1 = input("Give me ten numbers, first one = ")
number2 = input("second one = ")

if number1 >= number2:
    print(number1)
elif number2 >= number1:
    print(number2)

#2 prints equal if the numbers are equal

if number1 == number2:
    print("equal")

#3 Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

sum = int(number1) + int(number2)
print(sum)

#4 Create a program that ask user to input 2 numbers. Print the product of the two numbers.

product = int(number1) * int(number2)
print(product)

#5 Print the quotient of the two numbers with the decimal point

quotient = float(number1) / float(number2)
print(quotient)

#6 Print the result when the first number is raised to the second number.

exponent = int(number2) ** int(number1)
print(exponent)

#7 Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

n3 = input("third = ")
n4 = input("fourth = ")
n5 = input("fifth = ")
n6 = input("sixth = ")
n7 = input("seventh = ")
n8 = input("eight = ")
n9 = input("ninth = ")
n10 = input("tenth = ")
sum2 = int(number1) + int(number2) + int(n3) + int(n4) + int(n5) + int(n6) + int(n7) + int(n8) + int(n9) + int(n10)
print(sum2)

#8 Create a program that ask user to input 10 numbers. Print how many are odd numbers.

numbers = [number1, number2, n3, n4, n5, n6, n7, n8, n9, n10]
b = [int(item) for item in numbers]
odd = 0
even = 0

for x in b:
    if x %2 == 1:
        odd += 1
    elif x %2 == 0:
        even += 1

print(f"There are a total of {odd} odd numbers")

#9 Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

empty = []

for x in range(101):
    empty.append(x)

even = []
for i in empty:
    if i %2 == 0:
        even.append(i)

print(even)

#10 Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

numbers_without_zero = []
for a in empty:
    if a %10 != 0:
        numbers_without_zero.append(a)

print(numbers_without_zero)
        




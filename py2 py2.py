#name : Tirumala c v
#usn : Kub25EEe694
#Date : 22/08/26

#1. [3,10,15,54,75,25,23] print num divisible by 3,5,8 if none print none

num = [3, 10, 15, 54, 75, 25, 23]
found = False
for i in num:
    if i % 3 == 0 or i % 5 == 0 or i % 8 == 0:
        print(i)
        found = True
        
if not found:
    print("none")
    

# 2. [10,3,5,6,7,8,9,24,3,5,6,7,89] find the smallest and largest elements and swap them.

num = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

small = min(num)
large = max(num)

i = num.index(small)
j = num.index(large)

num[i], num[j] = num[j], num[i]

print("Smallest:", small)
print("Largest:", large)
print("After swapping:", num)

#3.[-1,3,34,-8,-9,1] replace -1 by 100.

num = [-1, 3, 34, -8, -9, 1]
num[0] = 100
print(num)

#4.[1,2,3,4],[3,4,5,6],find the average of 2 list.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

avg1 = sum(list1) / len(list1)
avg2 = sum(list2) / len(list2)

print("Average of list 1:", avg1)
print("Average of list 2:", avg2)

# 5. take the number as input and add 5 it if it is divisible by 3.

num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num + 5

print("Result:", num)

# 6.[3,10,15,54,75,25,23] print num divisible by 3 and not 5.
num = [3, 10, 15, 54, 75, 25, 23]

for i in num:
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        
#7.[10,3,5,6,7,8,9,24,3,5,6,7,89] find the elements greater than 20.
num = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for i in num:
    if i > 20:
        print(i)
        
#8.[-1,3,34,-8,-9,1] print only negetive numbers.
num = [-1, 3, 34, -8, -9, 1]

for i in num:
    if i < 0:
        print(i)
        
#9.[1,2,3,4,5,6,7,8,9] find the count of list.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = len(num)

print("Count:", count)

# 10.take the number as input and multiply 5 it if it is divisible by 3.
num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num * 5
    print("Result:",num )
else:
    print("the number is not divisible by 3:", num)

# 11.  take 2 num as input from user and check whether the sum is divisible by 5.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

if sum % 5 == 0:
    print("Sum is divisible by 5")
else:
    print("Sum is not divisible by 5")

# 12. [10,3,5,6,7,8,9,24,3,5,6,7,89] find prime numbers.
numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# 13. [-1,3,34,-8,-9,1]perfrm list operations.
numbers = [-1, 3, 34, -8, -9, 1]

print("Original list:", numbers)

numbers.append(10)
print("After append:", numbers)

numbers.insert(2, 50)
print("After insert:", numbers)

numbers.remove(-8)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.sort()
print("After sorting:", numbers)

numbers.reverse()
print("After reverse:", numbers)

# 14. [1,2,3,4,5,6,7,8,9] find the average of list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average =", average)

# 15. take the divisors from 1 to 10 and check 1578693 is divisble or not if divisible create a list of divsors that divide it.
number = 1578693
divisors = []

for i in range(1, 11):
    if number % i == 0:
        divisors.append(i)

print("Divisors:", divisors)

# 16. Take 2 num as input from user and if it divsible by 5 sqaure  the number.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 5 == 0:
    print(num1, "is divisible by 5")
    print("Square =", num1 ** 2)
else:
    print(num1, "is not divisible by 5")

if num2 % 5 == 0:
    print(num2, "is divisible by 5")
    print("Square =", num2 ** 2)
else:
    print(num2, "is not divisible by 5")

# 17. [10,3,5,6,7,8,9,24,3,5,6,7,89] find pirme numbers, even numbers and odd numbers
numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

prime = []
even = []
odd = []

for num in numbers:

    # Even and odd
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

    # Prime
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(num)

print("Prime numbers:", prime)
print("Even numbers:", even)
print("Odd numbers:", odd)

# 18. [-1,3,34,-8,-9,1]remove negetive numbers and numbers divisible by 3.
numbers = [-1, 3, 34, -8, -9, 1]

new_list = []

for num in numbers:
    if num >= 0 and num % 3 != 0:
        new_list.append(num)

print("New list:", new_list)

# 19.[1,2,3,4,5,6,7,8,9] find the average, sum, count of list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = sum(numbers)
count = len(numbers)
average = total / count

print("Sum =", total)
print("Count =", count)
print("Average =", average)

# 20. take the divisors from 1 to 10 and check 1578693 is divisible or not if divisible -100 from it.
num = 1578693

for divisor in range(1, 11):

    if num % divisor == 0:
        num = num - 100
        print("Divisible by", divisor)
        print("After subtracting 100:", num)
    else:
        print("Not divisible by", divisor)

# 21. "kishkindauniversity" count vowwls in it.
text = "kishkindauniversity"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

# 22. [10,3,5,6,7,8,9,24,3,5,6,7,89] print 89 using index and 59 to the list in 9th index.
numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89]

print(numbers[12])

numbers.insert(9, 59)

print(numbers)

# 23. [-1,3,34,-8,-9,1] square elements of the list.
numbers = [-1,3,34,-8,-9,1]

for i in numbers:
    print(i ** 2)

# 24. take 2 numbers as input and 2 floor division.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 // num2

print("Floor division:", result)

# 25. [10,3,5,6,7,8,9,24,3,5,6,7,89,7,8,54,621,57,24,3,5,6,4,]find unique values.
numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89,7,8,54,621,57,24,3,5,6,4]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Unique values:", unique)

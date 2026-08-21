# name : tirumala c v
# date : 21:08:2026
# usn: kub25EEE694

 # find even num and store it in new list
numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# consider a sting "university" and reverse it without using ::-1

string = ("university")
string = "university"

reverse_string = ""

for char in string:
    reverse_string = char + reverse_string

print(reverse_string)

# find the avreage of the list of elements
numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89]

average = sum(numbers) / len(numbers)

print(average)

# find the smallest numbers
numbers = [-1,3,34,-8,-9,1]

smallest = min(numbers)

print(smallest)

# find common elements in 3 list
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

common = set(list1) & set(list2) & set(list3)

print(common)

# print the num not divisible by 3
numbers = [3,10,42,54,75,89,25,23]

for num in numbers:
    if num % 3 != 0:
        print(num)
        
# consider a string "university" and count the characters
string = "university"
count = len(string)
print(string)

# find the second smallest elements
numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

unique_numbers.sort()

print(unique_numbers[1])


# # swap only the first and last elements
numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

# find repeating values in both the list
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)

# print the num divisible by 3 and 5
numbers = [3, 10, 15, 54, 75, 89, 25, 23]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(num)
        
#  find the smallest and largest elements
numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest = min(numbers)
largest = max(numbers)

print("Smallest:", smallest)
print("Largest:", largest)

# swap only the first and third elements
numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[2] = numbers[2], numbers[0]

print(numbers)

# find the non repeating values in both the list 
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

non_repeating = []

for num in list1:
    if num not in list2:
        non_repeating.append(num)

for num in list2:
    if num not in list1:
        non_repeating.append(num)

print(non_repeating)

# take the number as input and square it if it is divisible by 3

num = int(input("Enter a number: "))

if num % 3 == 0:
    square = num ** 2
    print("Square:", square)
else:
    print("Number is not divisible by 3")










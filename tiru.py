my_list = [5, 3, 0, 7, 2]

index = my_list.index(0)

print(index)

# consider a string "hellow world " and write a python function that reverese the string and returns it.


def reverse_string(s):
    return s[::-1]

text = "hellow world "
print(text)
print(reverse_string(text))

# consider a string "artifical intelligence"and count the number of characters in the string

text = "artificialintelligence"
count = len(text)
print("Numbers os characters :", count)

#take the input from the user and perform sum of 2 numbers.

a = 10
b = 20
sum = a + b
print("sum =",sum)

# creat a list and perform insert(), append(), remove() operations on it.

# Create a list
fruits = ["Apple", "Banana", "Mango"]

print("Original list:", fruits)

# append() - adds an item to the end
fruits.append("Orange")
print("After append():", fruits)

# insert() - adds an item at a specific position
fruits.insert(1, "Grapes")
print("After insert():", fruits)

# remove() - removes a specific item
fruits.remove("Banana")
print("After remove():", fruits)

#creat dictionary and perfrom add, update, and delete opertion on its.

 # Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"b
}

print("Original dictionary:", student)

# Add a new key-value pair
student["city"] = "Bangalore"
print("After adding city:", student)

# Update an existing value
student["age"] = 21
print("After updating age:", student)

# Delete a key-value pair
del student["course"]
print("After deleting course:", student)
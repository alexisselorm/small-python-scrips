# Lists

from sys import getsizeof
from array import array
from collections import deque
letters = ["a", "b", "c"]

matrix = [[0, 1], [2, 3]]

zeros = [0] * 5

combined = zeros + letters

numbers = list(range(20))

chars = list("Hello World")


print(chars)


# Accessing items in a list

numbers = list(range(20))

# Print items in the list by steps of two

print(numbers[::2])

# Print everything in reverse order

print(numbers[::-1])


# unpacking lists

numbers = list(range(20))

first, *others, last = numbers

print(first, last)

print(others)


# Looping over lists

chars = list("Hello World")

for index, char in enumerate(chars):

    print(index, char)


# Adding or removing items

people = ["Alexis", "Fefe", "Divine", "Kubu", "Haq", "Eugene"]


# Adding items

# Append adds items to the end of the list

people.append("Kelly")
print(people)

# insert adds items at the specified index\

people.insert(4, "O.B.O")
print(people)


# Removing items

# Pop removes items at an index

people.pop(5)
print(people)

# remove deletes a specified item

people.remove("Eugene")
print(people)

# del can be used to delete a range of items

del people[2:4]
print(people)

# clear - clears out the entire list

# people.clear()
# print(people)

# Finding items in a list
if "Alexis" in people:
    print(people.index("Alexis"))

# SORT
num = [5, 96, 8, 2, 3]
num.sort(reverse=True)
print(num)
print(sorted(num))

# Sorting a tuple
items = [("Product 5", 25), ("Product 1", 12), ("Product 3", 5), ]

# define your own sort function to specify what to sort by in a tuple

items.sort(key=lambda item: item[1])
print(items)

# Map and lambda
prices = map(lambda item: item[1], items)
for price in prices:
    print(price)

# Converting to a list and printing result
x = list(map(lambda item: item[1], items))
print(x)
# Using list comprehension to achieve same results
prices = [item[1] for item in items]
print(prices)

# Filtering from a list
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
# Using list comprehension to filter from a list.
filtered = [item for item in items if item[1] >= 10]
print(filtered)

# Zipping
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(zip("abc", list1, list2)))

# Stack - LIFO
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.pop()
if not browsing_session:
    print(browsing_session[-1])

#Queues -FIFO
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(queue)
# If queue is empty print empty
if not queue:
    print("empty")

# Tuples
point = (1, 2, 3)
x, y, z = point
print(point)
print(x, y, z)

# Swapping and assigning multiple variables on the same line
# Swapping
x = 10
y = 11
x, y = y, x
print("x ", x)
print("y ", y)
x, y = 7, 8
print("x ", x)
print("y ", y)

# Arrays. Have the same methods as lists.
numbers = array("i", [1, 2, 3])
print(numbers)

# Sets. (no duplicates)
numbers = [1, 2, 3, 4, 5, 5, 5]
first = set(numbers)
second = {1, 6}

print(first | second)  # Union
print(first & second)  # Intersection
print(first - second)  # Difference
# Symmetric difference. Either in first or second set but not both
print(first ^ second)

# Dictionaries
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
for key, value in point.items():
    print(key, value)

# Using dictionary comprehension
values = {x: x*2 for x in range(6)}
print(values)

# Generator expressions
values = (x*2 for x in range(600000))
print(getsizeof(values))

# Unpacking operator
# Unpacking lists
values = list(range(6))
print(values)
values = [*range(6)]
print(values)

# Unpacking dictionaries
first = {"x": 1}
second = {"x": 10, "y": 23}
combined = {**first, **second, "z": 5}
print(combined)

# Exercise
sentence = "This is a common interview question"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)
print(char_frequency_sorted[0])

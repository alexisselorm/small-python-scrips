# Something small for the revision week
# 1.Write a Python function to find the Max of three numbers
# 2. Write a Python function to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
import math


def findMax(a, b, c):
    list = [a, b, c]
    return max(list)


print(findMax(5, 9, 88))


def rev(string):
    string = input("Enter a string: ")
    return string[::-1]


print(rev("dcba4321"))


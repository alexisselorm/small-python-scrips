print('finding the maximum...')
numbers = [56,67,32]
print(numbers)

# function for the maximum
def function():
    print(max(numbers))

#calling of the function
function()

# Printing the reverse of a string
sample = '1234abcd'
print('finding the reverse of:', sample)
print(sample[::-1])

def add(*numbers):
    total = 0
    for number in numbers:
        total+=number
    return total

# Packing keyword arguments kwargs
def about(name,age,likes):
    sentence = f"Meet {name}. They are {age} years old and they like {likes}"
    print(sentence)

dictionary={"name":"Lumumba","likes":"Grr","age":56}
about(**dictionary)
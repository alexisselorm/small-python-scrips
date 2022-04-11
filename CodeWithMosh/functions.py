# Function that performs a task and stores the value
def greet(first_name, last_name):
    return f"Hello {first_name} {last_name}"


message = greet("Alexis", "Selorm")
file = open("message.txt", "w")
file.write(message)

# Defining a function that allows an optional argument


def increment(number, by=1):
    return number + by


print(increment(3, by=3))

# A variable number of arguments


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6))

# Function to dictionary


def save_user(**user):
    # use [] and the key to access a specific value
    print(user)
    print(user["id"])
    print(user["name"])


save_user(id=67464213, name="Jones", age=23)


def fizz_buzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizz_buzz(35))

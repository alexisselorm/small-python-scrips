# Ternary operators
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical operators
high_income = True
good_credit = False
student = True

if high_income and good_credit or not student:
    print("Eligible")
else:
    print("Not Eligible")

# Chaining Conparison Operators
age2 = 18
if age >= 18 and age < 65:
    print("Eligible")
if 18 <= age2 < 65:
    print("Eligible")

# For Loops
successful = True
for number in range(1, 4):
    print("Attempt", number, (number)*"*")
    if successful:
        print("Successful")
        break
else:
    print("Attempted three times and failed")

# Nested Loops
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# Iterables
# range function returns an iterable. Strings and Lists are also iterable
for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# While Loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
count = 0
for even in range(1, 10):
    if even % 2 == 0:
        count += 1
        print(even)

print(f"we have {count} even numbers")

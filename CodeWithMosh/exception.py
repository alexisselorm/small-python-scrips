from timeit import timeit
try:
    file = open("exception.py")
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Invalid age.")
else:
    print("No exceptions were thrown")
finally:
    file.close()


# Using the with statement to automatically close files
try:
    with open("exception.py") as file:
        print("File opened")
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Invalid age.")
else:
    print("No exceptions were thrown")

# Raising exceptions

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(0)
except ValueError as error:
    print(error)
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age



xfactor=calculate_xfactor(0)
if xfactor==None:
    pass
"""
print("Code1", timeit(code1, number=10000))
print("Code2", timeit(code2, number=10000))

# def recursivem(n):
# 	if n<1:
# 		print("n is less than 1")
# 	else:
# 		recursivem(n-1)
# 		print(n)

# recursivem(6)

def fact(n):
    assert n >= 0 and int(n) == n, 'The number must be positive'
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)


print(fact(3))


def fibo(n):
    assert n >= 0 and int(n) == n, 'The number must be positive'
    if n in [0, 1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(6))


def sumofdigits(n):
    assert n >= 0 and int(n) == n, 'The number must be positive'
    if n == 0:
        return 0
    else:
        return int(n % 10)+sumofdigits(int(n/10))


print(sumofdigits(659))


def power(base, exponent):
    assert exponent >= 0 and int(
        exponent) == exponent, "Exponent should be positive"
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base * power(base, exponent-1)


print(power(2, 6))

# greatest common divisor


def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers must be positive"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))


def decimalToBinary(n):
    assert int(n) == n, "Parameter must be an integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10*decimalToBinary(int(n/2))


print(decimalToBinary(9))


def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])


print(productOfArray([1, 2, 3]))


def recursiveRange(num):
    if num <= 0:
        return 0
    else:
        return num + recursiveRange(num-1)


print(recursiveRange(4))


def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-2) + fib(num-1)


print(fib(4))


def reverse(strng):
    if len(strng) <= 1:
        return strng
    else:
        return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


print(reverse("Alexis"))

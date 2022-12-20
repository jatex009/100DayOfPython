# using the asterix(*args) argument we literally pack every number as an input and perform the type of function
# assigned.
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 5, 8, 10, 34))

# The next argument is keyword arguments(**kwargs) which is an unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2,add=2, multiply=5)

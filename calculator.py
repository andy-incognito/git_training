def addition(a, b):
    """
    Adds two numbers, e.g 1 + 2 -> 3
    """
    pass


def substraction(a, b):
    """
    Substract two numbers, e.g 1 - 2 -> -1
    """
    pass


def multiplication(a, b):
    """
    Multiplicates two numbers, e.g 1 * 2 -> 2
    """
    pass


def division(a, b):
    """
    Divides two numbers, e.g 1 / 2 -> 0.5
    ! division with zero should raise ZeroDivisionError
    """
    if b == 0:
        raise ZeroDivisionError

# Roman se snažil
def power(a, b):
    return a ** b


def digit_sum(n):
    """ Return sum of digits, e.g digit_sum(234) -> 9"""
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

 
def substract_5(n):
    return n - 5


def add_2(n):
    return n + 2


# def your_own_function():
#     pass

import cmath
import math
import random
from math import pi
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr15 = lambda x: math.sin(pi*x)
    expr14 = lambda x: math.cos(pi*x)
    expr13 = lambda x: math.atan(x)
    expr12 = lambda x: 1/(1+x) if x != -1 else 1

    expr11 = lambda x: random.choice([x.real, x.imag])
    expr10 = lambda x: abs(x)

    expr9 = lambda x: cmath.asin(pi*x)
    expr8 = lambda x: x*cmath.asinh(1j*x.real - x.imag)
    expr7 = lambda x: (1j-x)*(1j+x) if x != -1j else 1/(1-x)
    expr6 = lambda x: (1+x)/(1-x) if x !=1 else 1/(1+x)

    ave = lambda x,y: (x+y)/2
    unave = lambda x,y: (x-y)/2

    expr5 = lambda x,y:  (x+1j*y)*cmath.exp(1j*random.uniform(-.5,.5))
    expr4 = lambda x,y: (x+y)/2
    expr3 = lambda x,y: (x-y)/2
    expr2 = lambda x,y: random.choice([x,y])
    expr1 = lambda x,y: x*y

    list_1 = [expr1, expr2, expr3, expr4, expr5] # real/complex, 2 -> 2
    list_2 = [expr6, expr7, expr8, expr9] # real/complex 1 -> 1
    list_3 = [expr12, expr13, expr14, expr15] # real 1 -> 1
    reals = [expr10, expr11] # complex -> real, 1 -> 1


    num_start = random.randint(1,10)
    num_choices = random.randint(1,10)
    num_real = random.randint(1,10)
    start = []
    choices = []
    final = []

    average = random.choice([ave, unave]) # averages or not...
    real = random.choice(reals) # makes it real

    for _ in range(num_start):
        start.append((random.choice(list_1), random.choice(list_1)))

    for _ in range(num_choices):
        choices.append(random.choice(list_2))

    for _ in range(num_real):
        final.append(random.choice(list_3))




    def returner(x, y):
        start_x, start_y = x, y


        for item1, item2 in start:
            start_x, start_y = item1(start_x, start_y), item2(start_y, start_x)

        num = average(start_x, start_y)

        for item in choices:
            num = item(num)

        num = real(num)

        for item in final:
            num = item(num)

        return num

    return returner


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)

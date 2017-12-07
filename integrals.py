def calculate_area(f, h):
    return f * h

# def fun_wrapper(function)

def linear_fun(x, a, b):
    return a*x+b

def square_fun(x, C):
    return C*x*x


def calculate_integral(range_min, range_max, step_number):
    ran = range_max - range_min
    step_width = ran / step_number
    # print(ran, step_width)
    total_a = 0
    current_step = range_min
    while current_step <= range_max:
        f = linear_fun(current_step, a=1, b=1)
        a = calculate_area(f, step_width)
        total_a += a
        current_step += step_width
    print(round(total_a, 4))

calculate_integral(-12.54, 17.455, 100000)

# # equation Y = X^2 + 4*X + 3
#
# def input_equation(equation):
#     e = equation.split()
#     print(e)
#
# input_equation("X^2 + 4*X + 3")

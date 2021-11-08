import constraint

problem = constraint.Problem()

# The maximum amount of each coin type can't be more than 60
# (coin_value*num_of_coints) <= 60

problem.addVariable("x1", range(61))  # 1 cent
problem.addVariable("x2", range(21))  # 3 cent
problem.addVariable("x3", range(13))  # 5 cent
problem.addVariable("x4", range(7))  # 10 cent
problem.addVariable("x5", range(4))  # 20 cent

problem.addConstraint(
    constraint.ExactSumConstraint(60, [1, 3, 5, 10, 20]),
    ["x1", "x2", "x3", "x4", "x5"]
)


# Where we explicitly give the order in which the weights should be allocated

# We could've used a custom constraint instead, BUT in this case the program will
# run slightly slower - this is because built-in functions are optimized and
# they find the solution more quickly
# def custom_constraint(a, b, c, d, e):
#     if a + 3*b + 5*c + 10*d + 20*e == 60:
#         return True
#     problem.addConstraint(o, ["1 cent", "3 cent", "5 cent","10 cent", "20 cent"])


# A function that prints out the amount of each coin
# in every acceptable combination
def print_solutions(solutions):
    for s in solutions:
        print("---")
        print("""
        1 cent: {0:d}
        3 cent: {1:d}
        5 cent: {2:d}
        10 cent: {3:d}
        20 cent: {4:d}""".format(s["x1"], s["x2"], s["x3"], s["x4"], s["x5"]))
        # If we wanted to we could check whether the sum was really 60
        # print("Total:", s["1 cent"] + s["3 cent"]*3 + s["5 cent"]*5 + s["10 cent"]*10 + s["20 cent"]*20)
        # print("---")


solutions = problem.getSolutions()
print_solutions(solutions)
print("Total number of ways: {}".format(len(solutions)))

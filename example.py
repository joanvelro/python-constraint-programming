"""
https://stackabuse.com/constraint-programming-with-python-constraint/
 pip install python-constraint

"""
import constraint
import numpy as np

problem = constraint.Problem()

problem.addVariable('x', [0, 1, 2, 3])
problem.addVariable('y', np.arange(-20, 20, 1))


def constraint1(x, y):
    if 8 * x + 3 * y ** 2 >= 5:
        return True


def constraint2(x, y):
    if 4 * np.sqrt(x) + 9 * y < 78:
        return True


def constraint3(y):
    if y != 0:
        return True


problem.addConstraint(constraint1, ['x', 'y'])
problem.addConstraint(constraint2, ['x', 'y'])
problem.addConstraint(constraint3, ['y'])

#  we wanted to fetch only combinations where x /= y
problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()

# Easier way to print and see all solutions
# for solution in solutions:
#    print(solution)

# Prettier way to print and see all solutions
length = len(solutions)
print("(x,y) ∈ {", end="")
for index, solution in enumerate(solutions):
    if index == length - 1:
        print("({},{})".format(solution['x'], solution['y']), end="")

    else:
        print("({},{}),".format(solution['x'], solution['y']), end="")
print("}")

from constraint import *

problem = Problem()
problem.addVariable("a", [1, 2, 3])
problem.addVariable("b", [4, 5, 6])
print(problem.getSolutions())

problem.addConstraint(lambda a, b: a * 2 == b,
                      ("a", "b"))
print('Solution 2', problem.getSolutions())

problem2 = Problem()
problem2.addVariables(["a", "b"], [1, 2, 3])
problem2.addConstraint(AllDifferentConstraint())
print(problem2.getSolutions())

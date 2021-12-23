# https://labix.org/python-constraint

from constraint import *

problem = Problem()
numpieces = 8
cols = range(numpieces)
rows = range(numpieces)
problem.addVariables(cols, rows)
for col1 in cols:
    for col2 in cols:
        if col1 < col2:
            problem.addConstraint(lambda row1, row2: row1 != row2, (col1, col2))
solutions = problem.getSolutions()

for i in range(0, len(solutions)):
    print(solutions[i])
import constraint

problem = constraint.Problem()

problem.addVariable('A', range(31))
problem.addVariable('B', range(45))
problem.addVariable('C', range(76))
problem.addVariable('D', range(101))

from tqdm import tqdm


# We have 3kg = 3,000g available
def weight_constraint(a, b, c, d):
    if (a * 100 + b * 45 + c * 10 + d * 25) <= 3000:
        return True


# We have 1dm^3 = 1,000cm^3 available
def volume_constraint(a, b, c, d):
    if (a * 8 * 2.5 * 0.5 + b * 6 * 2 * 0.5 * c * 2 * 2 * 0.5 + d * 3 * 3 * 0.5) <= 1000:
        return True


# We can't exceed $300
def value_constraint(a, b, c, d):
    if (a * 8 + b * 6.8 + c * 4 + d * 3) < 300:
        return True


problem.addConstraint(weight_constraint, "ABCD")
problem.addConstraint(volume_constraint, "ABCD")
problem.addConstraint(value_constraint, "ABCD")

solutions = problem.getSolutions()

maximum_sweetness = 0
feasible_solution = {}

# check for the maximum sweetness possible
for s in tqdm(solutions):
    current_sweetness = s['A'] * 10 + s['B'] * 8 + s['C'] * 4.5 + s['D'] * 3.5
    if current_sweetness > maximum_sweetness:
        maximum_sweetness = current_sweetness
        feasible_solution = s

print("""
The maximum sweetness we can bring is: {}
We'll bring:
{} kg A Chocolates,
{} kg B Chocolates,
{} kg C Chocolates,
{} kg D Chocolates
""".format(maximum_sweetness, feasible_solution['A'], feasible_solution['B'], feasible_solution['C'], feasible_solution['D']))

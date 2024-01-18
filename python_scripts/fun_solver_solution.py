# Add any imports you need here
from numba import jit


@jit(nopython=False)
def fun_solver(
        func, tol=0.01
        ):
    # grid over which to search for potential roots
    # Pick a step size that is 10 times larger than the tolerance
    # if the tolerance is 0.1, the step size will be 1
    step = int(1/(tol*10))
    grid = [i/step for i in range(-100*step, 101*step, 1)]
    eval = [func(i) for i in grid]
    # get the sign (+ve or -ve) of the function at each point
    sign = [eval[i]/abs(eval[i]) if eval[i] else 1 for i in range(len(eval))]
    # check for sign change
    root_range = [[grid[i], grid[i+1]]
                  for i in range(len(sign)-1) if sign[i] != sign[i+1]]

    # for each potential root,
    # use Newton Raphson method to find the root to tol
    roots = []
    for i in root_range:
        x = (i[0] + i[1])/2  # initial guess at midpoint of range
        xp = x + 2*tol  # ensure xp not in tolerance of x
        # continue searching while x remains in range and the difference
        # between the approximations is greater than the tolerance
        while abs(xp - x) > tol and (x > i[0]-1 and x < i[1]+1):
            # get the gradient at x
            m = (func(x+tol) - func(x))/tol
            # store the previous approximation
            xp = x
            # get the intercept
            x = x - func(x)/m
        roots.append(x)
    return roots

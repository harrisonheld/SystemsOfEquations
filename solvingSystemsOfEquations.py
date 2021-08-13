from sympy import *
from sympy.plotting import (plot, plot_parametric)
import mpmath
    
# declare your variables
a,b = symbols('a,b')
    
# set up your equations. these are assumed to be equal to zero
# so if you wanted a = 2b, you would rearrange it into a - 2b (= 0)
# and if you wanted a + b = 12, you would rearrange for a + b - 12 (= 0)
# so you'd write
eq1 = a - 2*b
eq2 = a + b - 12

# use the solve command like this.
sol = solve([eq1, eq2], [a, b])
# the result will be a dictionary
print(\"The solution dictionary:\", sol)

# access values by using the symbol as a key, like this
print(\"The value of 'a' is\", sol[a])
print(\"The value of 'b' is\", sol[b])

# also -
# to convert degrees to radians:
angle_deg = 180
angle_rad = mpmath.radians(angle_deg)
print(angle_deg, \"deg =\", angle_rad, \"rad\")

import numpy as np
import math
from scipy import optimize

np.random.seed(42)
N2 = 10000
w_vec2 = np.random.uniform(0.5,1.5,N2)
l_vec2 = np.empty(N2)
t_vec = np.empty(N2)

## Spørgsmål 1
def u_func(l, w, epsilon, m, nu, tau0, tau1, kappa):
    return math.log10( m+w*l-(tau0*w*l+tau1*max(w*l-kappa,0)) ) - nu*l**(1+1/epsilon)/(1+1/epsilon)

epsilon = 0.3
w = 1 # arbitrary value for w, so problem can be solved

# objective funciton (to minimize)
def value_of_choice(l,w,epsilon, m, nu, tau0, tau1, kappa):
    return -u_func(l,w,epsilon, m, nu, tau0, tau1, kappa)

# call solver
sol_case1 = optimize.minimize_scalar(
    value_of_choice,method='bounded',
    bounds=(0,1),args=(w,epsilon))

# c. unpack solution
l = sol_case1.x
u = u_func(l,w,epsilon)


## Spørgsmål 2 
N = 100
# vector of wages
w_vec = np.linspace(0.5,1.5,N)
l_vec = np.empty(N)
c_vec = np.empty(N)

# function to calculate consumption
def c_func(l, w, epsilon, m, tau0, tau1, kappa):
    return m+w*l-(tau0*w*l+tau1*max(w*l-kappa,0)) 

# calculates l and c for every value of w
for i,w in enumerate(w_vec):
    w = w_vec[i]
    sol_case1 = optimize.minimize_scalar(value_of_choice,method='bounded',bounds=(0,1),args=(w,epsilon))
    l_vec[i] = sol_case1.x
    l=l_vec[i]
    c_vec[i] = c_func(l,w,epsilon)


## Spørgsmål 3
def t_func(l, w, epsilon, m, nu, tau0, tau1, kappa):
    """ function for calculating taxes paid by each individual

    """
    return tau0*w*l+tau1*max(w*l-kappa,0)


def tax_rev(epsilon, m, nu, tau0, tau1, kappa):
    for i,w in enumerate(w_vec2):
        w = w_vec2[i]
        find_l =sol_case1(sol_case1(w, epsilon, m, nu, tau0, tau1, kappa)
        l_vec2[i] = find_l
        l=l_vec2[i]
        t_vec[i] = t_func(l,w,epsilon)

    return sum(t_vec)



    

    

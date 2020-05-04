import numpy as np
import math
from scipy import optimize


##Defining the utility function
def u_func(l, w, epsilon, m, nu, tau0, tau1, kappa):
    return math.log10( m+w*l-(tau0*w*l+tau1*max(w*l-kappa,0)) ) - nu*l**(1+1/epsilon)/(1+1/epsilon)

# objective funciton (to minimize)
def value_of_choice(l, w, epsilon, m, nu, tau0, tau1, kappa):
    return -u_func(l, w, epsilon, m, nu, tau0, tau1, kappa)

#Consumption function
def c_func(l, w, epsilon=0.3, m=1, tau0=0.4, tau1=0.1, kappa=0.4):
    return m+w*l-(tau0*w*l+tau1*max(w*l-kappa,0)) 


np.random.seed(42)
N2 = 100 #OBS! Was supposed to be 10K, but code took forever to run in Q5
w_vec2 = np.random.uniform(0.5,1.5,N2)
l_vec2 = np.empty(N2)
t_vec = np.empty(N2)

# function for calculating taxes paid by each individual
def t_func(l, w, epsilon, m, nu, tau0, tau1, kappa):
     return tau0*w*l+tau1*max(w*l-kappa,0)

# funtion for returning total tax revenue
def tax_rev(epsilon, m, nu, tau0, tau1, kappa):
    for i,w in enumerate(w_vec2):
        w = w_vec2[i]
        sol_case1 = optimize.minimize_scalar(value_of_choice,method='bounded',bounds=(0,1),args=(w,                  epsilon, m, nu, tau0, tau1, kappa))
        l_vec2[i] = sol_case1.x
        l=l_vec2[i]
        t_vec[i] = t_func(l,w,epsilon, m, nu, tau0, tau1, kappa)
    return sum(t_vec)

def obj_func(x):
    tau0=x[0]
    tau1=x[1]
    kappa=x[2]
    return -tax_rev(0.1,1,10,tau0, tau1, kappa)

    

    

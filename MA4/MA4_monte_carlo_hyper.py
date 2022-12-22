import random
import math
import numpy as np
from time import perf_counter as pc

def monte_carlo_hyper(n, d):
    '''
    How to calculate the empirical volume:
    prob_in_hyper = n(in_hyper) / n_total
                     = V_hyper / V_total
                     = V_hyper / 2**d
    Therefore:
    V_hyper = n(in_hyper) * 2**d / n_total
    '''

    #Create coordinates: List comprehension
    coord = [[random.uniform(-1, 1) for dimension in range(d)] for item in range(n)]

    sum_sq_elem = []
    for item in coord:
        result = 0
        for element in item:
            result = result + element**2
        sum_sq_elem.append(result)
    
    #Sort between inside or outside the hypersphere: Lambda and Filter
    f_in_hyper = lambda result: True if result <= 1 else False
    in_hyper = list(filter(f_in_hyper, sum_sq_elem))

    #Calculate the volumes  
    theor_volume = (math.pi ** (d/2)) / math.gamma((d / 2) + 1)
    emp_volume = 2**d * (len(in_hyper)/n)

    #Print infos
    print("Points in hypershere:\t", len(in_hyper))
    print("Empirical volume:\t", round(emp_volume, 5))
    print("Theoretical volume:\t\t", round(theor_volume, 5))
    return

if __name__ == "__main__":
    n = int(input("Type n (integer) to generate points:"))
    d = int(input("Type d (integer) to choose number of dimentions:"))
    start = pc()
    monte_carlo_hyper(n, d)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
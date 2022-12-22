import random
import math
import numpy as np
from time import perf_counter as pc
import concurrent.futures as future

def monte_carlo_hyper_parallel(n, d):
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
    emp_volume = 2**d * (len(in_hyper)/n)

    return round(emp_volume, 5)

def multiprocessing(n, d, processes=10):
    iterations = [n // processes for item in range(processes)]
    dimensions = [d for item in range(processes)]
    
    with future.ProcessPoolExecutor() as ex:
        result = ex.map(monte_carlo_hyper_parallel, iterations, dimensions)

    theor_volume = (math.pi ** (d/2)) / math.gamma((d / 2) + 1)
    emp_volume_multi = sum(result) / processes
    
    #Print infos
    print("Empirical volume:\t", round(emp_volume_multi, 5))
    print("Theoretical volume:\t\t", round(theor_volume, 5))

    return emp_volume_multi

if __name__ == "__main__":
    n = int(input("Type n (integer) to generate points:"))
    d = int(input("Type d (integer) to choose number of dimentions:"))

    
    with future.ProcessPoolExecutor() as ex:
        start = pc()
        multiprocessing(n, d)
        end = pc()
        print(f"Process took {round(end-start, 2)} seconds")
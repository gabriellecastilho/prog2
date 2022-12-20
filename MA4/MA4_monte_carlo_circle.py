import random
import math
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_circle(n):
    #Create coordinates
    coord = []
    for item in range(n):
        coord.append((random.uniform(-1, 1), random.uniform(-1, 1)))

    #Sort between inside or outside the circle
    in_circle = []
    out_circle = []
    for x, y in coord:
        if x**2 + y**2 <= 1:
            in_circle.append((x,y))
        else:
            out_circle.append((x,y))

    #Transform list in numpy array
    in_circle = np.array(in_circle)
    out_circle = np.array(out_circle)

    #Calculate empirical pi    
    pi = 4 * len(in_circle) / n

    #Print infos
    print("Points in circle:\t", len(in_circle))
    print("Empirical pi:\t\t", round(pi, 5))
    print("Real pi:\t\t", round(math.pi, 5))

    #Scatter plot
    plt.rcParams["figure.figsize"] = (5,5)
    plt.text(-0.95,1.15,f"n = {n}, p_circle = {len(in_circle)}, pi = {round(pi, 5)}")
    plt.scatter(out_circle[:,0],out_circle[:,1])
    plt.scatter(in_circle[:,0],in_circle[:,1])
    plt.savefig(f'circle_{n}.png')

    return

if __name__ == "__main__":
    n = int(input("Type n (integer) to generate points:"))
    monte_carlo_circle(n)
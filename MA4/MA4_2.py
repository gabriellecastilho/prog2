#!/usr/bin/env python3.10

from person import Person
from time import perf_counter as pc
from numba import njit
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return (fib_numba(n-1) + fib_numba(n-2))

def main():
	numbers = [number for number in range(30,46)]
	time_py = []
	time_numba = []
	time_cpp = []

	for number in numbers:
		start = pc()
		fib_py(number)
		end = pc()
		time_py.append(end-start)
		# print(f"Pure python fib({number}) took {round(end-start,2)} seconds")

	for number in numbers:
		start = pc()
		fib_numba(number)
		end = pc()
		time_numba.append(end-start)
		# print(f"Numba fib({number}) took {round(end-start,2)} seconds")

	for number in numbers:
		start = pc()
		f = Person(number)
		f.fib()
		end = pc()
		time_cpp.append(end-start)
		# print(f"C++ fib({number}) took {round(end-start,2)} seconds")

	plt.plot(time_py)
	plt.plot(time_numba)
	plt.plot(time_cpp)
	plt.savefig(f'time_py_numba_cpp.png')

if __name__ == '__main__':
	main()


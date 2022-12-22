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
	numbers1 = [number for number in range(30,46)]
	time_py1 = []
	time_numba1 = []
	time_cpp1 = []

	numbers2 = [number for number in range(20,31)]
	time_py2 = []
	time_numba2 = []
	time_cpp2 = []

	for number in numbers1:
		start = pc()
		fib_py(number)
		end = pc()
		time_py1.append(end-start)
		# print(f"Pure python fib({number}) took {round(end-start,2)} seconds")

	for number in numbers1:
		start = pc()
		fib_numba(number)
		end = pc()
		time_numba1.append(end-start)
		# print(f"Numba fib({number}) took {round(end-start,2)} seconds")

	for number in numbers1:
		start = pc()
		f = Person(number)
		f.fib()
		end = pc()
		time_cpp1.append(end-start)
		# print(f"C++ fib({number}) took {round(end-start,2)} seconds")

	for number in numbers2:
		start = pc()
		fib_py(number)
		end = pc()
		time_py2.append(end-start)
		# print(f"Pure python fib({number}) took {round(end-start,2)} seconds")

	for number in numbers2:
		start = pc()
		fib_numba(number)
		end = pc()
		time_numba2.append(end-start)
		# print(f"Numba fib({number}) took {round(end-start,2)} seconds")

	for number in numbers2:
		start = pc()
		f = Person(number)
		f.fib()
		end = pc()
		time_cpp2.append(end-start)
		# print(f"C++ fib({number}) took {round(end-start,2)} seconds")

	
	fig1 = plt.figure(1)
	plt.plot(time_numba1, 'b')
	plt.plot(time_py1, 'r')
	plt.plot(time_cpp1, 'g')
	plt.xlabel('n')
	plt.ylabel('Time (s)')
	plt.xticks(ticks=range(16), labels=numbers1)
	plt.title('Time to compute Fib(n) by varied methods')
	fig1.legend(['numba', 'py', 'cpp'])
	fig1.savefig(f'time_py_numba_cpp1.png')

	fig2 = plt.figure(2)
	plt.plot(time_numba2, 'b')
	plt.plot(time_py2, 'r')
	plt.plot(time_cpp2, 'g')
	plt.xlabel('n')
	plt.ylabel('Time (s)')
	plt.xticks(ticks=range(10), labels=numbers2)
	plt.title('Time to compute Fib(n) by varied methods')
	fig2.legend(['numba', 'py', 'cpp'])
	fig2.savefig(f'time_py_numba_cpp2.png')

	start = pc()
	fib_numba(47)
	end = pc()
	print(f"Numba fib(47) took {round(end-start,2)} seconds")

	start = pc()
	f.get(47)
	f.fib()
	end = pc()
	print(f"C++ fib(47) took {round(end-start,2)} seconds")

if __name__ == '__main__':
	main()


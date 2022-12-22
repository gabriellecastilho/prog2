#!/usr/bin/env python3.10

from person import Person
from time import perf_counter as pc
from numba import njit

@njit
def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

def main():
	f = Person(5)
	print(f.get())
	print("age:\t", f.get())
	print("fibo:\t", fib_py(f.get()))
	f.set(7)
	print(f.get())
	print("age:\t", f.get())
	print("fibo:\t", fib_py(f.get()))
	f.set(35)
	print("age:\t", f.get())
	print("fibo:\t", fib_py(f.get()))
	print("fibo c++:", f.fib(f.get()))

if __name__ == '__main__':
	start = pc()
	main()
	end = pc()
	print(f"process took {round(end-start,2)} seconds")

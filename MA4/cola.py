#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt
import numpy as np

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())

	array = np.arange(25,40)
	time_py = []
	time_cpp = []

	for i in array:
		start1 = pc()
		fib_py(i)
		end1 = pc()
		time_py.append(end1-start1)

	for j in array:
		start2 = pc()
		g = Integer(j)
		g.fib_cpp()
		end2 = pc()
		time_cpp.append(end2-start2)

	plt.plot(array, time_py, 'r-', array, time_cpp, 'b-')
	plt.savefig("Fib 25-40 plotted against time, c++ vs python")
	plt.show()


	start1p = pc()
	resultpy = fib_py(7)
	print(resultpy)
	end1p = pc()

	print(f"fib python took {round(end1p-start1p, 5)} seconds")#Took approx 27.5 minutes

	start2c = pc()
	resultcpp = f.fib_cpp()
	print(resultcpp)
	end2c = pc()

	print(f"fib c++ took {round(end2c-start2c, 5)} seconds")#Took approx 1 minute

if __name__ == '__main__':
	main()


---


#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib_cpp();
	private:
		int val;
		int fib_cpp_private(int);
	};

int Integer::fib_cpp(){
	return fib_cpp_private(val);
} 
int Integer::fib_cpp_private(int n){
	if (n <= 1){
		return n;
	}
	else {
		return (fib_cpp_private(n-1)+fib_cpp_private(n-2));
	}
}
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_fib_cpp(Integer* integer){return integer -> fib_cpp();}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}


-----
""" Python interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes = [ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
		lib.Integer_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]
		lib.Integer_fib_cpp.argtypes = [ctypes.c_void_p]
		lib.Integer_fib_cpp.restype = ctypes.c_int
		self.obj = lib.Integer_new(val)

	def get(self):
		return lib.Integer_get(self.obj)

	def set(self, val):
		lib.Integer_set(self.obj, val)
        
	def __del__(self):
		return lib.Integer_delete(self.obj)

	def fib_cpp(self):
		return lib.Integer_fib_cpp(self.obj)

----

import matplotlib.pyplot as plt
import math
import random
import numpy as np
import array
from functools import reduce
from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp
import concurrent.futures as future


def första(n):
    
    i = 0 #Så man vet att while-loopen ska gå framåt
    nc = 0 #Räknar kordinater inanför cirkeln
    x = [] #Har lagras x-koordinater för plot
    y = [] #Har lagras y-koordinater för plot
    pi = math.pi
    
    while i < n: #sålänge index är mindre än totala kordinater skapa koordinater
        
        x1 = np.random.uniform(-1,1) #randomtal på intervall -1:1
        y2 = np.random.uniform(-1,1) #annat randomtal på intervall -1:1
        x.append(x1) #lägg till det första som x-koordinat
        y.append(y2) # det andra som y-koordinat
        i += 1 #öka index så whileloopen går frammåt
        
        if math.sqrt(x1 ** 2 + y2 ** 2) < 1: # om sqrt(x^2 + y^2) < 1 så ligger koordinaterna inanför linjen 
            nc +=1 #addera isf 1 till nc
            
    #gör om listan till array för att kunna plota
    x = np.array(x) 
    y = np.array(y)

    
    #Arean för cirkeln
    area = pi * (np.random.rand(n))**2
    
    #Beskriver vad radien av cirkeln är
    r = np.sqrt(x ** 2 + y ** 2)
    
    #Delar upp i två areor
    
    area1 = np.ma.masked_where(1 < r, area) #innanför cirkeln
    area2 = np.ma.masked_where(1 >= r, area) #på eller utanför cirkeln
    
    plt.scatter(x, y, s=area1, marker='o', color='r') #plott för punkter innanför cirkeln
    plt.scatter(x, y, s=area2, marker='o', color='b' ) # plott för punkter utanför cirkeln
    plt.show()
    

    pi = 4 * (nc/n) #approximera pi
    
    return pi
    


def andra(n, d):
    r = 1
    nc = 0
    
    x = [np.random.uniform(-1,1) for ii in range(0,n)] #List comprehensions
    
    l = map(lambda z: z**2, x) #map
    
    for e in l:
        if (lambda z: d*z)(e) <= 1: #Lambda högre ordning
            nc += 1 
    
    vdr = ((math.pi**(d/2))/(math.gamma((d/2)+1)))*(r**d)
    #print(vdr)
    
    
    v = 4 * (nc/n) #approximera pi
    
    return v

#Tredje
with future.ProcessPoolExecutor() as ex:
    p1 = ex.submit(andra, 10000, 2) # Starts first→ process
    p2 = ex.submit(andra, 10000, 2) # Starts second,→ process

    r1 = p1.result() # Program waits until p1 is complete before assigning r2
    r2 = p2.result()

print("all done") # Will be printed once all processes are completed
      
if __name__ == "__main__":
    start = pc()
    andra(100000, 2)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

# Anrop        
#print(första(1000))
# approximationen för n=1000 blev 3.156
# approximationen för n=10000 blev 3.1612
# approximationen för n=100000 blev 3.145

#print(andra(100000, 2))
# Med n=100000 och d=2, Vdr=3.141592653589793, approx = 2.82044
# Med n=100000 och d=11, Vdr=1.8841038793898994, approx = 1.20664

----


#!/usr/bin/env python3
import matplotlib.pyplot as plt
from integer import Integer
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2))
def main():
#C++
	f = Integer(47)
	print(f.fib())
	#f.set(7)
	#print(f.fib())

#python
	#print(fib_py(6))

#tidtagning
	a = 30
	py = []
	inte = []
	while a < 45:
		startpy = pc()
		fib_py(a)
		endpy = pc()
		py.append(endpy-startpy)
		f = Integer(a)
		startit = pc()
		f.fib()
		endit = pc()
		inte.append(endit-startit)
		a += 1

	x = list(range(30,45))
	plt.plot(x,py,'r',x,inte,'b')
	plt.savefig('plott.png')

if __name__=='__main__':
	main()



----

#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
                int fib();
	private:
		int val;
                int fib1(int);
	};

Integer::Integer(int n){
	val = n;
	}

int Integer::get(){
        return val;
	}

int Integer::fib(){
        return fib1(val);
	}

int Integer::fib1(int n){
	if (n <= 1)
		return n;
	else
		return fib1(n-1)+fib1(n-2);
	}

void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
        int Integer_fib(Integer* integer) {return integer->fib();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}

---

""" Phyton interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes =[ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
		lib.Integer_set.argtypes = [ctypes.c_void_p, ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]
		lib.Integer_fib.argtypes = [ctypes.c_void_p]
		lib.Integer_fib.restypes = ctypes.c_int
		self.obj = lib.Integer_new(val)

	def get(self):
		return lib.Integer_get(self.obj)

	def set(self, val):
		lib.Integer_set(self.obj, val)

	def __del__(self):
		return lib.Integer_delete(self.obj)

	def fib(self):
		return lib.Integer_fib(self.obj)
    
    ---

    
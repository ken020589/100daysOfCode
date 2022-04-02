##!/usr/bin/env python
#day3 Fibonacci (Recursive)

def FibonacciNumber(i):
    if i < 2 :
        return i
    return(FibonacciNumber(i - 1) + FibonacciNumber(i - 2))

print("Fibonacci number is like Fib(n3) = Fib(n1) + Fib(n2) then n1 = 1")
n = int(input("Please inout your n = "))
print("Fib(n) = %d" % FibonacciNumber(n))
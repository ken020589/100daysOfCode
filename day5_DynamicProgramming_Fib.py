##!/usr/bin/env python
#day5 Fib with dynamic programming

# Time complexity = O(n)
# Space complexity = O(n)
F_n = {0:0, 1:1} # init stores F_0=0 & F_1=1
def DPFib(i):
    if i in F_n.keys():
        return F_n[i]
    else:
        F_n[i] = DPFib(i-1) + DPFib(i-2)
        return F_n[i]

n = int(input("Plaese input n = "))
print(DPFib(n))

# Time complexity = O(n)
# Space complexity = zero
def Bottom_up_DPFib(j):
    if j < 2:
        return j # returns F_0 & 1
    iteration = 1 # iteration = k-1, i.e., k=2 st first
    F_k1 = 1
    F_k2 = 0
    while iteration < j:
        F_k = F_k1 + F_k2
        iteration += 1
        F_k2 = F_k1
        F_k1 = F_k
    return F_k

k = int(input("Plaese input k = "))
print(Bottom_up_DPFib(k))
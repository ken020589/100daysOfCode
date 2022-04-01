##!/usr/bin/env python
#day2 operate X! & sum of Y

from re import X


operation = 1

for i in range (1, 6):
    operation = operation * i
print("5! = %d" % (operation))

operation = 0
for i in range (1, 6):
    operation += i
print("sum 1 to 5 = %d" % (operation))

print("X! = 1*2*3*....*X")
print("sum(Y) = 1+2+3+....+Y")
Operand1 = int(input("Please input your X = "))
Operand2 = int(input("Please inout your Y = "))

operation = 1
for i in range (1, Operand1 + 1):
    operation = operation * i
Operand1 = operation
print("X! = %d" % (Operand1))
operation = 0
for i in range (1, Operand2 + 1):
    operation += i
Operand2 = operation
print("sum 1 to Y = %d" % (Operand2))

if Operand1 == Operand2 :
    print("Yes X! = sum(Y)")
else:
    print("No X! != sum(Y)")
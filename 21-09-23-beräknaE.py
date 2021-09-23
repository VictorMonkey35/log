import math as m
import os

os.system('cls')

n = 10000 

x1 = 0 #start värde

x2 = 0 #startvärde


x1 = (1 + 1/n)**n

for i in range(n):
    x2 += 1/(m.factorial(i))

print(f'de två talens differens blir {x1 - x2} vilket kan antas vara ett närmevärde på 0')
print(x1)
print(x2)

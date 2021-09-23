import math as m
import os
os.system('cls')
n = 10000000
x = 0
for i in range(1, n+1):
    x=x+(-1)**(i-1)*1/(2*i-1)
print(f"4 * a = {4*x}, dvs summan är π/4")
print('')
print(f'        {m.pi}    <- riktiga pi')
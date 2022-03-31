from math import ceil
v = int(input())
flag = True
for i in range(2, ceil(int(v**0.5))):
    if v % i == 0:
        flag = False

if flag:
    print("prime")
# v = w * w (w = v**0.5)
# v = a * b

from math import ceil
v = int(input())
flag = True
for i in range(2, ceil(int(v**0.5))):
    if v % i == 0:
        print(i, v//i)

if flag:
    print("prime")
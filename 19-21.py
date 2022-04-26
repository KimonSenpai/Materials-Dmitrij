#problem 18 kompege
from functools import lru_cache


def move(a, b):
    return [solve(a + 1, b), solve(a, b + 1), solve(a*2, b), solve(a, b*2)]

@lru_cache(None)
def solve(a, b):
    if a + b >= 77:
        return -0

    mas = move(a, b)

    if all(val > 0 for val in mas):
        return -max(mas)
    else:
        return -max(val for val in mas if val <= 0) + 1


print('problem 19')
for s in range(69, 1, -1):
    if +1 in move(7, s):
        print(s)
print('problem 20')
for s in range(69, 1, -1):
    if solve(7, s) == +2:
        print(s)

print('problem 21')
for s in range(69, 1, -1):
    if solve(7, s) == -2:
        print(s)
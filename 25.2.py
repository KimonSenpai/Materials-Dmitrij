# 2594 kompege


# x = 2 * p^2
def check(v):
    div = 2
    while div*div <= v:
        if v % div == 0:
            return False
        div += 1
        
    return True

a = 113000000
b = 114000000
p = 3
res = []
while 2*p*p <= b:
    if not check(p):
        p += 2
        continue
    if 2*p*p >= a:
        res += [(2*p*p, 2*p)]
    p += 2

res.sort()
for l in res:
    print(*l)

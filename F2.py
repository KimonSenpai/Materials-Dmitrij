counter = 0

A = int(input())
B = int(input())
while True:
    C = int(input())
    if C == 0: break

    if B > A and B > C:
        counter += 1
    
    A = B
    B = C
print(counter)
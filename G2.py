i = 0
i_last = -1
min_len = 0

A = int(input())
B = int(input())
while True:
    C = int(input())
    if C == 0: break

    if B > A and B > C:
        if i_last != -1 and (min_len > i - i_last or min_len == 0):
            min_len = i - i_last
        i_last = i
    A = B
    B = C
    i += 1
print(min_len)
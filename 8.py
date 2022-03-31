
#help(str)
def to_str(n):
    s = ''
    for i in range(6):
        s += str(n%10)
        n //= 10

    return s

def check(s):
    for i in range(5):
        if (int(s[i]) + int(s[i + 1])) % 2 == 0:
            return False
    if s.find('0') == -1:
        return False
    if s.find('34') != -1:
        return False

    return True
cnt = 0
for i in range(10**6):
    if check(to_str(i)):
        cnt += 1
print(cnt)
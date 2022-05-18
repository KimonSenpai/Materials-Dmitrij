# 3091 kompege

def isPal(s):
    return s == "".join(reversed(s))

def check(s):
    if isPal(s):
        return True

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            ss = list(s)

            ss[i], ss[j] = ss[j], ss[i]
            ss = "".join(ss)
            
            if isPal(ss):
                return True
    return False

def checkStr(s: str):

    for i in range(len(s) - 7):
        ss = str(s[i:i+7])
        if check(ss):
            return True
    return False

f = open(r"D:\Downloads\24_.txt")
cnt = 0
for line in f:
    cnt += checkStr(line)

print(cnt)
import regex as re

r = re.compile(r"192\.2\d\.1\d5\.14[\n\r]*")

f = open(r"D:\Downloads\24 (6).txt")
cnt = 0
for line in f:
    #print(line)
    cnt += (r.fullmatch(line) is not None)

print(cnt)
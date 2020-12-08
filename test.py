from pip._vendor.distlib.compat import raw_input

n = int(raw_input())
d = dict()
for i in range(1, n + 1):
    d[i] = i * i

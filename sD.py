import csv
import math

with open('dat.csv', newline='') as a:
    q = csv.reader(a)
    d = list(q)

dat = d[0]

l = len(dat)
tot = 0

for w in dat:
    tot += int(w)

mean = tot/l

sl = []
for g in dat:
    c = int(g) - mean
    h = c**2
    sl.append(h)

sum = 0

for s in sl:
    sum += int(s)

res = sum/(l-1)
sd = math.sqrt(res)

print(sd)
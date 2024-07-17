print("hi")

a = ('Asyikin', 'Liam', 'Austin')
print(a[0])

b = (2, 4, 6)
print(b)
print(max(b))

for num in b:
    print(num)

#tuples and assignments
(m, n) = (10, 'asyikin')
print(m)
print(n)

#tuples and dictionaries
s = dict()
s['cat'] = 3
s['ball'] = 5
for (x, y) in s.items():
    print(x, y)

tups = s.items()
print(tups)

#tuples are comparable
compare1 = (1, 2, 3) < (6, 2, 3)
print(compare1)

compare2 = (0, 1, 2000000) < (0, 3, 4)
print(compare2)

compare3 = ('spongebob', 'patrick') < ('spongebob', 'crab')
print(compare3)

#sorting list of tuples (based on key)
d = {'w':1, 'y':2, 't':3}
print(d.items())

print(sorted(d.items()))

#using sorted
d = {'w':1, 'y':2, 't':3}
t = sorted(d.items())
for a, b in t:
    print(a, b)

#sort by values - value comes before key
print('sort by values')
d = {'w':1, 'y':2, 't':3}
tmp = list()
for p, q in d.items():
    tmp.append( (q, p))
print(tmp)

tmp = sorted(tmp, reverse=True)      #sort value in descending order
print(tmp)

#shorter version
print('shorter version')
c = {'w':1, 'y':2, 't':3, 'a':10, 'f':99}
print(sorted( [ (p, q) for q,p in c.items() ] ) )
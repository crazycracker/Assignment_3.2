# code for output ['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']
s = 'A C A D G I L D'.split()
print(s)

# code for output ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
l = list()
alphabet = ['x','y','z']
for x in alphabet:
    for y in range(1,5):
        l.append(x*y)
print(l)


# code for output ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
l = list()
for x in range(1,5):
    for y in alphabet:
        l.append(y*x)
print(l)


# code for output [[2],[3],[4],[3],[4],[5],[4],[5],[6]]
l = list()
for x in range(2,5):
    for y in range(x,x+3):
        l.append([y])
print(l)


# code for output [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
s = [ [ z for z in range(2 + x, x + 6) ] for x in range(0,4)]
print(s)


# code for output [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
l = list()
for x in range(1,4):
    for y in range(1,4):
        l.append((y,x))
print(l)

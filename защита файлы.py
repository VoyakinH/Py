f = open('mat.txt','r')
g = open('matout.txt','w')
l = (sum(1 for _ in f))
f.close()
for j in range(l):
    f = open('mat.txt','r')
    s = ''
    for i in range(l):
        buff = f.readline()
        s += buff[j]
    s += '\n'
    g.write(s)
    f.close()
g.close()

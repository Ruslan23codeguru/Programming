from collections import Counter
d = int(input())
s=[]
for i in range(d):
    s.append(int(input()))
c = Counter(s)
print(c)
for i in c:
    c[i]=[f(i)]
for i in s:
    print(c[i])
    print('jjj')
    


























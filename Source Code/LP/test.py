import random
import lp

num=256
n=80
a = [0 for x in range(num)]

for x in range(num):
	a[x] = chr(int(random.uniform(32,122)))

target = open('in.txt', 'w')
target.truncate()

for e in a:
	target.write(e)

target.close()

lp.main(num,n)


target = open('out.txt', 'r')
ms = target.read()
target.close()

g=0
b=0
x=0
for e in ms:
	if (e==a[x]): g=g+1
	else: b=b+1
	x=x+1

print float(g)/num*100
print float(b)/num*100

import random
import numpy as np

def encl(n,mu,sigma,q):
	d = np.random.normal(mu, sigma, n)
	for x in range(n):
		d[x] = int(d[x]%q)
	return d

def enc1(e1,e2,a,n1,n2,q):
	p = [0 for x in range(n1)]
	for x in range(n1):
		n=0
		for y in range(n2):
			p[x] = int((p[x] + (a[x][y]*e1[n]))%q)
		n=n+1

	for x in range(n1):
		p[x] = int((p[x] + e2[x])%q)

	return p


def enc2(e1,e2,a,n1,n2,msg,q):
	p = [0 for x in range(n1)]
	for x in range(n1):
		n=0
		for y in range(n2):
			p[x] = int((p[x] + (a[x][y]*e1[n]))%q)
		n=n+1

	for x in range(n1):
		p[x] = int((p[x] + e2[x])%((q/8)-1))

	for x in range(n1):
		p[x] = int((p[x] + int(msg[x]*(q/2)))%q)


	return p

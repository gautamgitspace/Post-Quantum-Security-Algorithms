import random
import numpy as np

def gena(n,c,q):
	a = [[0 for x in range(n)] for x in range(n)]
	for x in range(n):
		for y in range(n):
			a[x][y] = int((random.random()*c)%q)
	return a

def gens(n,l,mu,sigma,q):
	d = np.random.normal(mu, sigma, n*l)
	s = [[0 for x in range(n)] for x in range(l)]
	for x in range(l):
		for y in range(n):
			s[x][y] = int((d[(x*y)+y])%q)
	return s

def genp(n,l,a,s,e,q):
	p = [[0 for x in range(n)] for x in range(l)]
	for x in range(l):
		for y in range(n):
			for z in range(n):
				p[x][y] = p[x][y] - int((s[x][z]*a[z][y])%q)

	for x in range(l):
		for y in range(n):
			p[x][y] = int((p[x][y] + e[x][y])%q)

	return p

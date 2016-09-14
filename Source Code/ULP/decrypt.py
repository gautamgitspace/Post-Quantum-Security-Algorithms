#S*c1+c2
def dec(s,c1,c2,n1,n2,q):
	p = [0 for x in range(n1)]
	for x in range(n1):
		n=0
		for y in range(n2):
			p[x] = int((p[x] + (s[x][y]*c1[n]))%(q/8))
		n=n+1

	#print p
	for x in range(n1):
		p[x] = int((p[x] + c2[x])%q)

	#print p
	return p

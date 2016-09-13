import keygen
import encrypt
import decrypt
import time

#ms = raw_input('Enter the message: ')

def main(num,n):
	target = open('in.txt', 'r')
	ms = target.read()
	#print ms
	target.close()

	msg = ''
	q=251

	#encode
	for ch in ms:
		i = ord(ch)
		i = int(i)
		m = str(bin(i))	
		l = len(m)
		mo = "00000000"
		mo = mo[l-2:] + m[2:]
		msg = msg + mo
	
	l=len(msg)

	c=1000
	mu=1
	sigma1=215
	sigma2=21

	a=keygen.gena(n,c,q)
	s=keygen.gens(n,l,mu,sigma1,q)
	e=keygen.gens(n,l,mu,sigma1,q)
	p=keygen.genp(n,l,a,s,e,q)
	
	start = time.time()
	e1=encrypt.encl(n,mu,sigma2,q)
	e2=encrypt.encl(n,mu,sigma2,q)
	e3=encrypt.encl(l,mu,sigma2,q)
	c1=encrypt.enc1(e1,e2,a,n,n,q)
	c2=encrypt.enc2(e1,e3,p,l,n,msg,q)
	end = time.time()
	print end-start
	print "Encryptions per second:",num/(end-start)

	start = time.time()
	d1=decrypt.dec(s,c1,c2,l,n,q)
	for x in range(l):
		if (d1[x]>=(q/2)):d1[x]=1
		else:d1[x]=0

	out = ''
	for x in range(len(ms)):
		o1 = 0
		z = 7
		for y in range(8):
			o1 = o1 + (int(d1[(8*x)+y])*(2**z))
			z = z - 1
	#	print o1
		out = out + chr(o1)
	end = time.time()

	print end-start
	print "Decryptions per second:",num/(end-start)

	#print "input:\n",msg
	#print "a:\n",a
	#print "s:\n",s
	#print "p:\n",p
	#print "c1:\n",c1
	#print "c2:\n",c2
	#print "d1:\n",d1
	#print "output:\n",out

	target = open('out.txt', 'w')
	target.truncate()

	for e in out:
		target.write(e)

	target.close()

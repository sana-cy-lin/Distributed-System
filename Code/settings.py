import hashlib

#To be adjust for testing
HASH_BITS=160 		#SHA1
ID_LEN=80			#M

K_TEST=14			#K=3 to 14
N_NODES=2**K_TEST
N_KEYS=100*2**K_TEST

N_QUERIES=1
N_EXP=20

inc_none=0
inc_left=1
inc_right=2

def in_interval(n,a,b,inclusive=inc_none):
	bb=b
	nn=n
	if(b<=a):
		bb=b+2**ID_LEN
		if(n<a):
			nn=n+2**ID_LEN
		
	if(inclusive==inc_none):
		return(a<nn<bb)
	elif(inclusive==inc_left):
		return(a<=nn<bb)
	elif(inclusive==inc_right):
		return(a<nn<=bb)
	else:
		print "PARAM ERROR"
		
def generate_id(p):
	x=hashlib.sha1(p).hexdigest()
	return int(bin(int(x,16))[2:].zfill(HASH_BITS)[0:ID_LEN],2)		


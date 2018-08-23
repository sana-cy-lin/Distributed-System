"""
ASSIGNMENT OF DISTRIBUTED SYSTEM 2018:

Write a basic simulator (in the language of your choice) that simulates the Chord peer-to-peer protocol.  
Your code should support (i) node insertion and (ii) message forwarding.  
Then, simulate example scenarios and report how the overhead of node insertion and packet forwarding scales with the number of nodes in your Chord implementation.  
Your report should reflect on your findings and compare with results from the existing literature.

Resources: Original Paper: 
			https://dl.acm.org/citation.cfm?id=383071
		   Example Codes: 
			https://github.com/gaston770/python-chord
			https://github.com/lucidvision/Chord-Protocol-Algrorithm-Simulator
		   Technical Articles: 
			https://www.toptal.com/big-data/consistent-hashing
			https://medium.com/karachain/peer-to-peer-protocols-explained-3b1d947c4600
		   Existing Literature about Performance of Chord:
		    https://pdfs.semanticscholar.org/a427/212bd8991c0c12bffd01401631520180506e.pdf
			https://www.researchgate.net/profile/M_V_Subramanyam/publication/270512342_Performance_Analysis_of_Chord_Protocol_for_Peer_to_Peer_Overlay_Topology_in_Wireless_Mesh_Network/links/54acc8550cf2479c2ee8538f/Performance-Analysis-of-Chord-Protocol-for-Peer-to-Peer-Overlay-Topology-in-Wireless-Mesh-Network.pdf
"""  
import random
import socket
import struct
import string
from settings import *


from Node import *

"""
Path Length Measurement (from the original paper)
We simulate a network with N=2*K nodes and 100*2**k keys in all.
We vary k from 3 to 14 and conduct a separate experiment.
(A)We insert a random node in each experiment and repeat the experiment 20 (N_EXP) times for each k.
According to THEOREM 3. With high probability, any node joining an N-node Chord network 
will use O(log^2N) messages to re-establish the Chord routing invariants and finger tables.
(B)Each node in each experiment picked a random set of keys to query from the system,
and we measure the path length required to resolve each query on average.
In the original paper the path length is about 1/2*logN. (section 6.3)
"""

# ##############################################(A)###############################################
#CREATE IPs
# It may generate same ip addresses and then be deleted, so that causing less ip addresses problem
#g_addr_list=[socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))) for i in range(N_EXP*(N_NODES+1))]
g_addr_list=[socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))) for i in range((N_EXP+1)*(N_NODES+1))]
#keep unique ones
g_addr_list=set(g_addr_list)
#print "%d addressed created."%len(g_addr_list)

#CREATE NODES e.g., servers
#print "Creating chord network with: %s nodes and %s keys" %(N_NODES, N_KEYS)
results=[]
results_str=""
for x in range(N_EXP):
	Chord=[]

	for i in range(N_NODES):
		ip=g_addr_list.pop()
		node=Node(ip)
		#print "CurNode:%d"%node.id
		
		if(len(Chord)==0):
			node.join()
		else:
			node.join(Chord[0])
		Chord.append(node)
	#print "%d node in Chord"%len(Chord)
	
	#print "========================%d==========================="%x
	ip=g_addr_list.pop()
	node=Node(ip)
	node.join(Chord[0])
	
	results.append(len(node.insert_path))
	results_str=results_str+","+str(len(node.insert_path))
	
print "resulting insert_path:%s"%results
f= open("resInsertion.csv", "a")
f.write("\n"+str(K_TEST)+results_str)


##############################################(B)###############################################
# #CREATE IPs
# g_addr_list=[socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))) for i in range(N_NODES)]
# #keep unique ones
# g_addr_list=set(g_addr_list)
# #print "%d addressed created."%len(g_addr_list)
	
# #CREATE NODES e.g., servers
# #print "Creating chord network with: %s nodes and %s keys" %(N_NODES, N_KEYS)
# Chord=[]

# for i in range(N_NODES):
	# ip=g_addr_list.pop()
	# node=Node(ip)
	# #print "CurNode:%d"%node.id
	
	# if(len(Chord)==0):
		# node.join()
	# else:
		# node.join(Chord[0])
	# Chord.append(node)
# print "%d node in Chord"%len(Chord)
	
# #CREATE DATA
# def data_generator(type, size=6):
	# return ''.join(random.choice(type) for i in range(size))
# g_data_list=[ (data_generator(type=string.ascii_lowercase),data_generator(string.digits)) for i in range(N_KEYS)]
# g_hashed_data=[(generate_id(i[0]),i[1]) for i in g_data_list]
# print "%d data created."%len(g_hashed_data)
	
# # LOCATE DATA
# for i in g_hashed_data:
	# nn=Chord[0].find_successor(i[0])
	# nn.storage[i[0]]=i[1]

# # LOOKUP
# results=[]
# results_str=""
# for i in range(len(Chord)):
	# sequence=random.sample(g_hashed_data,N_QUERIES)
	# avg=0
	# for j, data in zip(range(len(sequence)),sequence):
		# Chord[i].(data[0])
		# #print "path:%s"%Chord[i].path
		# if j==0:
			# avg=len(Chord[i].path)
		# else:
			# avg=(avg*j+len(Chord[i].path))/float(j+1)
	# results.append(avg)
	# results_str=results_str+","+str(avg)
# print "%f:%s"%(sum(results)/float(len(results)),results)
# print str(K_TEST)+results_str

			
# f= open("resLookUp.csv", "a")
# f.write("\n"+str(K_TEST)+results_str)

	
#
# #hash ips and take m-bits (ID_LEN) as ids
# sha_bits=160
# hash_list=map(lambda x: int(bin(int(x,16))[2:].zfill(sha_bits)[0:ID_LEN],2), list(hashlib.sha1(i).hexdigest() for i in addr_list))
# #sort and make the first one as local machine
# #hash_list.sort()
# #print hash_list

# want_id=[1,8,14,21,32,38,42,48,51,56,26]
# for id in want_id:
 # if id in hash_list:
	# index=hash_list.index(id)
	# print "%d:%s"%(id,addr_list[index])

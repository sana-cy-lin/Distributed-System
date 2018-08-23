from settings import *


class Node:
	"""
	A Chord Node
	"""
	# VARIABLES FOR VALIDATION
	population=0 	# number of nodes
	path=[]			# path of lookup
	insert_path=[]	# path of node insertion 
	
	def __init__(self, ip):
		# LOCAL VARIABLES
		self.ip=ip
		self.id=generate_id(ip)
		self.predecessor=None
		self.fingers=map(lambda x: None, range(ID_LEN))
		self.storage=dict()
		
		
		Node.population+=1

	def join(self, nn=None):
		if nn:
			Node.insert_path=[]
			#print "insert_path before insertion:%d"%len(Node.insert_path)
			self.init_finger_table(nn)
			self.update_others()
			#print "insert_path after insertion:%d"%len(Node.insert_path)
			
			#move keys in (predecessor,n] from successor
			for key in sorted(self.fingers[0].storage.iterkeys()):
				if(in_interval(key,self.predecessor.id,self.id,inc_right)):
					self.storage[key]=self.fingers[0].storage[key]
					del(self.fingers[0].storage[key])
				else:
					break
		else:
			self.fingers=[self for i in range(ID_LEN)]
			self.predecessor=self

	def find_successor(self, id):	
		#print "====Node %d find successor of %d==="%(self.id, id)
		Node.path=[]
		nn=self.find_predecessor(id)
		return nn.fingers[0]			
		
	def find_predecessor(self,id):
		#print "Node %d find predecessor of %d"%(self.id, id)
		nn=self
		while(in_interval(id,nn.id,nn.fingers[0].id,inc_right)==False):
			Node.path.append(nn.id)
			Node.insert_path.append(nn.id)
			nn=nn.closet_preceding_finger(id)
		return nn
		
	def closet_preceding_finger(self,id):
		#print "Node %d find closet_preceding_finger of %d"%(self.id, id)
		for i in range(ID_LEN-1,-1,-1):
			if(in_interval(self.fingers[i].id,self.id,id)):
				return self.fingers[i]
		return self
	
	def init_finger_table(self, nn):
		self.fingers[0]=nn.find_successor(self.start(0))
		#print"set self.fingers0 %s,%d"%(self.fingers[0],self.fingers[0].id)
		self.predecessor=self.fingers[0].predecessor
		#print"set self.predecessor %d"%self.predecessor.id
		self.fingers[0].predecessor=self
		for i in range(ID_LEN-1):
			start=self.start(i+1)
			#print "finger %d: start=%d" %((i+1),start)
			if(in_interval(start,self.id,self.fingers[i].id,inc_right)):
				#print "In interval"
				self.fingers[i+1]=self.fingers[i]
			else:
				#print "Not in interval"
				self.fingers[i+1]=nn.find_successor(start)				
		 		
	def update_others(self):
		for i in range(ID_LEN):
			#p=self.find_predecessor((self.id-2**i)%(2**ID_LEN))
			#add one so that we can find the "immediate predeccesor" including the node id-2**i
			p=self.find_predecessor((self.id-2**i+1)%(2**ID_LEN))
			#print "finger: %d, predecessor: %d"%(i,p.id)
			p.update_finger_table(self,i)
			
	def update_finger_table(self,s,i):
		#print "Enter update_finger_table"
		
		#if(in_interval(s.id,self.id,self.fingers[i].id,inc_left)): 
		#original pseudo codes allow n changes itself and previous nodes
		#but we think the function should stops when it sees itself 
		if(in_interval(s.id,self.id,self.fingers[i].id)):
			self.fingers[i]=s
			p=self.predecessor
			#print "Updated node %d, finger %d, with %d"%(self.id, i, s.id)
			p.update_finger_table(s,i)
	
	def start(self, k):
		return (self.id+2**k)%(2**ID_LEN)
			
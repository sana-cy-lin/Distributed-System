def key_location(ld):
	for i in ld:
		nn=node0.find_successor(i[0])
		nn.storage[i[0]]=i[1]
		
def lookup(local, id):
	nn=loacl.find_successor(id)
	return nn.storage[id]

def node_insertion(node):
	if(len(Chord)==0):
		node.join()
	else:
		node.join(Chord[0])
	Chord.append(node
	
	
	
	
	
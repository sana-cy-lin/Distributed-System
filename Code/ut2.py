from Node import *
##############################TEST CASE FROM TECHNICAL REPORT ##############################
# When ID_LEN=6
print "UNIT TEST ID_LEN==6"
node1=Node('121.96.112.173')
node8=Node('152.226.145.165')
node14=Node('148.169.65.25')
node21=Node('97.132.193.239')
node32=Node('74.100.140.140')
node38=Node('226.113.116.215')
node42=Node('4.102.31.174')
node48=Node('111.83.143.35')
node51=Node('88.185.135.193')
node56=Node('99.3.112.103')

assert node1.id==1
assert node8.id==8
assert node14.id==14
assert node21.id==21
assert node32.id==32
assert node38.id==38
assert node42.id==42
assert node48.id==48
assert node51.id==51
assert node56.id==56

node1.join()
node8.join(node1)
node14.join(node1)
node21.join(node1)
node32.join(node1)
node38.join(node1)
node42.join(node1)
node48.join(node1)
node51.join(node1)
node56.join(node1)

assert [node8.fingers[i].id for i in range(ID_LEN)]==[14,14,14,21,32,42]
assert [node21.fingers[i].id for i in range(ID_LEN)]==[32,32,32,32,38,56]

#
# TEST key location
#
data_list=[(generate_id('sestbs'),'850500'),(generate_id('ugxxbp'),'45618'),(generate_id('zbpwzr'),'12313'),(generate_id('xjbmyo'),'45465'),(generate_id('jpidew'),'15485646')]
for i in data_list:
	nn=node1.find_successor(i[0])
	nn.storage[i[0]]=i[1]
	
assert [(key,node14.storage[key]) for key in sorted(node14.storage.iterkeys())]==[(10,'850500')]
assert [(key,node32.storage[key]) for key in sorted(node32.storage.iterkeys())]==[(24,'45465'),(30,'15485646')]
assert [(key,node38.storage[key]) for key in sorted(node38.storage.iterkeys())]==[(38,'45618')]
assert [(key,node56.storage[key]) for key in sorted(node56.storage.iterkeys())]==[(54,'12313')]

node26=Node('123.33.29.241')
node26.join(node21)
assert [node8.fingers[i].id for i in range(ID_LEN)]==[14,14,14,21,26,42]
assert [node21.fingers[i].id for i in range(ID_LEN)]==[26,26,26,32,38,56]

assert [(key,node26.storage[key]) for key in sorted(node26.storage.iterkeys())]==[(24,'45465')]
assert [(key,node32.storage[key]) for key in sorted(node32.storage.iterkeys())]==[(30,'15485646')]

#
# TEST lookup
#
nn=node1.find_successor(54)
assert nn.id==56
assert nn.storage[54]=='12313'

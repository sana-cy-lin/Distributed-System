from Node import *
# When ID_LEN=3
# HASHED ADDRESS REFERENCES
#(0)'68.211.208.177','143.222.200.67','93.79.79.2'
#(1)'49.178.72.28','68.201.229.134'
#(2)'219.227.120.70'
#(3)'231.83.146.165','33.222.81.216'
#(4)'208.155.34.162'
#(5)'251.8.106.141'
#(6)'89.125.61.67','48.152.36.195'
#(7)'29.191.165.87','188.113.15.213'
#
#HASHED KEYS REFERENCES
#(0)'ncnwtw','ribaxf'
#(1)'aeeakt'
#(2)'kxygqa','mazlvi'
#(3)'euiokz'
#(4)'mgtmik','prjmsn'
#(5)'rphale','aqsfno','meqvhc'
#(6)'rmnxjz','uykuui'
#(7)'rpptqs','dyaqyu'

print "UNIT TEST ID_LEN==3"
#
# TEST in_interval
#
assert in_interval(2,1,3)==True
assert in_interval(7,1,4)==False
assert in_interval(2,3,1)==False
assert in_interval(6,3,1)==True

assert in_interval(1,1,3)==False
assert in_interval(1,1,3,inc_left)==True
assert in_interval(1,3,1)==False
assert in_interval(1,3,1,inc_right)==True

#
# TEST closet_preceding_finger
#
node0=Node('68.211.208.177')
node1=Node('49.178.72.28')
node3=Node('231.83.146.165')
assert (node0.id, node1.id, node3.id)==(0,1,3)

node0.fingers=[node1,node3,node0]
node1.fingers=[node3,node3,node0]
node3.fingers=[node0,node0,node0]
node0.predecessor=node3
node1.predecessor=node0
node3.predecessor=node1

nn=node1.closet_preceding_finger(5)
assert nn.id==3
nn=node1.closet_preceding_finger(2)
assert nn.id==1
nn=node1.closet_preceding_finger(1)
assert nn.id==0

nn=node3.closet_preceding_finger(5)
assert nn.id==3
nn=node3.closet_preceding_finger(2)
assert nn.id==0
nn=node3.closet_preceding_finger(1)
assert nn.id==0

#
# TEST find_predecessor
#
nn=node1.find_predecessor(1)
assert nn.id==0
nn=node1.find_predecessor(2)
assert nn.id==1
nn=node1.find_predecessor(5)
assert nn.id==3

nn=node3.find_predecessor(1)
assert nn.id==0
nn=node3.find_predecessor(2)
assert nn.id==1
nn=node3.find_predecessor(5)
assert nn.id==3

nn=node0.find_predecessor(1)
assert nn.id==0
nn=node0.find_predecessor(2)
assert nn.id==1
nn=node0.find_predecessor(5)
assert nn.id==3

#
# TEST find_successor
#
nn=node1.find_successor(1)
assert nn.id==1
nn=node1.find_successor(2)
assert nn.id==3
nn=node1.find_successor(5)
assert nn.id==0

nn=node3.find_successor(1)
assert nn.id==1
nn=node3.find_successor(2)
assert nn.id==3
nn=node3.find_successor(5)
assert nn.id==0

nn=node0.find_successor(1)
assert nn.id==1
nn=node0.find_successor(2)
assert nn.id==3
nn=node0.find_successor(5)
assert nn.id==0

#
# TEST init_finger_table
#
node0.predecessor=node3
node1.predecessor=node0
node3.predecessor=node1
node5=Node('251.8.106.141')
node5.init_finger_table(node3)
assert [node5.fingers[i].id for i in range(ID_LEN)]==[0,0,1]
assert node5.predecessor.id==3

node0.predecessor=node3
node1.predecessor=node0
node3.predecessor=node1
node5=Node('251.8.106.141')
node5.init_finger_table(node1)
assert [node5.fingers[i].id for i in range(ID_LEN)]==[0,0,1]
assert node5.predecessor.id==3

node0.predecessor=node3
node1.predecessor=node0
node3.predecessor=node1
node5=Node('251.8.106.141')
node5.init_finger_table(node0)
assert [node5.fingers[i].id for i in range(ID_LEN)]==[0,0,1]
assert node5.predecessor.id==3

#
# TEST update_others
#
node0.predecessor=node3
node1.predecessor=node0
node3.predecessor=node1
node6=Node('89.125.61.67')
node6.init_finger_table(node3)
assert [node6.fingers[i].id for i in range(ID_LEN)]==[0,0,3]
assert node6.predecessor.id==3

node6.update_others()
assert [node0.fingers[i].id for i in range(ID_LEN)]==[1,3,6]
assert [node1.fingers[i].id for i in range(ID_LEN)]==[3,3,6]
assert [node3.fingers[i].id for i in range(ID_LEN)]==[6,6,0]

############################## TEST CASE FROM THE ORIGINAL PAPER ############################
#
# TEST join
#
node0=Node('68.211.208.177')
node1=Node('49.178.72.28')
node3=Node('231.83.146.165')
node0.join()

assert [node0.fingers[i].id for i in range(ID_LEN)]==[0,0,0]
assert node0.predecessor==node0
node1.join(node0)
assert [node0.fingers[i].id for i in range(ID_LEN)]==[1,0,0]
assert node0.predecessor==node1
assert [node1.fingers[i].id for i in range(ID_LEN)]==[0,0,0]
assert node1.predecessor==node0
node3.join(node0)
assert [node0.fingers[i].id for i in range(ID_LEN)]==[1,3,0]
assert [node1.fingers[i].id for i in range(ID_LEN)]==[3,3,0]
assert [node3.fingers[i].id for i in range(ID_LEN)]==[0,0,0]
assert node0.predecessor==node3
assert node1.predecessor==node0
assert node3.predecessor==node1

#
# TEST key location
#
data_list=[(generate_id('aeeakt'),'1234'),(generate_id('kxygqa'),'45618'),(generate_id('rmnxjz'),'1318')]
for i in data_list:
	nn=node0.find_successor(i[0])
	nn.storage[i[0]]=i[1]
	
assert [(key,node0.storage[key]) for key in sorted(node0.storage.iterkeys())]==[(6,'1318')]
assert [(key,node1.storage[key]) for key in sorted(node1.storage.iterkeys())]==[(1,'1234')]
assert [(key,node3.storage[key]) for key in sorted(node3.storage.iterkeys())]==[(2,'45618')]

node6=Node('89.125.61.67')
node6.join(node0)
assert [node6.fingers[i].id for i in range(ID_LEN)]==[0,0,3]
assert node6.predecessor.id==3
assert [node0.fingers[i].id for i in range(ID_LEN)]==[1,3,6]
assert [node1.fingers[i].id for i in range(ID_LEN)]==[3,3,6]
assert [node3.fingers[i].id for i in range(ID_LEN)]==[6,6,0]

assert [(key,node0.storage[key]) for key in sorted(node0.storage.iterkeys())]==[]
assert [(key,node1.storage[key]) for key in sorted(node1.storage.iterkeys())]==[(1,'1234')]
assert [(key,node3.storage[key]) for key in sorted(node3.storage.iterkeys())]==[(2,'45618')]
assert [(key,node6.storage[key]) for key in sorted(node6.storage.iterkeys())]==[(6,'1318')]

#
# TEST lookup
#
nn=node0.find_successor(6)
assert nn.id==6
assert nn.storage[6]=='1318'




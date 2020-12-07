#while loop statement example

vendors=['Cisco','Huawei','Arista','Juniper','HPE','Extreme']
while len(vendors)>0:
	print vendors.pop()
#	vendors.pop()
	print vendors

#combing the if statement with while loop statment to optimize the previous example in if_condition.py

print '''Please choose a rounting protocol using number:
1. RIP
2. EIGRP
3. IGRP
4. OSPF
5. ISIS
6. BGP'''
while True:
	protocol_option=raw_input("Please enter your choice(number 1-6): ")
	if protocol_option.isdigit() and int(protocol_option) in range(1,7):
		if int(protocol_option) in range(1,4):
			print "This routing protocol is a distance vector protocol."
		elif int(protocol_option) in range(4,6):
			print "This routing protocol is a link state protocol."
		else:
			print "This routing protocol is a path vector protocol"
		break	
	else:
		print "Invalid choice! Please enter a valid number"
  
raw_input()







raw_input()

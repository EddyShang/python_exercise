#if condition example 2
#an edited version of example 1 using in which is a better choice if there are a lot of option
print '''Please choose a rounting protocol using number:
1. RIP
2. EIGRP
3. IGRP
4. OSPF
5. ISIS
6. BGP'''

protocol_option=raw_input("Please enter your choice(number 1-6): ")
if protocol_option.isdigit() and int(protocol_option) in range(1,7):
	if int(protocol_option) in range(1,4):
		print "This routing protocol is a distance vector protocol."
	elif int(protocol_option) in range(4,6):
		print "This routing protocol is a link state protocol."
	else:
		print "This routing protocol is a path vector protocol"
else:
	print "Invalid choice! The program has been terminated!"


raw_input()

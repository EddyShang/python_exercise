#if condition example
#

print '''Please choose a rounting protocol using number:
1. RIP
2. EIGRP
3. IGRP
4. OSPF
5. ISIS
6. BGP'''

protocol_option=raw_input("Please enter your choice(number 1-6): ")
if protocol_option.isdigit() and 1<=int(protocol_option)<=6:
	if protocol_option=='1' or protocol_option=='2' or protocol_option=='3':
		print "This routing protocol is a distance vector protocol."
	elif protocol_option=='4' or protocol_option=='5':
		print "This routing protocol is a link state protocol."
	else:
		print "This routing protocol is a path vector protocol"
else:
	print "Invalid choice! The program has been terminated!"


raw_input()

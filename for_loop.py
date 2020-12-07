# this is for loop statement example in python

routing_protocols=['RIP','EIGRP','IGRP','OSPF','ISIS','BGP']
link_state_protocol=['OSPF','ISIS']
for protocols in routing_protocols:
	if protocols not in link_state_protocol:
		print protocols+" is not a link state protocol."

raw_input()	
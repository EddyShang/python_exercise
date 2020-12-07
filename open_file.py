#file manipulation example in python
file=open('vendor_list.txt','r')
print file.read()
#after reading the file, the file pointer move to the end. use tell method to verify
print "pointer location: ",file.tell()
if int(file.tell()) != 0:
	print "file pointer is not at the beginning of the file!"
else:
	print "file pointer is at the beginning of the file, ready to read file."

#if the file needed to be read again, use seek to move the pointer back to the beginning of the file.
file.seek(0)
print "pointer location: ",file.tell()
if int(file.tell()) != 0:
	print "file pointer is not at the beginning of the file!"
else:
	print "file pointer is at the beginning of the file, ready to read file."
print file.read()
print "\n"
##############################################################################################################################
#readline example
#first, reset pointer
print "-"*30
file.seek(0)
print "first line: ",file.readline()
print "second line: ",file.readline()
print "thrid line: ",file.readline()
print "pointer has moved to:",file.tell()
print "\n"
###############################################################################################################################
#readlines example
#reset pointer
print'-'*30
file.seek(0)
print file.readlines(),"\n",type(file.readlines())
print "As you can see, the return value of readlines is a list instead of a string"

#an example usage
print '-'*40
file.seek(0)
print file.readlines()
file.seek(0)
devices=file.readlines()
for i in devices:
	print i
print '\n'
print '-'*50

#another usage of readlines
#there is a file named ip.txt contains a list of unordered and unmanaged ip. using python can effectively tells how many ips are there in the file
#and print out matching ips in the file.

ip_file=open('ip.txt','r')
print "There are ",len(ip_file.readlines()),"ip addresses in the file."
ip_file.seek(0)

ct=0
for ip in ip_file.readlines():
	if ip.startswith('172.16'):
		print ip.strip()
		ct+=1
print "there are",ct,"class B ip addresses"
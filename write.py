#wrtie usage examples

#using uder r+ mode
vendor_list=open('vendor_list.txt','r+')
print "original vendor list:\n",vendor_list.read()
vendor_list.seek(0)

#write to the file where the it starts to write at the beginning of the file and overwrite existing content
vendor_list.write('Avaya')
vendor_list.close()
vendor_list=open('vendor_list.txt','r')
print "\n"
print "-"*60
print "vendor list becomes:\n",vendor_list.read()
vendor_list.seek(0)

print "As you can see, the very first item has been overwritten"
#reset the list
vendor_list.close()
vendor_list=open('vendor_list.txt','r+')
vendor_list.write('Cisco')
vendor_list.close()

#using w/w+ mode
print '-'*60
print '\n'
#first, save the vendor list content somewhere else first
origin_file = open('vendor_list.txt','r')
buffer_1=origin_file.read()+"\n"

#original content has been saved in buffer_1


vendor_list=open('vendor_list.txt','w')
vendor_list.write('test')
vendor_list.close()
vendor_list=open('vendor_list.txt','r')
#In the w mode, the origin conent will be entirely rewritten by the new argument
print "Now, the file has been overwritten with just the argument: \n", vendor_list.read(),"\n"

#restoring the file content
vendor_list=open('vendor_list.txt','w')
vendor_list.write(buffer_1)
vendor_list.close()

print '\n'
print "-"*60

#using a/a+ mode

#in a/a+ modes, the write content will append to the end of the original content
vendor_list=open('vendor_list.txt','a')
vendor_list.write('Avaya\n')
vendor_list.close()
vendor_list=open('vendor_list.txt','a+')
vendor_list.write('Aruba\n')
vendor_list.close()

vendor_list=open('vendor_list.txt','r')
print vendor_list.read()

#restore origin content using with as so that close file is no longer needed

with open('vendor_list.txt','w') as vendor_list:
	vendor_list.write(buffer_1)

#check if the file is closed
print vendor_list.closed
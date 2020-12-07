#data type: set, tuple, none
#creating a set requires the usage of set function and there is no repeated element in a set. That is every element is unique
vendors = set(['Cisco','Arista','Juniper','Cisco'])
print vendors," ",type(vendors)
#set is also orderless so that no index method in a set

#adding a new element to a set
vendors.add('Huawei')
print vendors

#removing an element from a set
vendors.remove('Arista')
print vendors

#Tuple is a special list which cannot be edited
#Tuple is ordered as list
vendors_tuple=('Cisco','Juniper','Arista','Juniper','Juniper')
print vendors_tuple
print vendors_tuple[0]
#However adding a new element to tuple would cause an error since a tuple cannot be edited
#vendors_tuple[2]='Huawei'

#Since tuple is ordered, index is a method available in tuple
vendor_name=raw_input("Enter the vendor you would like to find the index of: ")
print "the index of ",vendor_name," is ",vendors_tuple.index(vendor_name)

#count how many elements match a value
print "There are ",vendors_tuple.count('Juniper'), "Juniper value in the tuple"


#None, there is no method in None type, but it can be assigned to a variable
print type(None)
print None == 100
a=None
print 
raw_input()

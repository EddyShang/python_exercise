#
#
dict={'Vendor':'Cisco','Model':'WS-C3750E-48PD-S','Ports':48,'IOS':'12.2(55)SE12','CPU':36.3}
#dict is unordered key-value pairs
print dict
#print out a certain value use the corrsponding key:
print dict['Vendor']
print dict['IOS']
#adding a new key-value pair to the dict
dict['number of devices']=30
print dict
#changing the value of a key
dict['Model']='WS-C2960E-24PS-L'
dict['Ports']='24'
print dict
#deleting a key-value pair from the dict
del dict['number of devices']
print dict
#print the number of key-value pairs in the dict
print "There are ",len(dict)," pairs in the dictionary"
#print only keys in the dict
print dict.keys() #python 2.x
# print list(dict.keys()) #python3.x
#print only values in the dict
print dict.values() #python2.x
# print dict.values() #python3.x
print dict
#delete a pair from the dict
dict.pop('Ports')
print dict," -- Port:24 key-value pair has been removed"
#get the value of corresponding key
print dict.get('Vendor')
print dict.get('CPU')

raw_input()
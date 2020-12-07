#using paramiko to remotely login to multiple devices with ssh

import paramiko

username=raw_input("Username: ")
password=raw_input('Password: ')
file=open('ip_real.txt')

for ip in file.readlines():
	ip=ip.strip()
	print "connecting: ",ip
	ssh_client=paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip, username=username, password=password)
	print "Successfully connect to ", ip


raw_input()

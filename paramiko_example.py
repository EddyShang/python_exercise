#This is an example of using paramiko to remotely connect to cisco device based on SSH
#This example shows how to connect and config L3_SW3 with a loop interface using paramiko

#import the modules, time module is used to pause between command line inputs
#so that commands are entered properly and entirely
import paramiko
import time

ip="192.168.2.13"
username="python"
password="cisco123"

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username=username,password=password)

print ("Succesfully connected to", ip)

command=ssh_client.invoke_shell()
command.send("configure terminal\n")
command.send("interface loopback 1\n")
command.send("ip address 3.3.3.3 255.255.255.255\n")
command.send("end\n")
command.send("wr mem\n")

time.sleep(2)
output=command.recv(65535)
print (output)

ssh_client.close

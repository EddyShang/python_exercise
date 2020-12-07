#using telnetlib module to telnet cisco device L3_switch 1 and configure a lookback interface with an ip address 1.1.1.1

import telnetlib

host="192.168.2.11"
username="python"
password="cisco123"

#establishing telnet connection by passing username and password
connect=telnetlib.Telnet(host)
connect.read_until("Username:")
connect.write(username+'\n')
connect.read_until("Password:")
connect.write(password+'\n')
print "Connection has been established."

#config the connected divice with a loopback interface
connect.write("config ter\n")
connect.write("int loopback 1\n")
connect.write("ip address 1.1.1.1 255.255.255.255\n")
connect.write("end\n")
connect.write("exit\n")

print connect.read_all()
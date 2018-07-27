# Python demo script to show basic connectivity to DellEMC data center switches using the Netmiko python library
# Written by Bob Okony - DellEMC - Netowrk Architect 07/20/18
# This code is provided as is and DellEMC does not offer support or claim any responsibility for this code

from netmiko import ConnectHandler
from getpass import getpass

print '\n\n*******************************************************************************************'
print 'This demonstration program uses a Python script to send commmands through an SSH pipeline'
print 'to an OS9 or OS10 Enerprise Switch'
print 'Enter the approprate Show Command when prompted'
print '*******************************************************************************************\n'

hostip = raw_input('Enter the Host IP Address: ')
uname = raw_input('Enter your SSH User ID: ')
pword = getpass()
scommand = raw_input('Enter entire show command - i.e. show version : ')


ftos = {
    'device_type': 'dell_force10',
    'host':  hostip,
    'username': uname ,
    'password': pword,
}
device = ConnectHandler(**ftos)

output = device.send_command(scommand)
print '\nOuput from Show Command - ' +scommand, '\n'
print '***********************************************************\n'
print output



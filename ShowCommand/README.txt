A simple Python demo script (attached) that will communicate to OS9 or OS10 Enterprise based switches.   It simply takes the switch IP, SSH credentials, and a show command and pipelines it to the switch.  The output is the result from the show command fed back to the python program.  The intention to have a simple program that demonstrates how Dell OS switches can be accessed with Python.  This is a very basic script.  It does not include any error checking and the intention is to demonstrate functionality.  

Requirements:
	Switch must configured for SSH access
	Crypto keys must be in the known_hosts file.   Simply perform a ssh to the switch from the control machine to establish   entry in the known_hosts file
	IP connectivity exists between control machine and switches.  
	Uses Python version 2.x Use sudo apt-get install python-pip to install python on a Ubuntu Linux control machine.
	Load the netmiko library into the control machine  see link below for netmiko set up

http://networktocode.com/labs/tutorials/netmiko-quickstart/

To execute the script.  Copy the python script to the control machine.  At the linux prompt type:   python DellSW_show.py.  

The program will prompt for the necessary information.  Results will be displayed on the screen.


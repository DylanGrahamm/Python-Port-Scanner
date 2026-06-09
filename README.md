# Python-Port-Scanner

# What It Does?
User provides target IP and Port Range, scans the ports, if open prints and advises of the service running on that port

# What Tools are Needed And What Do They Do?
This program uses socket and threading.
Socket is used to attempt to make a connection via the port. If a successful connection is made, it retrieve the information of the service running on the port and prints this out.
Threading is used to speed up the process of port scanning, rather than iterating through each port one by one, threading allows us to attempt multiple port scans at once, speeding up the process.

# Iterations
The first iteration was a very basic slow port scanner providing info about which ports were open. It ran using a for loop, and iterated through each port testing the connection one by one. As you can imagine iterating through the all available ports (65,535) can take a while.
The second iteration I introduced multi threading with threading. This allows the program to run significantly faster as it runs the scan_port function concurrently rather than one by one.
For the third iteration I wanted to retrieve the service running on the port. I found the getservbyport function apart of socket. This ran after confirming the port was open and the service printed along with the open ports message.
Finally, rather than using the hardcoded target IP and port range I wanted to allow the user to input these themself. This was added through the basic Python command input()

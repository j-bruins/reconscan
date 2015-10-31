#!/usr/bin/env python
import subprocess
import sys

if len(sys.argv) != 3:
    print "Usage: sshrecon.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

sys.exit(0)

print "INFO: Performing hydra ssh scan against " + ip_address 
HYDRA = "hydra -L /root/oscp/pass-resources/oscp-user.lst -P /root/oscp/pass-resources/oscp-pass.lst -f -o %s/%s_sshhydra.txt -u %s -s %s ssh" % (ip_address, ip_address, ip_address, port)
try:
    results = subprocess.check_output(HYDRA, shell=True)
    resultarr = results.split("\n")
    for result in resultarr:
        if "login:" in result:
	    print "[*] Valid ssh credentials found: " + result 
except:
    print "INFO: No valid ssh credentials found"

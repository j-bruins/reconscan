#!/usr/bin/python

import sys
import os
import subprocess
from config import *

if len(sys.argv) != 3:
    print "Usage: dirbust.py <target url> <port>"
    print "Example: dirbust.py www.google.com 88"
    print "====== DO NOT RUN DIRBUST ON GOOGLE ======"
    sys.exit(0)

address = str(sys.argv[1])
port = str(sys.argv[2])
url = "http://" + address + ":" + port
#name = str(sys.argv[2])
#workspace = str(sys.argv[3])
#folders = ["/usr/share/dirb/wordlists", "/usr/share/dirb/wordlists/vulns"]
folders = ["/root/lists/Discovery/Web_Content"]

found = []
print "INFO: Starting dirb scan for " + url
for folder in folders:
    for filename in os.listdir(folder):

	outfile = "-o " + WORKSPACE + "/" + address + "/" + "dirb_" + port + "_" + filename
	#print "running dirb on " + filename
	DIRBSCAN = "dirb %s %s/%s -S -r %s" % (url, folder, filename, outfile)
        print DIRBSCAN
	try:
	    results = subprocess.check_output(DIRBSCAN, shell=True)
	    resultarr = results.split("\n")
	    for line in resultarr:
	        if "+" in line:
		    if line not in found:
		        found.append(line)
	except:
	    pass

try:
    if found[0] != "":
        print "[*] Dirb found the following items..."
        for item in found:
            print "   " + item
except:
    print "INFO: No items found during dirb scan of " + url		

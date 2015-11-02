# reconscan.py
Originally authored by Mike Czumak (T_v3rn1x) -- @ SecuritySift
Note from the Author:
[Modification, Distribution, and Attribution]:
You are free to modify and/or distribute this script as you wish.  I only ask that you maintain original
author attribution and not attempt to sell it or incorporate it into any commercial offering (as if it's 
worth anything anyway :)

Modified by Jeff Bruins

Usage: 
./reconscan.py <ipaddress>
./ftprecon.py <ipaddress> <port>
(mreconscan.py is a temp script to reincorporate batch scanning but isn't currently functional)

reconscan.py scans to target and then executes the additional scanning scripts based on the findings (smb currently disabled)

All other scripts can be used independantly of reconscan.py 

At the present time, only ftprecon has been extensively modified and is "guaranteed" to be fully functional.  The others should work but may need modification to direct output or select brute forcing parameters.


Change-log:
11-1-2015 part II

Altered reconscan usage message

Incorporated global workspace variable to all scripts

11-1-2015

Incorporated config file config.py for global variables

ftprecon updated to include Hydra brute forcing functionality


Change-log:
10-30-2015

Altered target input - now takes single target rather than list of targets

Usage function added

Altered and consolidated result directories/files - new directory for each target 

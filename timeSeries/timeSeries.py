#!/usr/bin/python

from mode1 import *

# output timer
startTime = timeit.default_timer()

print([sys.argv[1], sys.argv[2], sys.argv[3]])

if (sys.argv[1] == "-1"):
    fileName = mode1(sys.argv[2], sys.argv[3])


stopTime = timeit.default_timer()
scriptTime = stopTime - startTime
print "\nScript run in: "+str(scriptTime)+" seconds."
print "Converted file at: '"+os.path.join(os.getcwdu(), fileName)+"'\n"
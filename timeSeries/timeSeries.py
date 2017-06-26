#!/usr/bin/python

from core import *

# output timer
startTime = timeit.default_timer()

if (sys.argv[1] == "-1"):
    fileName = mode1(sys.argv[2], sys.argv[3])
elif (sys.argv[1] == "-2"):
    fileName = mode2(sys.argv[2], sys.argv[3])

stopTime = timeit.default_timer()
scriptTime = stopTime - startTime
print "\nScript run in: "+str(scriptTime)+" seconds."
print "Converted file at: '"+os.path.join(os.getcwdu(), fileName)+"'\n"
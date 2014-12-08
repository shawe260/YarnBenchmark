#!/usr/bin/python

import os
import subprocess
import logging
from defaults import * # import all the default variables for the project
import Executor.RandomExecutor
from Executor.TraceExecutor import TraceExecutor
from Executor.RandomExecutor import RandomExecutor
from Metrics.Monitor import Monitor

#Assume executed in the current directory

def testRandomExecutor():
    re = RandomExecutor()
    re.__run__()

def testTraceExecutor():
    te = TraceExecutor()
    te.__run__() 
    te.__cleanUp__()
    te.__reportMetrics__()

def testSubProcess():
    proc = subprocess.Popen("ls -al /" ,
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
            )
    
    out, err = proc.communicate()
    print out
    print "\n"
    print err

def testMonitor():
    print "Testing the monitor"
    monitor = Monitor()



logging.basicConfig(filename = LOG_FILENAME,
        level = logging.DEBUG,
        filemode = 'w',
        format = "[%(levelname)s]: %(message)s   {%(threadName)s %(module)s}" ,
        )

if __name__ == "__main__":
    #testTraceExecutor()
    
    #testRandomExecutor()

    testMonitor()

    #print "Other convenience test"
    #testSubProcess()


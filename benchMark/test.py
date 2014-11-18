#!/usr/bin/python

import subprocess
#from defaults import * # import all the default variables for the project
import Executor.RandomExecutor
from Executor.RandomExecutor import RandomExecutor

def testRandomExecutor():
    re = RandomExecutor()
    re.__run__()

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

if __name__ == "__main__":
    testRandomExecutor()

    print "Other convenience test"
    #testSubProcess()

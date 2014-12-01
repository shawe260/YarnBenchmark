#!/usr/bin/python

import threading
import subprocess
import time
import logging
import random
from defaults import *

class Job(threading.Thread):
    jobConfig = {}
    elapsedTime = None

    def __init__(self, config):
        threading.Thread.__init__(self)
        self.jobConfig = config

    def __clean__(self):
        pass

    def run(self):
        start = time.time()

        cmd = self.generateYarnCommand()
        self.runCommand(cmd)
        
        #TODO: add a simulate mode for debug that only sleep for a random period but not actually launch the application
        # time.sleep(random.randrange(5, 15))
        # Report the status, if possible, report to the metrics module
        end = time.time()
        self.elapsedTime = end - start
        logging.debug("Start time: " + time.ctime(start))
        logging.debug("End time: " + time.ctime(end))
        logging.debug("Elapsed: " + str(self.elapsedTime))

    def runCommand(self, cmd):
        logging.debug("The command to run is : " + cmd)
        proc = subprocess.Popen(cmd, 
                shell = True)
        proc.wait()
        #TODO: add a silent mode
        #    stdout = subprocess.PIPE,
        #    stderr = subprocess.PIPE)
        #out, err = proc.communicate()
        #return out, err

    def generateYarnCommand(self):
        raise NotImplementedError

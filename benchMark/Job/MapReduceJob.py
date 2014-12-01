#!/usr/bin/python

import time
import subprocess
import random
import logging
from defaults import *
from Job import Job

class MapReduceJob(Job):

    def __init__(self, config):
        #The super is needed to start a thread
        super(MapReduceJob, self).__init__(config)

    def run(self):
        logging.debug("Starting a MapReduce Job")
        super(MapReduceJob, self).run()
        
    def generateYarnCommand(self): 
        jobargs = self.jobConfig[JOB_COMMAND].replace('%d', '-' + str(int(time.time())))
        cmd = "yarn jar {0}/{1} {2} {3}".format(JOB_POOL_DIR, 
                self.jobConfig[JOB_JAR_NAME], 
                self.jobConfig[JOB_NAME], 
                jobargs)
        return cmd

   #should also consider cleanup

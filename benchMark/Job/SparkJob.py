#!/usr/bin/python

import logging
from Job import Job
from defaults import *

class SparkJob(Job):
    
    def __init__(self, config):
        super(SparkJob, self).__init__(config)

    def run(self):
        logging.debug("Starting a Spark job: " + self.jobConfig[JOB_NAME])
        super(SparkJob, self).run()
        logging.debug("Spark job: " + self.jobConfig[JOB_NAME] + " completed")

    def generateYarnCommand(self):
        cmd = 'No implemented'
        return cmd



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
        driverMemory = 512
        if JOB_AM_MEM in self.jobConfig.keys():
            driverMemory = self.jobConfig[JOB_AM_MEM] 

        numContainers = 1
        if JOB_CONTAINERS in self.jobConfig.keys():
            numContainers = self.jobConfig[JOB_CONTAINERS]

        containerMemory = 1024
        if JOB_CONTAINER_MEM in self.jobConfig.keys():
            containerMemory = self.jobConfig[JOB_CONTAINER_MEM]
        
        containerCores = 1 
        if JOB_CONTAINER_CORES in self.jobConfig.keys():
            containerCores = self.jobConfig[JOB_CONTAINER_CORES]

        cmd = "%s/bin/spark-submit" %(SPARK_HOME) \
        + " --class %s"%self.jobConfig[JOB_APP_CLASS] \
        + " --master yarn-cluster" \
        + " --num-executors %d"%numContainers \
        + " --driver-memory %dm"%driverMemory \
        + " --executor-memory %dm"%containerMemory \
        + " --executor-cores %d"%containerCores \
        + " %s %s"%(JOB_POOL_DIR + self.jobConfig[JOB_JAR_NAME], self.jobConfig[JOB_COMMAND])
        
        return cmd



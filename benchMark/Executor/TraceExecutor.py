#!/usr/bin/python

import time
import logging
from defaults import *
from Executor import Executor
from Job.JobFactory import JobFactory #questionable

class TraceExecutor(Executor):
    
    def __init__(self, timeout = 1200):
        super(TraceExecutor, self).__init__(TRACE_EXECUTOR_CONF_FILE, timeout)
        self.tracef = open(TRACE_FILE, 'r')

    def __run__(self):
        baseTime = time.time()
        nextJob = self.__getNextJob()
        while (nextJob != None):
            jobconfig = self.__getJobConfigByName(self.jobPool[nextJob['jobType']], nextJob['jobName'])
            if jobconfig == None:
                logging.warning(nextJob['jobName'] + " of " + nextJob['jobType'] + " is not exist in the config file.")
                logging.warning("skip this application")
            else:
                jobType = nextJob['jobType']
                e = JobFactory().__createJob__(jobType, jobconfig)
                curTime = time.time()
                arrt = nextJob['arrt']
                deltaTime = arrt + baseTime - curTime
                if (deltaTime > 0):
                    logging.debug("Sleep: " + str(deltaTime) + " seconds until job: " + nextJob['jobName'] + " arrives")
                    time.sleep(deltaTime)
                e.start()
                self.runningJobMap[(e, jobType, arrt)] = "Finished" #Note: Assume finished, if killed, will be update in the killapp function
            nextJob = self.__getNextJob()

        for runningJob in self.runningJobMap.keys():
            runningJob[0].join()
            
    def __getJobConfigByName(self, jobList, jobName):
        for jobConfig in jobList:
            if jobConfig[JOB_NAME] == jobName:
                return jobConfig
        return None

    def __getNextJob(self):
        if (self.tracef == None):
            return None

        line = self.tracef.readline()
        while (line != '' and line[0] == '#'): 
            line = self.tracef.readline()

        if (line == ''):
            return None

        (arrt,jobtype, jobName) = line.strip().split(',')
        # skip invalid jobs
        if (int(jobtype) >= len(self.jobType)):
            logging.error("Invalid job type " + jobtype + "!")
            logging.error("Jobtype list is : ")
            logging.error(self.jobType)
            return self.__getNextJob()

        job = {}
        job['jobType'] = self.jobType[int(jobtype)]
        job['jobName'] = jobName
        job['arrt'] = float(arrt)
        return job

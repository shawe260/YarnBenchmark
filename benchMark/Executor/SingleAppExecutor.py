#! /usr/bin/python

import logging
import time
from defaults import *
from Executor import Executor
from Job.JobFactory import JobFactory

class SingleAppExecutor(Executor):

    def __init__(self, jobType, jobName, timeout = 1200):
        super(SingleAppExecutor, self).__init__(timeout)
        self.times = SE_RUN_TIMES;
        self.appType = jobType
        self.appName = jobName

    def run(self):
        jobToRun = self.__getJobConfig()
        jobType = self.jobType[self.appType]
        print "running application %s:%s for %d times"%(jobType, self.appName, self.times)
        for x in range(0, self.times):
            e = JobFactory().__createJob__(jobType, jobToRun)
            e.start()
            self.runningJobMap[(e, jobType, time.time())] = "Finished"
            e.join()
    
    def __getJobConfig(self):
        if (len(self.jobType) < self.appType or self.appType < 0):
            print "Error: the job type should be from 0 to %d"%len(self.jobType)
            exit()
        for jobConfig in self.jobPool[self.jobType[self.appType]]:
            if jobConfig[JOB_NAME] == self.appName:
                return jobConfig

        print "No application %s:%s found in pool"%(self.jobType[self.appType], self.appName)
        exit()

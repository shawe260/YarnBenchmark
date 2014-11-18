#!/usr/bin/python

import time
import json
import random
from defaults import *
from Executor import Executor
from Job.JobFactory import JobFactory #questionable

# need something like a job pool
# TODO: could also black list some applications
class RandomExecutor(Executor):
    # job pool should be extract to the abstract class, but I do it now here for the easinest of testing and will be move out soon
    jobPool = {}
    executorConfig = {}
    jobType = ['MapReduce'] # A list of existing job types
    
    def __init__(self):
       #generate the jobPool
        self.__loadExecutorConfig()
        self.__loadJobPool()
        pass 

    # this can actually put in the abstract class. the extended excutor only have to implement the getNextJob function
    def __run__(self):
        duration = self.executorConfig['duration']
        start = time.time()
        while (start + duration > time.time()): 
            nextJob = self.__getNextJob()
            e = JobFactory().__createJob__(nextJob['jobType'], self.jobPool[nextJob['jobType']][nextJob['jobNo']])
            e.start()
            time.sleep(5)

    def __getNextJob(self):
        randJob = {}
        randJobType = self.jobType[random.randrange(0, len(self.jobType))]
        randJob['jobType'] = randJobType
        randJobNo = random.randrange(0, len(self.jobPool[randJobType]))
        randJob['jobNo'] = randJobNo
        return randJob

    def __loadJobPool(self): #should be in abstract
        jobPoolFd = open(JOB_CONF_FILE, 'r') # make it to MapReduce config file
        self.jobPool = json.load(jobPoolFd)
        jobPoolFd.close()

    def __loadExecutorConfig(self):
        reConfigFd = open(RAND_EXECUTOR_CONF_FILE, 'r')
        self.executorConfig = json.load(reConfigFd) 
        reConfigFd.close()

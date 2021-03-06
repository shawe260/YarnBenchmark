#!/usr/bin/python

import time
import random
import logging
from defaults import *
from Executor import Executor
from Job.JobFactory import JobFactory #questionable

class RandomExecutor(Executor):
    blackList = {} # {jobtype : [jobName1, jobName2], ...}
    
    def __init__(self, timeout):
        super(RandomExecutor, self).__init__(timeout)
        self.blackList = RE_BLACK_LIST
        if (RE_GENERATE_TRACE_ON):
            self.trace = open(RE_TARGET_TRACE_FILE, 'w')

    def run(self):
        duration = RE_GEN_DURATION
        randlow = RE_GEN_RAND_LOW
        randhigh = RE_GEN_RAND_HIGH
        start = time.time()
        while (start + duration > time.time()): 
            nextJob = self.__getNextJob()
            if len(nextJob.keys()) == 0:
                logging.error("No available job to generate")
                break;
            jobType = nextJob['jobType']
            jobConfig = self.jobPool[nextJob['jobType']][nextJob['jobNo']]
            e = JobFactory().__createJob__(jobType, jobConfig)
            arrt = time.time()
            e.start()
            self.runningJobMap[(e, jobType, arrt)] = "Finished" #Note: Assume Finished, if killed, will be updated in the killapp function
            record = "%f,%d,%s\n"%(arrt-start, self.jobType.index(jobType),jobConfig[JOB_NAME])
            self.trace.write(record)
            time.sleep(random.randrange(randlow, randhigh))
        self.trace.close()


    def __getNextJob(self):
        randJob = {}
        cnt = 0 
        getJobTimeout = 10
        start = time.time()
        while (len(randJob.keys()) == 0 and (start + getJobTimeout) > time.time()): 
            randJobType = self.jobType[random.randrange(0, len(self.jobType))]
            randJobNo = random.randrange(0, len(self.jobPool[randJobType]))
            # check if the randomGenerated job is in the blacklist
            if (randJobType in self.blackList.keys()) and (self.jobPool[randJobType][randJobNo][JOB_NAME] in self.blackList[randJobType]):
                continue

            randJob['jobType'] = randJobType
            randJob['jobNo'] = randJobNo

        return randJob



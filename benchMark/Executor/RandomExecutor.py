#!/usr/bin/python

import time
import random
from defaults import *
from Executor import Executor
from Job.JobFactory import JobFactory #questionable

# TODO: could also black list some applications
class RandomExecutor(Executor):
    # blacklist 
    def __init__(self, timeout):
        super(RandomExecutor, self).__init__(RAND_EXECUTOR_CONF_FILE, timeout)

    def __run__(self):
        # should also be able to construct a log
        # duration is the lasting period that it keep generating different jobs
        duration = self.executorConfig['duration']
        start = time.time()
        while (start + duration > time.time()): 
            nextJob = self.__getNextJob()
            e = JobFactory().__createJob__(nextJob['jobType'], self.jobPool[nextJob['jobType']][nextJob['jobNo']])
            e.start()
            time.sleep(random.randrange(10, 100))
        #add to job map

    def __getNextJob(self):
        #add blacklist
        randJob = {}
        randJobType = self.jobType[random.randrange(0, len(self.jobType))]
        randJob['jobType'] = randJobType
        randJobNo = random.randrange(0, len(self.jobPool[randJobType]))
        randJob['jobNo'] = randJobNo
        return randJob



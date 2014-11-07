#!/usr/bin/python

import time
from Executor import Executor
from Job.JobFactory import JobFactory #questionable

class RandomExecutor(Executor):
    def __init__(self):
        pass 

    def __run__(self):
        print "\ncreating a random job: <MapReduce, Randomwriter>"
        e = JobFactory().__createJob__('MapReduce')
        e.start()
        time.sleep(8)
        print "\ncreating a random job: <Spark, pi>"
        e1 = JobFactory().__createJob__('Spark')
        e1.start()
        e.join()
        e1.join()

    def __getNextJob(self):
        pass

if __name__ == "__main__":
    e = RandomExecutor()
    e.__run__()

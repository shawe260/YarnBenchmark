#!/usr/bin/python

from MapReduceJob import MapReduceJob
from SparkJob import SparkJob

class JobFactory:
    def __init__(self):
        pass

    def __createJob__(self, jobType, config):
        return {
            'MapReduce': MapReduceJob( config),
            'Spark': SparkJob('pi')
        }.get(jobType, "Not correct")

if __name__ == "__main__":
    m = JobFactory().__createJob__('MapReduce')
    m.start()
